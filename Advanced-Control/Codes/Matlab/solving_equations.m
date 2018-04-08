%% Solving the systems
%     for veryfing answers purposes

syms M m L g I bx bth F x dx ddx th dth ddth s

%% Equations 1.15-1.17

A1 = [M+m               , -m*L*cos(th);
          -m*L*cos(th),     (m*L^2 + I)];

A2 = [F + m*L*dth*sin(th) - bx*dx, -m*L*cos(th)
                 m*g*L*sin(th) - bth*dth,      (m*L^2 + I)];
             
A3 = [               M+m, F + m*L*dth*sin(th) - bx*dx;
          -m*L*cos(th), m*g*L*sin(th) - bth*dth];
      
det(A1)
det(A2)
det(A3)

%% Convert state space to transfer function

alpha = (I+m*L^2)*(M+m) - (m*L)^2;

a = -(m*L^2 + I)*bx/alpha;
b = (g*(m*L)^2)/alpha;
c = -m*L*bth/alpha;
d = -m*L*bx/alpha;
e = (M+m)*m*g*L/alpha;
f = -(M+m)*bth/alpha;
g = (m*L^2 + I)/alpha;
h = m*L/alpha;

A = [0, 1, 0, 0; 0, a, b, c; 0, 0, 0, 1; 0, d, e, f];
B = [0; (m*L^2 + I)/alpha; 0; m*L/alpha];

det(s*eye(4) - A)