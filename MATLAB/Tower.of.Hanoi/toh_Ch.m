function toh_Ch(N)

%TOH_CH - Tower of Hanoi Chinese Version
%
% This program is going to
% 1. Solve the Tower of Hanoi problem;
% 2. Show the solution (more exactly, the procedures of movements).
% Try least steps to move disks from Tower A to C with the help of B.
% Explanation of parameters:
% N means the number of disks in Tower A which you are going to move.
% Syntax:
% toh: the default value of N will be 5
% toh(N)
%
% -------------------------------------------------------------------
% Author: Libao Jin
% Date: 2013.06.27 - 2013.07.04
% Copyright (c) 2013 JinLibao
% All rights reserved.
% License: The MIT License (MIT)
% -------------------------------------------------------------------

if nargin == 0
    N = 5;
end

global na nb nc nn X Y;

% Create a GUI and design elements
hf = figure('Color',[0.2745 0.7686 0.9882],...
    'Name','汉诺塔 - 应数1101班 金理宝',...
    'Menu','none');
% Add Title 'Tower of Hanoi' and set the format of it
ht1 = uicontrol(hf,'Style','text',...
    'String','汉诺塔',...
    'FontName','黑体',...
    'FontWeight','bold',...
    'Units','normalized',...
    'Position',[0.3,0.88,0.4,0.08],...
    'BackgroundColor',[0.2745 0.7686 0.9882],...
    'ForegroundColor',[0.9883 0.1406 0.1211]);
% Add Author information to the figure, and some tips
ht2 = uicontrol(hf,'Style','text',...
    'String','应数1101班 金理宝',...
    'FontName','仿宋',...
    'FontWeight','bold',...
    'Units','normalized',...
    'Position',[0.6,0.85,0.25,0.05],...
    'BackgroundColor',[0.2745 0.7686 0.9882],...
    'ForegroundColor',[1 1 0]);
ht3 = uicontrol(hf,'Style','text',...
    'String','Copyright (c) 2013 JinLibao',...
    'FontName','Time New Roman',...
    'FontWeight','normal',...
    'Units','normalized',...
    'Position',[0.40,0.04,0.2,0.03],...
    'BackgroundColor',[0.2745 0.7686 0.9882],...
    'ForegroundColor',[0 0 0]);
ht4 = uicontrol(hf,'Style','text',...
    'String','All rights reserved.',...
    'FontName','Time New Roman',...
    'FontWeight','normal',...
    'Units','normalized',...
    'Position',[0.4,0.01,0.2,0.03],...
    'BackgroundColor',[0.2745 0.7686 0.9882],...
    'ForegroundColor',[0 0 0]);
% Add time teller
ht5 = uicontrol(hf,'Style','text',...
    'FontName','华文行楷',...
    'Units','normalized',...
    'Position',[0.3,0.2,0.4,0.06],...
    'BackgroundColor',[0.2745 0.7686 0.9882],...
    'ForegroundColor',[1 1 1]);
% Add an axes to the figure
ha = axes('Position',[0 0.3 1 0.55]);
% And an slider to control the speed of movements
hs = uicontrol(hf,'Style','Slider',...
    'Units','normalized',...
    'Position',[0.09 0.12 0.15 0.045],...
    'value',0.6 ,...
    'Min',0.001,...
    'Max',0.8);
hsmin = uicontrol(hf,'Style','text',...
    'Fontname','宋体',...
    'String','慢',...
    'Units','normalized',...
    'Position',[0.07 0.075 0.05 0.04],...
    'BackgroundColor',[0.2745 0.7686 0.9882]);
hsmax = uicontrol(hf,'Style','text',...
    'Fontname','宋体',...
    'String','快',...
    'Units','normalized',...
    'Position',[0.21 0.075 0.05 0.04],...
    'BackgroundColor',[0.2745 0.7686 0.9882]);
% Add an button which you can click to close window
hbExit = uicontrol(gcf,'Style','pushbutton',...
    'String','退出',...
    'Fontname','宋体',...
    'Units','normalized',...
    'Position',[0.78 0.12 0.11 0.045],...
    'Callback','close(gcf)');
% Add an button to start or pause movements
hPause = uicontrol(hf,'Style','toggle',...
    'String','开始\暂停',...
    'Units','normalized',...
    'Position',[0.45 0.12 0.11 0.045],...
    'Fontname','宋体',...
    'Value',0);

% In order to be fit with the screen size
% the command below can adjust the size of window
% automatically according to the screen size
% ss = get(0,'ScreenSize');
ss = get(0,'MonitorPositions');
bottom = 50;
height = ss(4)-100;
left = (ss(3)-height*ss(3)/ss(4))/2;
width = ss(3)-2*left;
set(hf,'Position',[left bottom width height]);
if ss(3) >= 1366
    set(ht1,'FontSize',32);
    set(ht2,'FontSize',20);
    set(ht3,'FontSize',10);
    set(ht4,'FontSize',10);
    set(ht5,'FontSize',22);
    set(hbExit,'FontSize',16);
    set(hsmin,'FontSize',16);
    set(hsmax,'FontSize',16);
    set(hPause,'FontSize',16)
elseif ss(3) < 1366
    set(ht1,'FontSize',24);
    set(ht2,'FontSize',16);
    set(ht3,'FontSize',8);
    set(ht4,'FontSize',8);
    set(ht5,'FontSize',20);
    set(hbExit,'FontSize',12);
    set(hsmin,'FontSize',12);
    set(hsmax,'FontSize',12);
    set(hPause,'FontSize',12)
end

% Draw a tower and disks
tower;
hold on;
t = 12*2^N;
X = zeros(4,N,t);
Y = zeros(4,N,t);
for i = 1:N;
    X(1:4,i,1) = [4-(i-1)*0.2; 6+(i-1)*0.2; 6+(i-1)*0.2; 4-(i-1)*0.2];
    Y(1:4,i,1) = [(N-i)*0.4; (N-i)*0.4; (N-i+1)*0.4; (N-i+1)*0.4];
end
p = patch(X(:,:,1),Y(:,:,1),'w');
axis equal;
axis([0,30,0,9]);

% Generate the movements strategy
na = N; nb = 0; nc = 0; nn = 2;
move(N,N,'A','B','C');

% Make an animation of the movements
i = 1;
while i <= nn-1
    toggle = get(hPause,'Value');
    if toggle == 1
        drawnow
        speed = 0.801-get(hs,'Value');
        set(p,'XData',X(:,:,i),'YData',Y(:,:,i));
        pause(speed);
        if i == 1
            tic;
        end
        i = i+1;
    else pause(0.5);
    end
end

% Display how much time spent of the solution.
toc
tt = round(toc*100)/100;
tc = num2str(tt);
set(ht5,'String',['您总共使用了 ' tc ' 秒！']);

    function move(N,n,a,b,c)
        d = 2;
        if n == 1
            switch (a)
                case 'A'
                    na = na-1; j1 = 1; k1 = na;
                case 'B'
                    nb = nb-1; j1 = 2; k1 = nb;
                case 'C'
                    nc = nc-1; j1 = 3; k1 = nc;
            end
            switch (c)
                case 'A'
                    na = na+1; j2 = 1; k2 = na;
                case 'B'
                    nb = nb+1; j2 = 2; k2 = nb;
                case 'C'
                    nc = nc+1; j2 = 3; k2 = nc;
            end
            
            dy1 = [0.6 0.4]*(8.2-k1*0.4);
            if j2-j1 == 2
                d2 = d*2;
                dx = [0.4 0.3 0.2 0.1]*(j2-j1)*10;
            else d2 = d;
                dx = [0.7 0.3]*(j2-j1)*10;
            end
            
            dy2 = [0.6 0.4]*((k2-1)*0.4-8.2);
            for i = 1:d
                Y(:,:,nn) = Y(:,:,nn-1);
                Y(:,n,nn) = Y(:,n,nn)+dy1(i);
                X(:,:,nn) = X(:,:,nn-1);
                nn = nn+1;
            end
            for i = 1:d2
                X(:,:,nn) = X(:,:,nn-1);
                X(:,n,nn) = X(:,n,nn-1)+dx(i);
                Y(:,:,nn) = Y(:,:,nn-1);
                nn = nn+1;
            end
            for i = 1:d
                Y(:,:,nn) = Y(:,:,nn-1);
                Y(:,n,nn) = Y(:,n,nn)+dy2(i);
                X(:,:,nn) = X(:,:,nn-1);
                nn = nn+1;
            end
            
        else
            move(N,n-1,a,c,b);
            
            switch (a)
                case 'A'
                    na = na-1; j1 = 1; k1 = na;
                case 'B'
                    nb = nb-1; j1 = 2; k1 = nb;
                case 'C'
                    nc = nc-1; j1 = 3; k1 = nc;
            end
            switch (c)
                case 'A'
                    na = na+1; j2 = 1; k2 = na;
                case 'B'
                    nb = nb+1; j2 = 2; k2 = nb;
                case 'C'
                    nc = nc+1; j2 = 3; k2 = nc;
            end
            
            dy1 = [0.6 0.4]*(8.2-k1*0.4);
            if j2-j1 == 2
                d2 = d*2;
                dx = [0.4 0.3 0.2 0.1]*(j2-j1)*10;
            else d2 = d;
                dx = [0.7 0.3]*(j2-j1)*10;
            end
            dy2 = [0.6 0.4]*((k2-1)*0.4-8.2);
            for i = 1:d
                Y(:,:,nn) = Y(:,:,nn-1);
                Y(:,n,nn) = Y(:,n,nn)+dy1(i);
                X(:,:,nn) = X(:,:,nn-1);
                nn = nn+1;
            end
            for i = 1:d2
                X(:,:,nn) = X(:,:,nn-1);
                X(:,n,nn) = X(:,n,nn-1)+dx(i);
                Y(:,:,nn) = Y(:,:,nn-1);
                nn = nn+1;
            end
            for i = 1:d
                Y(:,:,nn) = Y(:,:,nn-1);
                Y(:,n,nn) = Y(:,n,nn)+dy2(i);
                X(:,:,nn) = X(:,:,nn-1);
                nn = nn+1;
            end
            move(N,n-1,b,a,c);
        end
    end

    function tower()
        x = ones(100,3);
        y = linspace(0,7.5,100);
        x(:,1) = x(:,1)*5;
        x(:,2) = x(:,2)*15;
        x(:,3) = x(:,3)*25;
        plot(x,y,'LineWidth',10);
        axis off;
        grid minor;
    end
end
