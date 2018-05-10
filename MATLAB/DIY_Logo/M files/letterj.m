% LETTERU
% Presented by JinLibao
% Copyright (c) 2013 JinLibao
% All Rights Reserved
% Generate an matrix contains a shape of "U"

function letj= letterj(g)  % g means the color depth range from 0 to 255
letj = zeros(100,80);      % generate a 100x80 zero matrix
letj(12:78,65:75) = g;
letj(78:88,5:65) = g;
letj(68:78,5:15) = g;
for j = 73:78
    for i = 1:j-73+1
        letj(j,65-i) = g;
    end
end
for j = 78:88
    for i = 1:88-j
        letj(j,65+i) = g;
    end
end
