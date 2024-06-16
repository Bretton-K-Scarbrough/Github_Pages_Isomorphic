---
title: How to Capture an Echo (1/2)
description: An exploration of how Green's functions can be utilized to capture a room's echo and put it onto an audio signal. 
date: '2024-3-??'
categories: 
    - Math 
    - Physics
    - Differential Equations
    - DSP
published: true
---

<svelte:head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.13.13/dist/katex.min.css" integrity="sha384-RZU/ijkSsFbcmivfdRBQDtwuwVqK7GMOw6IMvKyeWL2K5UAlyp6WonmB8m7Jd0Hn" crossorigin="anonymous">
</svelte:head>
<br>

In this series of posts, we are going to explore how it is possible to record the reverb of a room and then put it onto an audio signal. This first post will explore the mathematics behind such a process and the second post will explore implementing this process in Python.
<br>


## Brief Introduction to Green's Functions
Large structures, such as theaters, arenas, and churches are created with the specific intention to create pleasant acoustics. One of the pleasant acoustic traits is reverb. In music, reverb, to varying degrees, is added to audio tracks for its pleasant sound. The likelihood that you have access such a location while recording is slim to none. However, there exists a solution to this problem. A popular digital signal processing technique is that of an impulse response reverb. An impulse response reverb, is a reverb effect utilized in audio production to record the reverb or "echo" of a room, to later be mixed with an audio signal. This allows for the grandiose acoustics of a concert hall to be put on vocals that were recording in a closet. Such an effect can be constructed from a mathematical object called a "**Green's Function**". Such a function can be understood as the *inverse* of a differential operator. We will now quickly review operational inverses and their implications.


#### Multiplication and Division as Inverses
Most people are familiar with what an inverse operation is. It is an operation that "undoes" whatever the original operation did. An elementary example is multiplication and division. 
Given $a, b$ are real numbers and $a,b \ne 0$, we can notate multiplication as:
$$
ax = b
$$

Unsurprisingly, one can solve for $x$ by dividing both sides by $a$.
$$
x = \frac{b}{a}
$$

However an important fact that we normally overlook is the fact that we are hiding a step in the operations that we just performed. A multiplication by $1$. 

$$
 \frac{a}{a} \cdot x = \frac{b}{a}\equiv 1\cdot x = \frac{b}{a} 
$$
This fact is unremarkable when looking at multiplication, nonetheless, it becomes more interesting in context. 

#### Inverse Matrices 
Inverses come in many shapes and sizes, usually more interesting than just  scalar division. Another example that may come to mind is that of an *inverse matrix*. We say that a matrix $A^{-1}$ is the inverse of $A$ if the following is true: 

$$
A^{-1}A = I 
$$
where $I$ is the *identity matrix*. As highlighted before, when a operators inverse acts upon itself it should yield "$1$". Yet, we are describing matrices, therefore, a single number does not describe the system accurately. The solution to characterize the problem is identity matrix. The identity matrix can be described as $1$ in the main diagonal and zero everywhere else. 

$$
I = \begin{bmatrix}
1 & 0 & 0 & \cdots & 0 \\ 
0 & 1 & 0 & \cdots & 0\\
0 & 0 & 1 & \cdots &0 \\ 
\vdots & & &\ddots &\\ 
0 & 0 &0 &\cdots & 1
\end{bmatrix}
$$

If we know $A^{-1}$, then we know then we know how to solve the equation: 
$$
A \hat{x} = \hat{b}
$$
where $A$ is a matrix and $\hat{x}$, $\hat{b}$ are vectors. We can solve this problem with the inverse as such:
$$
\begin{align*}
A^{-1} A\hat{x} &= A^{-1}\hat{b}\\
I A\hat{x} &= A^{-1}\hat{b} \\
\hat{x} &= A^{-1}\hat{b}
\end{align*}
$$

#### Green's Functions
Given a linear differential equation, you can always rewrite the equation such that you can identify a linear differential operator.

$$
Lu = f
$$
Let's look at the wave equation for an example.

$$
\begin{align*}
u_{tt} - c^2 u_{xx} &= f(x,t) \\
\underbrace{(\partial_{tt} - c^2\partial_{xx})}_{L}u &= f(x,t)
\end{align*}
$$

Therefore, all linear partial differential equations can be put into the form: 
Hopefully you are starting to see a pattern. A logical question when seeing linear equations of that form is "can I solve this with an **inverse operator?**" Unsurprisingly, you can! But what does an inverse linear differential operator look like? Well the inverse of differentiation is integration, therefore, it makes sense to look for a linear integral operator. 
<br>

Something to note about each of the different domains that we have been working in is the fact that they have had different operations that had similar structure. For example, in the context of just numbers, we were able to use normal multiplication. However, this was not sufficient for matrix operations, and we needed matrix multiplication instead of classical multiplication. Therefore we may expect some new kind of operation to describe differential operators and their inverses. 
This new operation that we are looking for ends up being something called a convolution. Something that we should also consider is the fact that we needed something slightly different than "$1$" for matrices. We will need something slightly different for differential equations as well.
<br>

A convolution operation, often shortened to $*$, between $x$ and $h$ is defined as: 
$$
x(t) * h(t) = \int_{-\infty}^{\infty}x(\tau)h(t-\tau) d\tau
$$

Convolutions look a little intimidating at first but actually appreciating what they look like helps dramatically. Below is an animation of what the convolution of two functions looks like. 
<br>

![Svelte](/How_to_Capture_an_Echo/Convolution.gif)
<br>

Convolution is not the primary focus of this discussion and I plan on discussing it more in later posts. However, if you are more interested in convolutions I suggest you watch this [video](https://youtu.be/KuXjwB4LzSA?si=BqEidoXjih6PHkkv) by the one and only 3Blue1Brown.
<br>

We say that a linear differential operator $G$ is the inverse of $L$ if 
$$
LG = \delta
$$

Where $\delta$ is a *delta function*. Delta functions are our new mathematical object which takes the place of "$1$". It has some important properties that may seem unfamiliar at first, but they make more sense when we lean on our intuition from algebra and linear algebra.  

<!-- It is likely you have picked up on a pattern. When we are given an equations of the form  -->
<!-- $$ -->
<!-- Ax = b -->
<!-- $$ -->

