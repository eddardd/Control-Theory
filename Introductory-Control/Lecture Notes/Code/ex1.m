%% Lecture 5, exercise 1, 09/05/2018
%  Eduardo Fernandes Montesuma
%  e-mail: edumontesuma@gmail.com

%% First system

S1 = tf([2],[1,2]);
figure(1);
title('Step response for the first system')
step(S1);
grid on;

%% Second system

S2 = tf([5],[1,9,18]);
figure(2);
title('Step response for the second system')
step(S2);
grid on;

%% Third system

S3 = tf([10,70],[1,30,200]);
figure(3);
title('Step response for the third system')
step(S3);
grid on;

%% Second system

S4 = tf([20],[1,6,144]);
figure(4);
title('Step response for the fourth system')
step(S4);
grid on;

%% Fifth system

S5 = tf([1,5],[1,20,100]);
figure(5);
title('Step response for the fifth system')
step(S5);
grid on;