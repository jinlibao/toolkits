% LETTERZ
% Presented by JinLibao
% Copyright (c) 2013 JinLibao
% All Rights Reserved
% Generate an matrix contains a shape of "Z"

function letz = letterz(g)  % g means the color depth range from 0 to 255
letz = zeros(100,80);
letz(12:22,5:75) = g;
letz(78:88,5:75) = g;
for j = 22:78
    for i = 0:14
        letz(j,83+i-j) = g;
    end
end
