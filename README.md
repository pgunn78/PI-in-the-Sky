# PI-in-the-Sky
Our first semester project
## Planning
### Goals
Launch a raspberry pi into the sky measuring and recording accelerometer data along it's flight and ensure that the pi is not broken when it lands.
### Method
Using a air canon we will launch a inclosed capsule which will hold a Raspberry Pi which will be the brain of the missle, accelerometer to both measure its momentum and to know when to trigger its parachute, battery to power the Pi and Acclerometer, and parachute to slow its decent once its triggered. We can additionaly attempt to mount the air canon on somesort of mount so that it's easier to handel
### Materials
#### 1 - 12
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
![Inital Design](https://drive.google.com/drive/folders/1iUdTW36hJb27-zo4ejjXmfmp4jNzXrf4)
### Solidworks Design
### Code 
we need to measure and record the data from our accelerometer as well as using the data to determine tilt of the projectile while ignoring acceleration 
https://www.nxp.com/docs/en/application-note/AN3107.pdf

## Problems and Construction
### SolidWorks
While doing the solidworks design the most major problem that we encountered was material use, sizeing of the projectile, and space efficiency. due to the cylindrical shape the space inside was not the easiest to utalize properly and effectlivly while still securing the components so that they wont shift during flight. To fix this we added a midplane to secure the components onto and added another plane above that to fix the midplane during flight. In addition to providing a place to mount components this also provides ease of construction allowing us to fix all components before sliding the midplane into the projectile where there is much less space to work. by designing the projectile in a fairly bullet like shape we made it difficult for the projectile to be printed without material 
