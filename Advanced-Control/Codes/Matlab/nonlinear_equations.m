function [dx] = nonlinear_equations(t,x)
%  This function creates a model corresponding to the inverted pendulum sys
%  tem. It receaves as inputs:
%       - t: time variable
%       - x: state vector, composed by displacement, velocity, angle and
%            angular velocity.

%% Constants
M   = 4.800;    % Cart mass
m   = 0.356;    % Pendulum mass
L   = 0.560;    % Pole length
bth = 0.035;    % Joint Friction
bx  = 4.900;    % Cart Friction
I   = 0.006;    % Pole inertia moment
g   = 9.806;    % Gravitational acceleration

%% Equations

F = 1; % Step response
% Remark: you can change F to be an arbitrary input of your wish.

dx = zeros(4,1);

dx(1) = x(2);
dx(2) = ((m*L^2 + I)*(F - m * L * (x(4)^2) * sin(x(3)) - bx * x(2)) - ...
         m * L * cos(x(3)) * (m * g * L * sin(x(3)) - bx * x(2)))...
         /((M+m)*(m*L^2 + I) - (m^2)*(L^2)*(cos(x(3)))^2);
dx(3) = x(4);
dx(4) = ((M+m)*(m*g*L*sin(x(3)) - bth * x(4)) +...
         m*L*cos(x(3))*(F - m*L*(x(3)^2)*sin(x(3)) - bx*x(2)))...
         /((M+m)*(m*L^2 + I) - (m^2)*(L^2)*(cos(x(3)))^2);
end

