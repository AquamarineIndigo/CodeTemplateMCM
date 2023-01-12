% visualize
% https://www.mathworks.com/products/matlab/plot-gallery.html
% https://www.mathworks.com/products/matlab/live-script-gallery.html

x = linspace(0, 2, 2000);
y = exp(x.^0.5) ./ log(x + 1) .* sin(x);
plot(x, y, 'b--');
title('Name of the Graph');
xlabel('x');
ylabel('y');
legend('f(x)');
grid on;
grid minor;