%% Lecture 5, exercise 3, 09/05/2018
%  Eduardo Fernandes Montesuma
%  e-mail: edumontesuma@gmail.com

%% poles

A = [ 3, -4,  2;
     -2,  0,  1;
      4,  7, -5];
B = [-1;
     -2;
      3];

C = [1,7,1];

D = [0];

poles = eig(A)

%% Transfer function
[num,den] = ss2tf(A, B, C, D)

%% Symbolic system solving
syms s

L1 = inv(s*eye(3)-A);
L2 = L1*B;
L3 = C*L2;