%% Lecture 5, exercise 2, 09/05/2018
%  Eduardo Fernandes Montesuma
%  e-mail: edumontesuma@gmail.com

%% First system
omega_n = 4;
zeta = 3/8;

Tp = pi/(omega_n*sqrt(1-zeta^2))
OS = exp(-(zeta*pi)/(sqrt(1-zeta^2)))
Ts = 4/(zeta*omega_n)
Tr = 1.8/omega_n

%% Second system

omega_n = 0.2;
zeta = 0.05;

Tp = pi/(omega_n*sqrt(1-zeta^2))
OS = exp(-(zeta*pi)/(sqrt(1-zeta^2)))
Ts = 4/(zeta*omega_n)
Tr = 1.8/omega_n