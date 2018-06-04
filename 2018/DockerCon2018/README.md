# DockerCon 2018 - "Best Practices for Docker & CircleCI" or Alt Title "Lessons Learned Running Docker at Extreme Scale"
## Author: Angel Rivera
## Abstract: 
This talk takes the audience through a complete Continuous Integration\Continuous Deployment (CI\CD) process. CI\CD concepts will be demonstrated in real-time during a live coding demo of a simple application, unit test and a CircleCI configuration file. Continuos Deployment will also be demonstrated via the CircleCI configuration file. At the end of the demo the app will be live and functioning on a cloud server which will Digital Ocean. The goal is to show the crowd how to implement CI\CD into their development processes with ease and unravel the CI\CD mystery.

## Alt Abstract
The ascendance of Docker has helped bring about about a new focus on some software development values that are dear to our heart at CircleCI—consistency, automation, and continuity; that is, developing software within a consistent build environment, testing it in an automated fashion, and deploying it with a focus on continuous delivery of new code.

We released CircleCI 2.0 with these values in mind, placing Docker at the core of our Continuous Integration platform and allowing customers to build projects on CircleCI using any combination of Docker images as build environments.

CircleCI’s images for popular languages + frameworks have over 38M+ pulls on DockerHub. Docker images are an incredible asset for ensuring that your dev and production environments are mirrors. But, with every new technology comes added complexity and management overhead.

In this session, CircleCI CTO Rob Zuber will share some lessons learned in running Docker at scale, across thousands of customers, their language + technology choices, and their environments. With over 350,000 users and 10M+ jobs per month, we’ve seen up close how customers can succeed with Docker, and how to avoid potential issues.

## Talk Outline
- My Introduction
    - Who, What, Where
- CircleCI Introduction
    - What, Where, When & Why
- Brief history of v1.0 tech stack
    - How did it used to be?
- Intro into 2.0
    - What changed from 1.0
- Why Docker?
    - Decision factors
- Lessons Learned
    - Bad parts
    - Good parts
- Demo
    - Live code Python App
    - Live code python unittest
    - Live code v2.0 CircleCI config
        - add ssh keys
        - run tests
        - Wire up a deploy to Digital Ocean Server via Docker
    - Push "broken: code to repo cause build failure
        - Fix code
    - Push Fixed Code to repo
    - Show CircleCI build go Green
    - Have Audience go to hello.dpunks.org to see the app
    - End of Demos\Questions

## Talk Script

### Slide: My Introduction
Welcome everyone. Some of you are probably expecting Rob Zuber CircleCi's awesome CTO but unfortunately he is unable to present so I'll be subbing for him today and I'm really EXCITED to be speaking to all of you.

So my name is Angel Rivera & I'm a Developer Advocate for CircleCI. As a Developer Advocate my job is to directly engage developers... & you the community. 
Before we begin I want you all to know that this is my 1st conference talk as a CircleCI Developer Advocate and I intend to make it legit.

I know this talk is billed as "Lessons Learned Running Docker at Extreme Scale" I've decided to switch things up today and go a bit lighter on the slides & heavier on a demo. I want to keep you all engaged & demonstrate what Continuos Integration\Continuous Deployment is and how to implement it using CircleCI. So my apologies up front for switching it up on you.

#### Slide: What is CircleCI
CircleCI is a Continuos Integration Continuos Delivery\Deployment platform that enables developers to rapidly release quality code by automating the build, test, and delivery process.

Quick show of hands how many of you are familiar with CI\CD?

### Slide: CircleCI Version 1.0 - Pre Docker
Version 1 of the platform was launched in 2011 before the Containerization Boom so it executes builds on dedicated VMs using a selection of Ubuntu Linux and for mobile builds Ubuntu w/ Android SDK & OSX for XCode code bases. v1.0 is an awesome innovation but as our business processes evolve & new technologies emerge so must our platform. As usage increased customers required flexibility in their pipelines.

### Slides: CircleCI Version 2.0
CircleCI addressed their customers needs in the form of v.20. I wasn't with the company during the v2.0 design but the team shared early v2.0 internal docs with me which illustrated their design & technology considerations. The teams thoroughly debated decisions such as whether or not to roll their own stack vs incorporating existing off the shelf solutions where appropriate. A topic that stood out to me was around choosing a containerization stack for the 

### Slide: CircleCI Stats
CircleCI processes:
- 12 Million+ builds per month
- 500K+ avg per weekday

Our users are crushing it in regards to CI\CD.  Lots of quality code being written.


## Tech Stacksß
Here is a list of tech stacks being used:
- python 2.7.14
- unittests
- flask
- pyinstaller
- virtualenv
- docker
- CircleCI configuration
- Digital Ocean server




