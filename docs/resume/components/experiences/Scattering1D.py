# system/IO 
import time
import itertools
import copy

# math/numerical
import numpy as np
import sympy as sp

# special characters
import unicodeit as ucode

# plotting 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcl
import matplotlib.cm as cm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# logging and progress 
from tqdm.auto import tqdm
from logzero import logger

def FiniteBarrier( grid, vmax, width_fraction, offset=0 ):
    mn, mx = grid.min(), grid.max()
    barrier_center = offset + ( mx + mn ) / 2
    barrier_width = ( mx - mn )*width_fraction
    V = np.zeros( grid.shape )
    V[ np.where( np.abs( grid - barrier_center ) < barrier_width/2 ) ] = vmax
    return V

def PlotComplexField1D( x, y, cmap=cm.hsv ):
    '''
    hsv is visually the best cyclic color map, ideal for complex phase representations 
    '''
    assert y.dtype == 'complex', 'y should be a complex-valued array. '

    mag = np.abs( y )
    phase = np.angle( y )
    
    norm = mcl.Normalize( vmin = phase.min(), vmax = phase.max() )
    c_fill = cmap( norm( phase ) )
    
    x_fill = x[:,np.newaxis] + 0.5*epsilon*np.array( [ -1, 1 ] )[np.newaxis,:]
    y_fill = np.concatenate( ( mag[:,np.newaxis], )*2, axis=1 )
    for nn in range( x_fill.shape[0] ):
        ax.fill_between( x_fill[nn,:], y_fill[nn,:], color=c_fill[nn] )

    return norm

############################## user edit ########################################################
L = 1
J = 1000 # spatial grid points
N = 100  # temporal grid points
lam = 1/2
Vmax = 3e5
k0 = 625
tol = 1e-3 # reciprocal space tolerance, used to determine other tolerances
s0 = 2/( 2**6 )
width_fraction=0.05
##################################################################################################

x = np.linspace( -L/2, L/2, J ) # spatial grid points
epsilon = 1 / ( J - 1 )
delta = 4*epsilon**2 / lam
lam = 4*epsilon**2 / delta
km = tol * np.pi/epsilon

pstr = '%s = %e'
logger.info( pstr%( ucode.replace( '\\epsilon' ), epsilon ) )
logger.info( pstr%( ucode.replace( '\\delta' ), delta ) )
logger.info( pstr%( ucode.replace( 'k_0' ), k0 ) )
logger.info( 'Condition #3: %e'%( ( 4*N*epsilon**2)/(lam*s0**2) )**2 )
logger.info( 'Condition #4: %e'%( (km*epsilon)**2/12 ) )
logger.info( 'Condition #5: %e'%( (Vmax*epsilon)**2/12 ) )
logger.info( 'Condition #6: %e'%( N*delta**3*( km**6-k0**6 )/12 ) )

# uncomment the next line for a single finite barrier potential
# V = FiniteBarrier( x, Vmax, width_fraction=width_fraction )

# uncomment the next line for a grating of barrier potentials
V = np.zeros( x.size )
for loc in list( np.linspace( -0.1, 0.1, 3 ) ):
    V += FiniteBarrier( x, Vmax, width_fraction, loc )

psi = 1 / ( np.sqrt( 2*np.pi ) * s0 ) * np.exp( 1.j*k0*x ) * np.exp( -0.5 * ( ( x+0.35 )/s0 )**2 ) 
psi = psi.astype( complex )

# aux definitions
twominusilam = 2 - 1.j*lam
twoplusilam = 2 + 1.j*lam
epsq = epsilon**2

# creating arrays
F = np.zeros( V.shape ).astype( complex )
E = np.zeros( V.shape ).astype( complex )

Omega = np.zeros( V.shape ).astype( complex )

E[0] = twominusilam + epsq*V[0]
for j in range( 1, E.shape[0] ):
    E[j] = twominusilam + epsq*V[j] - 1/E[j-1]

fig, ax = plt.subplots()
ax2 = ax.twinx()
color_cycle = itertools.cycle( mcl.TABLEAU_COLORS )
for myax, y, color, lbl in zip( [ ax, ax2 ], [ V, np.abs( E ) ], color_cycle, [ '$V(\\boldsymbol{x})$', '${|E(\\boldsymbol{x})|}$' ] ):
    myax.plot( x, y, color=color )
    myax.tick_params( axis='y', colors=color )
    myax.set_ylabel( lbl, color=color )
ax.set_xlabel( '$\\boldsymbol{x}$ (a.u.)' )
plt.tight_layout()

# initial frame

fig = plt.figure( figsize=( 13, 5 ) )
ax = fig.subplots()

ax_col1 = 'red'
line, = ax.plot( x, np.abs( psi ), color=ax_col1 )

# ax_col1 = 'black'
# norm = PlotComplexField1D( x, psi )

titl = ax.set_title( 'Time step: 0' )
ax.set_ylim( [ -0.1, 3*np.abs( psi ).max() ] )
ax.tick_params( axis='y', colors=ax_col1 )
ax.set_ylabel( '$\\left|\\psi(x)\\right|$', color=ax_col1 )

col_ax2 = 'black'
ax2 = ax.twinx()
ax2.plot( x, V, color=col_ax2 )
ax2.set_ylim( [ -0.1, 2*np.abs( V ).max() ] )
ax2.tick_params( axis='y', colors=col_ax2 )
ax2.set_ylabel( '$V(x)$', color=col_ax2 )

ax.set_xlabel( '$x$ (normalized)' )

# axins1 = inset_axes(
#     ax,
#     width='50%',  # width: 50% of parent_bbox width
#     height='5%',  # height: 5%
#     loc='upper left'
# )
# axins1.xaxis.set_ticks_position("bottom")
# phaserange = np.linspace( -np.pi, np.pi, 100 )
# phdisp = np.meshgrid( phaserange, np.linspace( 0, 1, 10 ) )
# axins1.pcolormesh( phdisp[0], phdisp[1], phdisp[0], cmap=cm.hsv )
# axins1.set_yticks( [] )
# axins1.set_xlabel( 'Complex phase' )

# plt.tight_layout()


def animate( n ):
    # logger.info( 'Step = %d'%n )
    Omega[1:-1] = -psi[2:] + ( twoplusilam + epsq*V[1:-1] )*psi[1:-1] - psi[:-2]
    F[0] = Omega[0]
    for j in range( 1, F.shape[0] ): # forward pass
        F[j] = Omega[j] + F[j-1]/E[j-1] 
    psi[-2] = -F[-2]/E[-2]
    for j in range( J-3, -1, -1 ): # backward pass
        psi[j] = ( psi[j+1] - F[j] ) / E[j]
    # psi[0] = psi[1]
    # psi[-1] = psi[-2]
    # for coll in ax.collections: 
    #     coll.remove()
    # _ = PlotComplexField1D( x, psi )    
    line.set_ydata( np.abs( psi ) )
    titl.set_text( 'Time: %d'%n )
    return 

ani = animation.FuncAnimation( fig, animate, frames=400, blit=True, repeat=False )
plt.show()