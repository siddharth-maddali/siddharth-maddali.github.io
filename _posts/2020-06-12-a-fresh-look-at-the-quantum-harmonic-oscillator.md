---
layout: new
mathjax: true
author: Siddharth Maddali
categories: [Mathematics]
tags: [linear algebra, quantum mechanics, Fourier transform, operators, mathematics, physics, harmonic oscillators, Heisenberg, uncertainty]
---

{% include mathjax.html %}
A textbook favorite re-analyzed in the light of position-momentum similarity.

# Introduction
This post describes clever way to understand a physics undergraduate staple, namely the Schrödinger equation for the harmonic oscillator. 
I'll show how a lot of it can be realized with the help of the [position-momentum similarity relations](https://siddharth-maddali.github.io/mathematics/2020/02/15/position-and-momentum-are-similar-in-nature.html) described in an earlier blog post.
These relations continue to throw up interesting new ways of understanding things in quantum mechanics and signal processing and I'm happy to have found yet another use for them!

For completeness, the Schrödinger equation of the one-dimensional harmonic oscillator of mass $m$ and angular feequency $\omega$ is: 
$$
\begin{align}
	\left(
		-\frac{\hbar^2}{2m}\hat{D}_X^2 + \frac{1}{2}m\omega^2\hat{X}^2
	\right) \Psi(x) = E\Psi(x) \label{eq.sho}
\end{align}
$$
where $\hat{X}$ and $\hat{D}\_X$ are the usual linear operators defined by:
$$
\begin{align}
	\hat{X}(x, x^\prime)\Psi(x^\prime) &\equiv x\Psi(x) \label{eq.pos} \\
	\hat{D}_X(x, x^\prime)\Psi(x^\prime) &\equiv \left. \frac{d}{dx^\prime}\Psi(x^\prime) \right|_{x^\prime = x} \label{eq.grad} \\ 
	\text{for any } \Psi~&\in \mathcal{H} \equiv \left\{ f:\mathbb{R} \rightarrow \mathbb{C} \left| \int_\mathbb{R} dx \left|f(x)\right|^2 < \infty\right.\right\} \label{eq.hilbert}
\end{align}
$$
They also satisfy the commutation relation: $\left[\hat{X}, \hat{D}\_X\right] = -\mathbb{I}$, where $\mathbb{I}$ is the identity operator.
$E$ is the total energy of the oscillator (potential + kinetic).

The similarity relations linking them are: 
$$
\begin{align}
	\hat{D}_X &= -\iota \mathcal{F} \hat{X} \mathcal{F}^{-1} \label{eq.sim1} \\
	\hat{D}_X &=  \iota \mathcal{F}^{-1} \hat{X} \mathcal{F} \label{eq.sim2}
\end{align}
$$
where $\mathcal{F}$ is the symmetric Fourier transform operator: 
$$
\begin{align}
	\mathcal{F}(x, x^\prime)f(x^\prime) \equiv 
	\frac{1}{\sqrt{2\pi}} 
	\int_\mathbb{R}dx^\prime~
	e^{-\iota xx^\prime} f(x^\prime) 
	\tag{$\forall f \in \mathcal{H}$}
\end{align}
$$

# The operator viewpoint
The elegant approach to the solution of Eq. \eqref{eq.sho} is in terms of the familiar raising and lowering operators. 
In this post I won't actually lay out all this formalism, but I'll describe a closely related insight enabled by the Fourier-conjugate ("similar") nature of $\hat{X}$ and $\hat{D}\_X$ as encoded in Eqs. \eqref{eq.sim1} and \eqref{eq.sim2}.
This insight serves the useful purpose of identifying the all the eigenfunctions of the harmonic oscillator in one shot, without the pain of solving the second-order differential equation in \eqref{eq.sho}.
The eigenvalues (permissible values of $E$) are linked in a consistent manner by the raising and lowering operators, but that is outside the scope of this post. 

I'll first do what all cool physicists like to do: make the differential equation more lightweight by setting the value of any arbitrary constant to $1$. 
By this I mean assuming that $\hbar = 1$, $m = 1$ and $\omega = 1$ in some suitable units.
The fundamental nature of the differential equation with all its symmetries becomes clearer this way, without distraction from the junk constants.
The constants can always be reintroduced later in their correct positions by dimensionally analyzing the final solution. 
In the light of this, Eq. \eqref{eq.sho} is expressed in terms of the reduced operator $\hat{Q}$:
$$
\begin{align}
	\underbrace{
		\frac{1}{2}\left(\hat{X}^2 - \hat{D}_X^2\right)
	}_{\hat{Q}} \Psi = E\psi
	\label{eq.sho_red}
\end{align}
$$

Since $\hat{Q}$ is made up of operators that are related to each other through the Fourier transform, it is worth looking at what $\hat{Q}$ itself looks like when Fourier-transformed. 
This is given by the following similarity transformation on $\hat{Q}$. 
I will also liberally introduce $\\mathcal{F}^{-1}\mathcal{F} = \mathbb{I}$ in between operators where convenient:
$$
\begin{align}
	\mathcal{F} \hat{Q} \mathcal{F}^{-1} 
	&= \frac{1}{2} \left[
			\left(\mathcal{F} \hat{X} \mathcal{F}^{-1}\right)
			\left(\mathcal{F} \hat{X} \mathcal{F}^{-1}\right) - 
			\left(\mathcal{F} \hat{D}_X \mathcal{F}^{-1}\right)
			\left(\mathcal{F} \hat{D}_X \mathcal{F}^{-1}\right)
		\right] \notag \\
	&= \frac{1}{2}\left[
			\left(\iota \hat{D}_X\right)^2 - \left(\iota \hat{X}\right)^2
		\right] \tag{From Eqs. \eqref{eq.sim1} and \eqref{eq.sim2}} \\
	&= \frac{1}{2} \left(\hat{X}^2 - \hat{D}_X^2\right) \notag \\
	&= \hat{Q} \label{eq.invariant}
\end{align}
$$

Lo and behold, $\hat{Q}$ is invariant under the Fourier transform!
This automatically tells us a lot about the solution of Eq. \eqref{eq.sho_red}.
In particular, $\hat{Q} \mathcal{F} = \mathcal{F}\hat{Q} \Rightarrow \left[\hat{Q}, \mathcal{F}\right] = 0$ and so $\hat{Q}$ shares a common basis of eigenfunctions with $\mathcal{F}$, which [we know are the Hermite functions](https://siddharth-maddali.github.io/mathematics/2020/03/15/Breaking-down-the-Fourier-transform.html) $\Psi_n(x) = e^{-\frac{x^2}{2}}H_n(x)$ (where the $H_n(x)$ are the Hermite polynomials).
I am, of course, ignoring the normalization constants that quantum mechanics usually requires for total probability to be unity. 
So in one stroke, we have used fundamental knowledge of the Fourier transform to divine the solutions $\Psi_n(x)$ of Eq. \eqref{eq.sho_red} without the hassle of actually solving it!
I think this is a pretty cool realization in itself.

# Conclusion and further ruminations
While I'd love to go into a detailed solution of the harmonic oscillator with the raising and lowering operators, there is an abundance of literature that already addresses this (the [Wikipedia page](https://en.wikipedia.org/wiki/Quantum_harmonic_oscillator) is a good place to start).
Instead, I'd rather idly speculate as to what other operators are invariant under the Fourier transform, _à la_ $\hat{Q}$ defined above. 
If I restrict myself to those that are only made up of $\hat{X}$ and $\hat{D}\_X$, then the one that jumps out right away is the commutator $\left[\hat{X}, \hat{D}\_X\right] = -\mathbb{I}$.
This is, however, trivial and boring.
The anticommutator $\left\\{\hat{X}, \hat{D}\_X\right\\} \equiv \hat{X}\hat{D}\_X + \hat{D}\_X\hat{X}$ flips sign under the Fourier transform; it's easy to show that  $\mathcal{F} \left\\{\hat{X}, \hat{D}\_X\right\\}\mathcal{F}^{-1} = -\left\\{\hat{X}, \hat{D}\_X\right\\}$. 
I suppose the squared anticommutator satisfies the invariance property, or any even power of the anticommutator for that matter.

Is there any interesting use case to the even-powered anticommutator of $\hat{X}$ and $\hat{D}\_X$?
Can you think of other operators that are Fourier-invariant? 



