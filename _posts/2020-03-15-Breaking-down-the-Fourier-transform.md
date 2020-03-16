---
layout: post
mathjax: true
author: Siddharth Maddali
categories: [research, signal processing, mathematics, quantum mechanics]
tags: [linear algebra, position, momentum, Fourier transform, Hermite functions]
---

{% include mathjax.html %}
An operator-based proof spectral decomposition of the Fourier transform in terms of the Hermite functions.

# Introduction
In my [last post]({{ site.url }}{% post_url 2020-02-15-position-and-momentum-are-similar-in-nature%}) from quite a while ago, I derived a couple of simple but useful similarity relations between the position and momentum operators through the Fourier transform.
These are: 
$$
\begin{align}
	\hat{D}_X &=  \iota \mathcal{F}^{-1} \hat{X} \mathcal{F} \label{eq.rel1} \\
	\hat{D}_X &= -\iota \mathcal{F} \hat{X} \mathcal{F}^{-1} \label{eq.rel2}
\end{align}
$$
Here, I use them to show how to determine the eigenvalues and a corresponding eigenbasis for the Fourier transform itself.
As I mentioned in my last post, this is a re-telling of a well-known proof that I feel illuminates the power of using the operator formulation as a nice alternative to doing tedious integrals by hand.

# The derivative generates translations
In the proof that follows, I need another very useful relation between the position and derivative operators, one that does not explicitly contain the Fourier transform. 
For simplicity, I continue to operate on well-behaved, smooth and square-integrable functions belonging to $\mathcal{H} = \left\\{f:\mathbb{R} \longrightarrow \mathbb{C} \left| \int_\mathbb{R} dx \left|f(x)\right|^2 < \infty\right.\right\\}$, as in the [previous post]({{ site.url }}{% post_url 2020-02-15-position-and-momentum-are-similar-in-nature%}).
This relation basically says that the derivatives of a function $f \in \mathcal{H}$ can be used to 'generate' functional values at different distances, or translations, from complete information of the function at a point $x_0$. 
By complete information, I mean the functional value and all its derivatives.
In group theory -speak, _the derivative is the generator of translations_: 
$$
\begin{align}
	\underbrace{e^{t\hat{D}_X}}_\text{translation}f(x_0) = f(x_0 + t) = \sum\limits_{n=0}^\infty \frac{t^n}{n!}\hat{D}_X^{(n)}f(x_0)
	\label{eq.groupgenerator}
\end{align}
$$

...which is also well known as the Taylor series expansion of $f(x)$ about $x_0$.

# Spectrum of the Fourier transform
So as with the [Wikipedia proof](https://en.wikipedia.org/wiki/Hermite_polynomials#Hermite_functions_as_eigenfunctions_of_the_Fourier_transform), I start with the generating function of the Hermite functions: 
$$
\begin{align}
	e^{-\frac{x^2}{2} + 2xt - t^2} 
	= e^{-\frac{1}{2} \left(x-2t\right)^2 + t^2} 
	= \sum\limits_{n=0}^\infty \left[e^{-\frac{x^2}{2}} H_n(x)\right]\frac{t^n}{n}
	\label{eq.generatingfn}
\end{align}
$$

Here $H_n(x)$ are the Hermite polynomials, which by themselves don't belong to $\mathcal{H}$ because, well, they're polynomials and therefore not bounded on $(-\infty, \infty)$.
So Eq. \eqref{eq.generatingfn} can be rewritten using Eq. \eqref{eq.groupgenerator} in linear operator form:
$$
\begin{align}
	\sum\limits_{n=0}^\infty \left[e^{-\frac{x^2}{2}} H_n(x)\right]\frac{t^n}{n} &= e^{-2t\hat{D}_X} e^{-\frac{x^2}{2}} e^{t^2}
\end{align}
$$

Taking the Fourier transform on both sides gives:
<br/>
$$
\begin{align}
	\sum\limits_{n=0}^\infty \mathcal{F} \left[e^{-\frac{x^2}{2}}H_n(x)\right] \frac{t^n}{n!} 
	&= \mathcal{F}e^{-2t\hat{D}_X} e^{-\frac{x^2}{2}} e^{t^2} \notag \\
	&= \left(\mathcal{F} e^{-2t\hat{D}_X} \mathcal{F}^{-1}\right) \left(\mathcal{F} e^{-\frac{x^2}{2}} \right) e^{t^2} \label{eq.breakup}
\end{align}
$$

...where we have used the associative property of the linear operators and the fact that $\mathcal{F}^{-1} \mathcal{F} = \mathbb{I}$, the identity operator.

The term in the first parenthesis on the RHS of Eq. \eqref{eq.breakup} may be analyzed as:
$$
\begin{align}
	\mathcal{F} e^{-2t\hat{D}_X} \mathcal{F}^{-1} &= \sum\limits_{n=0}^\infty \frac{(-2t)^n}{n!} \mathcal{F} \hat{D}_X^{(n)} \mathcal{F}^{-1} \notag \\
	&= \sum\limits_{n=0}^\infty \frac{(-2t)^n}{n!} \underbrace{
	\left(\mathcal{F} \hat{D}_X \mathcal{F}^{-1}\right)
	\left(\mathcal{F} \hat{D}_X \mathcal{F}^{-1}\right) 
	\ldots
	\left(\mathcal{F} \hat{D}_X \mathcal{F}^{-1}\right)
	}_{n\text{ times}} \notag \\
	&=  \sum\limits_{n=0}^\infty \frac{(-2t)^n}{n!} \left(\iota \hat{X}\right)^n \tag{from Eq. \eqref{eq.rel1}} \\
	&= e^{-\iota 2t \hat{X}} \notag
\end{align}	
$$
<br/>
while the term in the second parenthesis of Eq. \eqref{eq.breakup} is simply the well-known Fourier transform of the bell curve with a standard deviation of $1$:
$$
\begin{align}
	e^{-\frac{x^2}{2}} \underset{\mathcal{F}^{-1}}{\stackrel{\mathcal{F}}{\rightleftharpoons}}  e^{-\frac{k^2}{2}}
\end{align}
$$
<br/>
with the result that Eq. \eqref{eq.breakup} becomes: 
$$
\begin{align}
	\sum\limits_{n=0}^\infty \mathcal{F} \left[e^{-\frac{x^2}{2}}H_n(x)\right] \frac{t^n}{n!}
	&= \left(e^{-\iota 2t \hat{X}} e^{-\frac{k^2}{2}}\right) e^{t^2} \notag \\
	&= e^{-\iota 2t k -\frac{k^2}{2}} e^{t^2} \notag \\
	&= e^{-\frac{k^2}{2}}e^{-2(\iota t) k + (\iota t)^2} \notag \\
	&= e^{-\frac{k^2}{2}}  \sum\limits_{n=0}^\infty H_n(k) \frac{(\iota t)^n}{n!} \label{eq.final}
\end{align}
$$
<br/>
Comparing coefficients of $t^n$ on either side of Eq. \eqref{eq.final}, we get:
$$
\begin{align}
	\boxed{
		\mathcal{F}\left[e^{-\frac{x^2}{2}}H_n(x)\right] = \iota^n \left[e^{-\frac{k^2}{2}}H_n(k)\right]
	} \label{eq.result}
\end{align}
$$

_i.e._, the Hermite functions $e^{-\frac{x^2}{2}}H_n(x)$ form an eigenbasis of the Fourier transform operator $\mathcal{F}$ with corresponding eigenvalue $\iota^n = e^{\iota n \frac{\pi}{2}}$.

# Conclusion
Clearly, the eigenvalues $\left\\{e^{\iota n \frac{\pi}{2}}\left|n \in \mathbb{N}\right.\right\\} = \left\\{\iota, -1, -\iota, 1\right\\}$ are heavily degenerate, and therefore the Hermite functions are not a unique eigenbasis of $\mathcal{F}$.
In fact, an infinity of other orthogonal eigenbases can be generated by (i) taking any or all of the four eigen-subspaces spanned by the sets $S_p = \left\\{e^{-\frac{x^2}{2}}H_{4n+p}(x)\left|n \in \mathbb{N}\right.\right\\}$ for $p = 0, 1, 2, 3$ and (ii) performing a high-dimensional 'rotation' or a unitary transformation on the basis functions.
So one way to write the Fourier transform in terms of these eigenfunctions is:
$$
\begin{align}
	\mathcal{F}(k, x )f(x) \equiv \underbrace{
		\sum\limits_{n=0}^\infty 
		e^{\iota n\frac{\pi}{2}} 
		\int_\mathbb{R} dx~e^{-\frac{x^2 + k^2}{2}}H_n(k) H_n(x)
	}_\mathcal{F} f(x) \label{eq.springboard}
\end{align}
$$
<br/>
It turns out that the expression in Eq. \eqref{eq.springboard} (known as the spectral decomposition of $\mathcal{F}$) is a nice entry into the generalization into the fractional Fourier transform.
In particular: consider the linear operator (assuming it exists), whose eigenbasis is the Hermite functions like $\mathcal{F}$, but the corresponding eigenvalues are powers of not $e^{\iota n\frac{\pi}{2}}$, but the more general unit phasor $e^{\iota n\alpha}$ with $\alpha \in \mathbb{R}$.
The corresponding operator $$\mathcal{F}_\text{fr}$$ on the left hand side of Eq. \eqref{eq.springboard} would depend on the fractional angular parameter $\alpha$.
This _fractional-order Fourier transform_ (FrFT) may be defined by: 
$$
\begin{align}
	\mathcal{F}_\text{fr}(k, x\left|\alpha\right.)f(x) \equiv 
	\sum\limits_{n=0}^\infty 
	e^{\iota n\alpha} 
	\int_\mathbb{R} dx~e^{-\frac{x^2+k^2}{2}}H_n(k) H_n(x)
	f(x) \label{eq.frft}
\end{align}
$$
As I mentioned in my [introductory post]({{ site.url }}/{% post_url 2020-02-09-digging-into-the-fractional-fourier-transform %}), there is a nice, easy-to-read [1937 PNAS article by Condon](https://www.pnas.org/content/23/3/158) that I really like, which approaches the FrFT from a purely group-theoretic approach without referring to the spectral decomposition at all.
It nicely derives and parcels all the group-like and spectrum-like properties of this important integral transform in a systematic way.
For my part, I directly dive into the adaptation of the FrFT formalism in optics and coherent diffraction, in [my next post]({{ site.url }}/404post.html).
