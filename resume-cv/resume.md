---
layout: cv
title: Curriculum vitae
mathjax: true
---
{% include resume-nav-body.html %}
{% include mathjax.html %}


# <a name="resint"></a>Research interests <a href="#cv-menu" style="font-size:20px;">[Back to CV menu]</a>

1. Diffraction-based imaging of materials
	- High-energy diffraction microscopy
	- Coherent diffraction imaging
	- Ptychography
	- Computational imaging (signal processing, compressed sensing)
1. Condensed matter physics
	- Crystallography
	- Micro- and nano-structure characterization
	- Grain boundary geometry, topology and dynamics
	- Materials discovery with data science/machine learning
1.  High-performance computing and scientific software development (check out [my Github page](https://github.com/siddharth-maddali))

# <a name="workex"></a>Work experience <a href="#cv-menu" style="font-size:20px;">[Back to CV menu]</a>

| **POSITION** | **INSTITUTION/COMPANY** | **SPECIALIZATION** | **PERIOD** |
|:------------:|:-----------------------:|:------------------:|:----------:|
| Post-doctoral researcher | Argonne National Laboratory | Synchrotron radiation studies | Jan 2017 - present |
| Post-doctoral researcher (ORISE) | National Energy Technology Laboratory | Machine learning for materials discovery | May 2016 - Nov 2016 |
| Graduate research assistant | Carnegie Mellon University | Computational materials science | Aug 2012 - Feb 2016 |
| Graduate teaching assistant | Carnegie Mellon University | Physics for science undergraduates | 2009 - 2012 |
| Intern, dept. of physics | National University of Singapore | Audio signal processing | May 2008 |

# <a name="education"></a>Education <a href="#cv-menu" style="font-size:20px;">[Back to CV menu]</a>

| **INSTITUTION** | **DEGREE** | **MAJOR** | **PERIOD** | **PLACE** | **DESCRIPTION** |
|:---------------:|:----------:|:---------:|:----------:|:---------:|:---------------:|
| Carnegie Mellon University | **Doctor of Philosophy (Ph.D)** | Physics | 2010 - 2016 | Pittsburgh (USA) | Doctoral dissertation: [Computational mining of meso-scale physics from high-energy X-ray data sets](https://kilthub.cmu.edu/articles/Computational_Mining_of_Meso-Scale_Physics_From_High-Energy_X-Ray_Data_Sets/6715259/1) |
| Carnegie Mellon University | Master of Science (M.S) | Physics | 2009 - 2010 | Pittsburgh (USA) | |
| Indian Institute of Technology - Madras | Master of Science (M.Sc) | Physics | 2007 - 2009 | Chennai (India) | Masters' thesis: Vibrational modes of a solid sphere |
| Bangalore university | Bachelor of Science (B.Sc) | Physics | 2004 - 2007 | Bengaluru (India) | Triple major also included mathematics and electronics |

# <a name="pubs"></a>Publications <a href="#cv-menu" style="font-size:20px;">[Back to CV menu]</a>

{% include pubs.md %} <!-- Hey what do you know...this works in markdown. -->

# <a name="softproj"></a>Computational projects <a href="#cv-menu" style="font-size:20px;">[Back to CV menu]</a>

| **NAME** | **LANGUAGE(S)** | **HARDWARE** | **DESCRIPTION** |
|:--------:|:---------------:|:------------:|:---------------:|
|[H-Smooth](https://github.com/siddharth-maddali/HierarchicalSmooth)| Matlab, Python, C++ | CPU | A module for topology-faithful smoothing of grain interface meshes obtained from 3D images of polycrystals |
|[Fast Phasing Library (FPL)](https://bitbucket.org/ynashed/fpl/src/smaddali/)(contributor) | C++ | CPU, GPU | A phase retrieval program for Bragg coherent diffractive imaging (BCDI) data built on the [Arrayfire](https://arrayfire.com/) computational library |
| [Phaser](https://github.com/siddharth-maddali/Phaser) | Python, Tensorflow | CPU, GPU | A Python module for BCDI reconstructions |
| MicAlign | C++, MPI | CPU | A small, parallelized image registration program for 2D microstructure images obtained from high-energy diffraction microscopymeasurements |

# <a name="presentations"></a>Presentations <a href="#cv-menu" style="font-size:20px;">[Back to CV menu]</a>

| **WHEN** | **WHERE** | **CONFERENCE/PROGRAM** | **DESCRIPTION** |
|:--------:|:---------:|:----------------------:|:---------------:|
| March 2019 | San Antonio, TX | The Minerals, Metals & Materials Society (TMS) | Invited talk |
| July 2018 | Lemont, IL | Advanced Photon Source User Science Seminar | Talk |
| June 2018 | Port Jefferson, NY | Coherence: International Workshop on Phase Retrieval and Coherent Scattering | Talk |
| May 2018 | Pittsburgh, PA | Department of Physics Seminar Series, Carnegie Mellon University | Invited talk |
| April 2018 | Phoenix, AZ | Materials Research Society (MRS) | Talk |
| July-August 2017 | Easton, MA | Gordon X-ray Science Conference and Seminar | Poster + Discussion leader |
| November 2015 | Atlanta, GA | Department of Mathematics Seminar, Georgia Institute of Technology | Talk |
| March 2015 | Orlando, FL | The Minerals, Metals & Materials Society (TMS) | Poster | 
| October 2014 | Pittsburgh, PA | Materials Science & Technology (MS&T) | Talk |
| October 2012 | Pittsburgh, PA | Materials Science & Technology (MS&T) | Poster |

# <a name="workshops"></a>Workshops attended <a href="#cv-menu" style="font-size:20px;">[Back to CV menu]</a>

1. Multi-physics Object-Oriented Simulation Environment ([MOOSE](https://mooseframework.org/)) - Orlando, FL
1. Center for Causal Discovery ([CCD](https://www.ccd.pitt.edu/)) - Pittsburgh, PA
1. Machine Learning for Materials Research ([MLMR](https://www.nanocenter.umd.edu/events/mlmr/)) - College Park, MD

# <a name="professional"></a>Professional activity <a href="#cv-menu" style="font-size:20px;">[Back to CV menu]</a>

1. **Peer review**
	* _Philosophical Magazine_
	* _Computational Materials Science_


1. **Society membership**
	* American Physical Society (APS)
	* Materials Research Society (MRS)
	* The Minerals, Metals & Materials Society (TMS)

<!--
<script>
	window.onscroll = function() {myFunction()};
	
	var navbar = document.getElementById("navbar");
	var sticky = navbar.offsetTop;
	
	function myFunction() {
		if (window.pageYOffset >= sticky) {
			navbar.classList.add("sticky")
		} else {
			navbar.classList.remove("sticky");
		}
	}
</script>
-->
