# PI-in-the-Sky
Our first semester project
## Planning
### Goals
Launch a raspberry pi into the sky measuring and recording accelerometer data along it's flight and ensure that the pi is not broken when it lands.
### Method
Using a air canon we will launch a inclosed capsule which will hold a Raspberry Pi which will be the brain of the missle, accelerometer to both measure its momentum and to know when to trigger its parachute, battery to power the Pi and Acclerometer, and parachute to slow its decent once its triggered. We can additionaly attempt to mount the air canon on somesort of mount so that it's easier to handel
### Materials
1. PVC tubing both 2 inch and 3 inch
2. Valve
3. air compressor
5. ABS plastic
6. wires
7. small lithium ion battery
8. accelerometer
9. Raspberry PI
10. 1 large parachute or multiple smaller parachutes
11. fittings
12. PVC glue/sealent
13. PVC glue Primer
14. Nuts and Bolts
15. 3mm plastic sheets
16. springs
17. PCB single sided copper material
### Timeline
#### weeks 1-2: planning and modeling
-finish projectile model
-decide on launch method
-start design of launch method
-source springs and materials
#### weeks 3-6: construction testing/Coding
-find out how to determine tilt
-build launch method
-assemble projectile
-milling of PCB
#### week 7-10: troubleshooting and polishing
-ensure that projectile stays level in flight
-work out kinks in parachute deployment
#### week 11: Launch
-launch projectile get data and assemble it into more easily understood graph
### Inital Design
![Alt Text](https://github.com/pgunn78/PI-in-the-Sky/blob/master/IMG-0793.jpg)
### Solidworks Design
![Alt Text](https://github.com/pgunn78/PI-in-the-Sky/blob/master/Complete%20and%20Stabalized.PNG)
![Alt Text](https://github.com/pgunn78/PI-in-the-Sky/blob/master/complete%20section%20view.PNG)
#### Design Overview
The components such as the Pi and battery are mounted on the midplane and held in place by a cap which has a hole cut in the center to run wires to a servo. Which opens to release the parachute hatch to slow down the projectile once the projectile reaches its maximum altitude. to maintain a level flight fins are mounted on the side with small extrusions to keep them held out at an ideal position.
### Code 

## Problems and Solutions
### SolidWorks
While doing the solidworks design the most major problem that we encountered was material use, sizeing of the projectile, and space efficiency. due to it's cylindrical shape the space inside was not the easiest to utalize properly and effectlivly while still securing the components so that they won't shift during flight. To fix this we added a midplane to secure the components onto and added another plane above that to fix the midplane during flight. In addition to providing a place to mount components this also provides ease of construction allowing us to fix all components before sliding the midplane into the projectile where there is much less space to work. by designing the projectile in a fairly bullet like shape we made it difficult for the projectile to be printed without a large amount of support material to minimize the support material needed we added a steeper slope to the shape and went into the advanced settings of the print job turning the angle down where support material was needed and allowing us to print the entire part without any material needed for the central point. The last major problem that we encountered was the sizing of certain features such as the threads which were done using the solidworks thread tool (Creating suprisingly good results). this could still present a problem as the ABC plastic is maluable enough to where a impact from the side can seperate the two pieces. Which might cause the parachute compartment to breakup when deployed spilling the internals out mid-flight, but it seems like a fairly strong connection along the length of the projectile.
### Construction of the Projectile
the largest problems in the construction of the Projectile was the header hight, PCB milling and sourcing of materials. When milling our PCB we broke the job into two different sections due to class time limitations, cutting the traces or the copper wire paths first, and then drilling the holes for the headers. this caused the holes and traces to become slightly misaligned although it did not significantly damage the board or prevent it from working. the Headers on the PCB also prevented the midplane from sliding in due to their hight to fix this we bent the header pins down in the process breaking one of the copper traces which was repaired using a section of wire which was striped of insulations and soldered on. in addition to this the LED on the board was connected to the signal pin of the servo which we fixed by breaking the connection and soldering a wire from 3V to the broken connection

<img src="https://github.com/pgunn78/PI-in-the-Sky/blob/master/Header%20Problem.jpg" width="300" height="300"> <img src="https://github.com/pgunn78/PI-in-the-Sky/blob/master/Header%20Solution%20close.jpg" width="300" height="300"> <img src="https://github.com/pgunn78/PI-in-the-Sky/blob/master/Header%20Solution.jpg" width="300" height="300">
### Construction of the Launcher
We had a problem with both the seals on the launcher and the size of the launch tube. the first tube we chose to use being a 3inch tube whitch served to be two narrow to fit the projectile with the fin connections points prompting us to go up a tube size requiring a four inch diameter tube presenting a additional problem where air would escape past the sides of the projectile which was fixed by placing a end cap behind the projectile catching all the air. To fix the seals on the launcher we had to both retape the fittings using a large amount of plumbers tape and switch out the schrodinger valves we were using to another company which proved to be more reliable.
### Code
