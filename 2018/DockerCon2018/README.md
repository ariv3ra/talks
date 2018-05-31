# DockerCon 2018 - "Best Practices for Docker & CircleCI" or Alt Title "Lessons Learned Running Docker at Extreme Scale"
## Author: Angel Rivera
## Abstract: 
This talk takes the audience through a complete Continuous Integration\Continuous Deployment (CI\CD) process. CI\CD concepts will be demonstrated in real-time during a live coding demo of a simple application, unit test and a CircleCI configuration file. Continuos Deployment will also be demonstrated via the CircleCI configuration file. At the end of the demo the app will be live and functioning on a cloud server which will Digital Ocean. The goal is to show the crowd how to implement CI\CD into their development processes with ease and unravel the CI\CD mystery.

## Alt Abstract
The ascendance of Docker has helped bring about about a new focus on some software development values that are dear to our heart at CircleCI—consistency, automation, and continuity; that is, developing software within a consistent build environment, testing it in an automated fashion, and deploying it with a focus on continuous delivery of new code.

We released CircleCI 2.0 with these values in mind, placing Docker at the core of our Continuous Integration platform and allowing customers to build projects on CircleCI using any combination of Docker images as build environments.

CircleCI’s images for popular languages + frameworks have over 38M+ pulls on DockerHub. Docker images are an incredible asset for ensuring that your dev and production environments are mirrors. But, with every new technology comes added complexity and management overhead.

In this session, CircleCI CTO Rob Zuber will share some lessons learned in running Docker at scale, across thousands of customers, their language + technology choices, and their environments. With over 350,000 users and 10M+ jobs per month, we’ve seen up close how customers can succeed with Docker, and how to avoid potential issues.

## Outline
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
    - End of Dem\Questions

## Talk Script

### Slide 1
Hi my name is Angel Rivera & I'm a Developer Advocate for CircleCI. As a Developer Advocate my job is to directly engage the developers & the community.


## Tech Stacks
Here is a list of tech stacks being used:
- python 2.7.14
- unittests
- flask
- pyinstaller
- virtualenv
- docker
- CircleCI configuration
- Digital Ocean server




