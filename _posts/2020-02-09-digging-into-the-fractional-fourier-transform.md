---
layout: new
mathjax: true
author: Siddharth Maddali
categories: [Research]
tags: [x-ray, microscopy]
---

{% include mathjax.html %}
My sporadic thoughts on the fascinating fractional Fourier transform, in the course of my work developing new x-ray imaging methods.

# Coherent dark-field x-ray microscopy - a new direction

As my life as a post-postdoc researcher branches out in more exciting directions, one of the things I'm trying to get off the ground at one of the APS beamlines is a developmental project for implementing dark-field microscopy using coherent x-ray illumination.
In contrast to what I do most of the time (coherent diffraction microscopy or CDI), this imaging technique does not require sophisticated data inversion algorithms like phase retrieval in order to obtain a real-space image: the material system is directly imaged on a screen with the help of strategically-placed x-ray lenses in the path of the diffracted beam.
While this has already seen some success with incoherent x-rays (see [here](https://www.nature.com/articles/ncomms7098) and [here](https://www.cambridge.org/core/journals/mrs-bulletin/article/multiscale-3d-characterization-with-darkfield-xray-microscopy/4D92CCF54C76AC30AAC21EF890F59F2E/share/15351d4b36cabdf8d10b49d19dc6612b91ece6f3)), the idea is that exploiting coherent illumination might allow us to explore the continuum in between the near- and far-field x-ray diffraction regimes (Fresnel and Fraunhofer diffraction) as a possibly new way to characterize the physics of materials, provided we can correctly model the diffracted wave field at different distances from the scatterer.

And so the overarching problem becomes to robustly model measured the diffraction pattern from a coherently illuminated scatterer (say, a nanocrystal like in Bragg CDI), with a complicated lens system placed anywhere in the path of the diffracted beam.
Now this is clearly a tall order, and the germs of different ideas for our original dark-field x-ray microscopy project are still being formed as we speak.
However, the natural starting point seems to be some generalization of the relatively-near-field Fresnel propagator in free space.
This is where the fractional Fourier transform (FrFT) comes in; it turns out that it is precisely the generalized propagator that we are looking for.
I have been studying this generalization of the Fourier transform for a while now. 
I'm simultaneously fascinated by the underlying rich mathematical structure, as well as its ubiquity in terms of practical applications (imaging, quantum mechanics, etc.). 
In college I was drilled pretty hard in mathematical topics that are usually on extreme ends of the practical applications spectrum, from abstract group theory to theoretical physics and signal processing, but never in something that spans all this cogently.
In FrFTs I find a subject that simultaneously tickles all those parts of my brain all over again. 
The next few blog posts will be my meanderings through the landscape of FrFTs (by no means thorough or complete), partly in chronological order of my literature survey and partly informed by what I needed done at work.

I will add that for the interested group theorist, there is a nice [1937 introductory article](https://www.pnas.org/content/23/3/158) by Condon in PNAS that I feel can be read at the undergrad level.
Further, the direct connection to the free-space Fresnel propagator is established in [this article here](https://www.osapublishing.org/ol/abstract.cfm?uri=ol-19-18-1388), and its connection to other applications is drawn in other works like [this one](https://www.sciencedirect.com/science/article/pii/S0165168410003956).
Being a physicist, I rather like the approach to FrFTs starting from Fourier transforms, within [the context of quantum mechanics](https://academic.oup.com/imamat/article-abstract/25/3/241/711477?redirectedFrom=fulltext).

Next post coming soon...!
