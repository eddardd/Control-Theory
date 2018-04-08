function [ A, B ] = linear_CartPend( M, m, L, I, bx, bth, sp)
%   This function is responsable to create the inverted
%   pendulum system. As parameters, we have:
%       - M: the cart's mass
%       - m: the pendulum mass
%       - L: the pole length
%       - I: the pole's inertia moment
%       - bx: track's friction coefficient
%       - bth: joint's friction coefficient
%       - sp: logic variable which indicates which setpoint we are treating
%  With those, the outputs are,
%       - A: the Jacobian matrix of the field f,
%       - B: the derivative of f with respect to the input

%% Handling bad arguments
if(sp ~= 0 && sp ~= 1)
    disp('Error: bad argument entry');
    A = 0;
    B = 0;
end

%% Constant terms
alpha = (I+m*L^2)*(M+m) - (m*L)^2;
g = 9.806;

%% Matrices
if(sp == 0)
    disp(sp)
    A = [0,                     1,                 0,                 0;
         0, -(m*(L^2)+I)*bx/alpha, ((m*L)^2)*g/alpha,    -m*L*bth/alpha;
         0,                     0,                 0,                 1;
         0,       -(m*L*bx)/alpha, (M+m)*m*g*L/alpha, -(M+m)*bth/alpha];

    B = [0;
         (m*L^2 + I)/alpha;
         0;
         m*L/alpha];
elseif(sp == 1)
    
    A = [0,                     1,                 0,                  0;
         0, -(m*(L^2)+I)*bx/alpha, -((m*L)^2)*g/alpha,     m*L*bth/alpha;
         0,                     0,                  0,                 1;
         0,        (m*L*bx)/alpha, -(M+m)*m*g*L/alpha, -(M+m)*bth/alpha];

    B = [0;
         (m*L^2 + I)/alpha;
         0;
         -m*L/alpha];
end
end

