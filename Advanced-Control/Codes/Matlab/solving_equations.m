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

%% Equations 1.50 and 1.51
% Values for theta = 0
alpha = (I+m*L^2)*(M+m) - (m*L)^2;

% f2 derivatives
a = -(m*L^2 + I)*bx/alpha; % df2/dx2
b = -(g*(m*L)^2)/alpha;    % df2/dx3
c =  m*L*bth/alpha;        % df4/dx4
% f4 derivatives
d =  m*L*bx/alpha;         % df4/dx2
e = -(M+m)*m*g*L/alpha;    % df4/dx3
f = -(M+m)*bth/alpha;      % df4/dx4
% input derivatives
g = (m*L^2 + I)/alpha;     % df2/du
h = -m*L/alpha;            % df4/du

A = [0, 1, 0, 0; 0, a, b, c; 0, 0, 0, 1; 0, d, e, f];
B = [0; (m*L^2 + I)/alpha; 0; m*L/alpha];

denominator = det(s*eye(4) - A);
numerator1  = B(2)*det([-1, 0, 0; 0, s, -1; -d, -e, s-f])...
              - B(4)*det([-1, 0, 0; s-a, -b, -c; 0, s, -1]);
numerator2  = B(2)*det([s, -1, 0; 0, 0, -1; 0, -d, s-f])...
              - B(4)*det([s, -1, 0; 0, s-a, -c; 0, 0, -1]);