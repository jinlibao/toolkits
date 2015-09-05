% LETTERU
% Presented by JinLibao
% Copyright (c) 2013 JinLibao
% All Rights Reserved
% Generate an matrix contains a shape of "U"

function letu = letteru(g)  % g means the color depth range from 0 to 255
letu = zeros(100,80);
letu(12:78,5:15) = g;
letu(12:78,65:75) = g;
letu(78:88,5:75) = g;