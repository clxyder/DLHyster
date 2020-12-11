# DLHyster
I am working on a research project to create a deep learning model that outputs a float between -1 to 1 indicating a state of charge, with 4 input. The inputs are either positive or negative, indicating a charge or discharge cycle respectively. The goal is to feed the neural network enough data to accurately predict the state of charge with given inputs.
For example:
-1.0713518066664 -0.24087 0.00000 0.00000 -0.88103

(-)  ->  (-)  ->  (0)  ->  (0) == s.o.c

\
 \ _ _
 
 A small representation of what the cycle would look like.
