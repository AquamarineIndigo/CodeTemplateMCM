% Linear Programming:
% max f(x) = 3*x1 + 5*x2
% s.t.    x1 <= 4;
%         2*2 <= 12;
%         3*x1 + 2*x2 <= 18;
%         x1 >= 0;
%         x2 >= 0;
f = [3 5];
A = [1 0; 0 2; 3 2];
b = [4; 12; 18];
Aeq = [];
beq = [];
lb = [0; 0];
ub = [];
[x val] = linprog(-f, A, b, Aeq, beq, lb, ub)
% f'x such that:
%     A * x <= b;
%     Aeq * x = beq
%     lb <= x <= ub;

t = 0:0.1:20;
% z = 0:0.1:20;
% y = [t t] .* f';
y1 = 9 - 1.5.*(t);
% for z = 0:0.1:20
%     y2 = 0.2.*z - 0.6.*(t);
%     plot(t, y2);
% end
plot(t, y1);