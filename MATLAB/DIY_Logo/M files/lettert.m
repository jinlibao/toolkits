% LETTERT
% Presented by JinLibao
% Copyright (c) 2013 JinLibao
% All Rights Reserved
% Generate an matrix contains a shape of "T"

function lett = lettert(g)  % g means the color depth range from 0 to 255
lett = zeros(100,80);
lett(12:22,5:75) = g;
lett(22:88,35:45) = g;