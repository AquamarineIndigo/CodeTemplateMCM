function createfigure(X1, Y1)
%CREATEFIGURE(X1, Y1)
%  X1:  plot x 数据的向量
%  Y1:  plot y 数据的向量

%  由 MATLAB 于 10-Dec-2022 23:24:13 自动生成

% 创建 figure
figure1 = figure('WindowState','maximized');

% 创建 axes
axes1 = axes('Parent',figure1,'Position',[0.13 0.11 0.775 0.815]);
hold(axes1,'on');

% 创建 plot
plot(X1,Y1,'DisplayName','f(x)','LineWidth',3,'LineStyle','-.',...
    'Color',[0.466666666666667 0.674509803921569 0.188235294117647]);

% 创建 ylabel
ylabel('y');

% 创建 xlabel
xlabel('x');

% 创建 title
title('Name of the Graph');

box(axes1,'on');
grid(axes1,'on');
hold(axes1,'off');
% 设置其余坐标区属性
set(axes1,'XMinorGrid','on','YMinorGrid','on','ZMinorGrid','on');
% 创建 legend
legend(axes1,'show');

