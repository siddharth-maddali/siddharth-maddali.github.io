---
layout: new
title: Home | Siddharth Maddali's website
permalink: /
mathjax: true
---
{% include mathjax.html %}

<img align="right" style="width: 25%;" src="{{ site.url }}/images/MSDHeadshot.jpg">

# Hello! 

You've reached the personal website of Siddharth Maddali. 

I'm a computational scientist with {% assign current_year = site.time | date: '%Y' | plus: 0 %}{{ current_year | minus: 2017 }}+ years’ combined professional experience in X-ray and optical microscopy, Fourier/wave optics, acoustics and ultrasound, imaging algorithms, signal processing, high-performance computing, scientific software development and condensed matter physics. 
I also have R&amp;D experience in the semiconductor industry and stints at top US national laboratories. 
I am a professional with a Ph.D in physics and strong fundamentals in computation and mathematics. 
I'm passionate about computational innovation, particularly the physical sciences. 
I'm seeking to leverage new ways of solving problems in the physical world with AI and computation. 

You can read more about me [here]({{ site.url }}/about). 

<!-- <nav style="display: block;">
    <ul>
        {% for item in site.data.details %}
            <li><a href="{{ item.link }}">{{ item.name }}</a></li>
        {% endfor %}
    </ul>
</nav> -->

And finally, for no reason, here's a picture I took that I really like...
<figure>
    <img class="filled-width" src="{{ site.url }}/images/titleBanner.jpg" alt="McWay Cove, CA, USA" class="responsiveimage">
    <figcaption class="customcaption">McWay Falls, Big Sur, California (USA)</figcaption>
</figure>
