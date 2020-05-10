---
layout: post
mathjax: true
author: Siddharth Maddali
categories: [Mathematics]
tags: [linear algebra, quantum mechanics, Fourier transform]
---

{% include mathjax.html %}
In my opinion an interesting relationship between the position and derivative operators X̂ and D̂ₓ, through a similarity transformation with the Fourier transform operator.

# Introduction

The similarity transformation is fundamental to the quantitative understanding of many things in physics. 
The most relatable, everyday instance is the manner in which "matrix-like" physical quantities (rank-2 tensors) transform under change of perspective of an observer.
In other words, how these quantities change under rotations (passive or active).
If we pick an arbitrary rotation $R$ from the group of rotations (known in mathematics as the **s**pecial **o**rthogonal group of order **3**, or $SO(3)$), then every student of physics is familiar with what the components of any vector $\boldsymbol{v}$ will look like when this rotation is applied to it: 
$$
\begin{align}
	\boldsymbol{v} \longrightarrow R\boldsymbol{v}
\end{align}
$$

or if we, the observer, reoriented ourselves by the rotation $R$: 
$$
\begin{align}
	\boldsymbol{v} \longrightarrow R^{-1} \boldsymbol{v}
\end{align}
$$

What is less obvious is what happens to rotationally dependent physical quantities with one level of complexity higher than vectors like $\boldsymbol{v}$ ("rank-1 tensors"). 
An example of such a "rank-2 tensor" is the intertia $I_{ij}$, the quantity that is usually distilled down to the scalar _moment of inertia_ in high-school physics textbooks.
$I_{ij}$ has an inherently convenient representation as a $3 \times 3$ matrix, unlike the column-vector $\boldsymbol{v}$. 
How then, does this quantity look under a rotation $R$, or re-orientation of our perspective by $R$?
Like this, respectively: 
$$
\begin{align}
	I &\longrightarrow R I R^{-1} \\
	I &\longrightarrow R^{-1} I R 
\end{align}
$$

Any transformation of the type shown above involving a matrix and its inverse (in this case, $R$) is a [_**similarity transformation**_](https://en.wikipedia.org/wiki/Matrix_similarity).
The old and new representations of $I$ are said to be similar to each other under the transformation $R$.
In this post, I show that the position and derivative operators $\hat{X}$ and $\hat{D}_X$ (from signal processing and quantum mechanics) are also similar, under the Fourier transform.

This fact has interesting implications for the Fourier transform, namely in indicating an important way to examine its entrails ("spectral decomposition"). 
In later posts I will be using this decomposition as a starting point for jumping from the Fourier transform, to the more generalized and interesting fractional-order Fourier transform (FrFT), which forms the theoretical basis of most of my current and future work.

## The space of interest

Before proceeding, it's worth clarifying the set of operands to which the operators of interest are applicable. 
For the purposes of this post, these will be single-variable functions that have a finite $\ell_2$-norm.
By this, I mean that the operators act upon the elements of the "Hilbert space" $\mathcal{H}$ of well-behaved, square-integrable functions of one variable: $\mathcal{H} = \left\\{ f:\mathbb{R} \rightarrow \mathbb{C} \left| \int_\mathbb{R} dx \left|f(x)\right|^2 < \infty \right.\right\\}$.
From a signal-processing perspective, al element of this set represents a signal of finite energy, and in quantum mechanics a wave function (modulo normalization) with a steady-state probability density function.

The linear operators $\hat{X}$ and $\hat{D}_X$ denoting position and derivative are quite simply defined by: 
$$
\begin{align}
	\hat{X}(x, x^\prime)f(x^\prime) &= x f(x) \\
	\hat{D}_X(x, x^\prime)f(x^\prime) &= \left.\frac{df}{dx^\prime} \right|_{x^\prime = x}
\end{align}
$$

An expression like $\hat{X}(x, x^\prime) f(x^\prime)$ is understood to be integrated over the repeated variable $x^\prime$ in order to obtain a final expression in terms of the un-repeated variable $x$. 
This is completely analogous to the [Einstein summation convention](https://en.wikipedia.org/wiki/Einstein_notation) for expressions such as $\hat{X}_{ij}f_j$, in which a summation is implied over the repeated index $j$ to leave an expression in $i$.
Wherever it's unambiguous, I'll be dropping these indices in my notation altogether; this makes for a more compactified form of the operator formalism, which in my opinion is a more elegant and illuminating way to do certain difficult mathematical proofs.
Undergrad students of quantum mechanics have already had a taste of this when they solved the Schrodinger equation for the one-dimensional harmonic oscillator using raising and lowering operators $\hat{a}$ and $\hat{a}^\dagger$ instead of directly integrating it.

For this post I'll skip mentioning all the underlying assumptions and make my life simpler by assuming that I'm dealing only with those linear operators that map back to elements of $\mathcal{H}$, in other words, $\left\\{ \hat{O} \left| \hat{O}(x, x^\prime)f(x^\prime) \in \mathcal{H}~~\forall f \in \mathcal{H}\right.\right\\}$.
The Fourier transform, of course, automatically satisfies this property owing to [Parseval's theorem](https://en.wikipedia.org/wiki/Parseval%27s_theorem).

Taking all this into account, $\hat{X}$ and $\hat{D}_X$ themselves may be represented quite trivially as integral operators by:
$$
\begin{align}
	\hat{X}f &= \underbrace{\int_\mathbb{R}dx^\prime~\delta(x^\prime - x) x^\prime}_{\hat{X}(x, x^\prime)}f(x^\prime) \\
	\hat{D}_X f &= \underbrace{\int_\mathbb{R}dx^\prime~\delta(x^\prime - x) \frac{d}{dx^\prime} }_{\hat{D}(x,x^\prime)} f(x^\prime)
\end{align}
$$
where $\delta(x^\prime - x)$ is the Dirac delta function.

As an aside: the derivative operator, undergraduate quantum mechanics tells us, is essentially the momentum operator $\hat{P}$ in the one-dimensional Schrodinger equation: 
$$
\hat{P} = -\iota \hbar \frac{\partial}{\partial x} = -\iota \hbar \hat{D}_X \notag
$$
So while the title of this post talks of the momentum operator, I refer to both the derivative and momentum operator as one and the same.
This entire analysis can be re-done by re-scaling the operators _i.e_, absorbing constants into them, with the final notation being a personal preference.

When I'm doing this kind of physics I find myself liking the following symmetric form of the Fourier transform of a function  $f \in \mathcal{H}$ given by: 
$$
\begin{align}
	\tilde{f}(k) &= \underbrace{\frac{1}{\sqrt{2\pi}}\int_\mathbb{R} dx~ e^{-\iota kx}}_{\mathcal{F}(k,x)} f(x) = \mathcal{F}(k,x) f(x) \\
	f(x) &= \underbrace{\frac{1}{\sqrt{2\pi}}\int_\mathbb{R}dk~e^{\iota kx}}_{\mathcal{F}^{-1}(x,k)} \tilde{f}(k) = \mathcal{F}^{-1}(x,k) \tilde{f}(k)
	\end{align}
$$

and will stick to it. 
Here $x,k \in \mathbb{R}$ are variables denoting Fourier-conjugate spaces.
As a side note, it turns out that in x-ray Bragg diffraction imaging (my day job), another symmetric form of the Fourier transform is more appropriate for the diffraction geometry of the experiment than this one.
It uses the conjugate variable pair $x, \frac{k}{2\pi} \in \mathbb{R}$ instead of the above.
See [this reference](https://doi.org/10.1107/S1600576720001363) for more information on this.
And so without further ado...

## Similarity relation 1: $\hat{D}_X =  -\iota \mathcal{F} \hat{X} \mathcal{F}^{-1}$

### _Proof_: 

With the above notation in place, we have $\forall f \in \mathcal{H}\ldots$
$$
\begin{align}
    \mathcal{F} \hat{X} f &= \frac{1}{\sqrt{2\pi}}\int_\mathbb{R}dx e^{-\iota kx}xf(x) \notag \\
    &= \iota \frac{d}{dk} \frac{1}{\sqrt{2\pi}}\int_\mathbb{R}dx~e^{-\iota kx}f(x) \notag \\
    &= \iota \hat{D}_X \mathcal{F} f \notag \\
    \Longrightarrow &\boxed{\hat{D}_X = -\iota \mathcal{F} \hat{X} \mathcal{F}^{-1}} \label{eq.rel1}
\end{align}
$$

## Similarity relation 2: $\hat{D}_X = \iota \mathcal{F}^{-1} \hat{X} \mathcal{F}$

### _Proof_: 
We again have $\forall \tilde{f} \in \mathcal{H} \ldots$
$$
\begin{align}
    \hat{D}_X \mathcal{F}^{-1} \tilde{f} &= \frac{d}{dx} \frac{1}{\sqrt{2\pi}} \int_\mathbb{R}dk~ e^{\iota kx}\tilde{f}(k) \notag \\
    &= \iota \frac{1}{\sqrt{2\pi}} \int_\mathbb{R}dk~e^{\iota kx}k \tilde{f}(k) \notag \\
    &= \iota \mathcal{F}^{-1} \hat{X} \tilde{f} \notag \\
    \Longrightarrow &\boxed{\hat{D}_X = \iota \mathcal{F}^{-1} \hat{X} \mathcal{F}} \label{eq.rel2}
\end{align}
$$

## Conclusion
One may think of the equations \eqref{eq.rel1} and \eqref{eq.rel2} as describing the 'rotation' of the position operator in some high- and infinite-dimensional space to give the derivative operator.
The primary difference is the presence of the pesky imaginary factor $\iota$, which is missing in true $SO(3)$-based rotations.

It turns out that the position-derivative similarity relations offer a neat way to break down tedious Fourier transform integrals, by expressing them in terms of simpler known integrals.
This can be exploited to interesting effect when spectrally decomposing the Fourier transform operator, and determining its eigenvalues and eigenvectors.
While the proof of this is actually straightforward and is [available on Wikipedia](https://en.wikipedia.org/wiki/Hermite_polynomials#Hermite_functions_as_eigenfunctions_of_the_Fourier_transform), I rather like the fact that the same thing can be done by applying the above relations to matrix-exponential operators.
I show this in my [next post]({{ site.url }}{% post_url 2020-03-15-Breaking-down-the-Fourier-transform %}).

