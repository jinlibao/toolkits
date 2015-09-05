% DIYCOLORLOGO
% Prensented by JinLibao
% Copyright (c) 2013 JinLibao
% All Rights Reserved
% You can design your own logo consists of letters you enter,
% Then you can choose the color and the depth of color of the characters

disp('DIY your own color logo!');
string = input('Please enter a string below:\n','s');       % display tips
n = length(string);
depth = input('Please enter the depth of color (range from 0 to 1) respectively:\n');
mat = [];
colormat = [];
RGB = input('Please enter RGB(range from 0 to 255) to choose the color you want:\n');
for k = 1:n
    switch(string(k))
        case 'A'
                A = imread('..\Letters\A.png');
                A = 255-A;
                for i = 1:500
                    for j = 1:378
                        if A(i,j) ~= 0
                            A(i,j) = A(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat A];
        case 'B'
                B = imread('..\Letters\B.png');
                B = 255-B;
                for i = 1:500
                    for j = 1:378
                        if B(i,j) ~= 0
                            B(i,j) = B(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat B];
        case 'C'
                C = imread('..\Letters\C.png');
                C = 255-C;
                for i = 1:500
                    for j = 1:378
                        if C(i,j) ~= 0
                            C(i,j) = C(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat C];
        case 'D'
                D = imread('..\Letters\D.png');
                D = 255-D;
                for i = 1:500
                    for j = 1:378
                        if D(i,j) ~= 0
                            D(i,j) = D(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat D];
        case 'E'
                E = imread('..\Letters\E.png');
                E = 255-E;
                for i = 1:500
                    for j = 1:378
                        if E(i,j) ~= 0
                            E(i,j) = E(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat E];
        case 'F'
                F = imread('..\Letters\F.png');
                F = 255-F;
                for i = 1:500
                    for j = 1:378
                        if F(i,j) ~= 0
                            F(i,j) = F(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat F];
        case 'G'
                G = imread('..\Letters\G.png');
                G = 255-G;
                for i = 1:500
                    for j = 1:378
                        if G(i,j) ~= 0
                            G(i,j) = G(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat G];
        case 'H'
                H = imread('..\Letters\H.png');
                H = 255-H;
                for i = 1:500
                    for j = 1:378
                        if H(i,j) ~= 0
                            H(i,j) = H(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat H];
        case 'I'
                I = imread('..\Letters\I.png');
                I = 255-I;
                for i = 1:500
                    for j = 1:378
                        if I(i,j) ~= 0
                            I(i,j) = I(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat I];
        case 'J'
                J = imread('..\Letters\J.png');
                J = 255-J;
                for i = 1:500
                    for j = 1:378
                        if J(i,j) ~= 0
                            J(i,j) = J(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat J];
        case 'K'
                K = imread('..\Letters\K.png');
                K = 255-K;
                for i = 1:500
                    for j = 1:378 
                        if K(i,j) ~= 0
                            K(i,j) = K(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat K];
        case 'L'
                L = imread('..\Letters\L.png');
                L = 255-L;
                for i = 1:500
                    for j = 1:378
                        if L(i,j) ~= 0
                            L(i,j) = L(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat L];
        case 'M'
                M = imread('..\Letters\M.png');
                M = 255-M;
                for i = 1:500
                    for j = 1:378
                        if M(i,j) ~= 0
                            M(i,j) = M(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat M];
        case 'N'
                N = imread('..\Letters\N.png');
                N = 255-N;
                for i = 1:500
                    for j = 1:378
                        if N(i,j) ~= 0
                            N(i,j) = N(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat N];
        case 'O'
                O = imread('..\Letters\O.png');
                O = 255-O;
                for i = 1:500
                    for j = 1:378
                        if O(i,j) ~= 0
                            O(i,j) = O(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat O];
        case 'P'
                P = imread('..\Letters\P.png');
                P = 255-P;
                for i = 1:500
                    for j = 1:378
                        if P(i,j) ~= 0
                            P(i,j) = P(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat P];
        case 'Q'
                Q = imread('..\Letters\Q.png');
                Q = 255-Q;
                for i = 1:500
                    for j = 1:378
                        if Q(i,j) ~= 0
                            Q(i,j) = Q(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat Q];
        case 'R'
                R = imread('..\Letters\R.png');
                R = 255-R;
                for i = 1:500
                    for j = 1:378
                        if R(i,j) ~= 0
                            R(i,j) = R(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat R];
        case 'S'
                S = imread('..\Letters\S.png');
                S = 255-S;
                for i = 1:500
                    for j = 1:378
                        if S(i,j) ~= 0
                            S(i,j) = S(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat S];
        case 'T'
                T = imread('..\Letters\T.png');
                T = 255-T;
                for i = 1:500
                    for j = 1:378
                        if T(i,j) ~= 0
                            T(i,j) = T(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat T];
        case 'U'
                U = imread('..\Letters\U.png');
                U = 255-U;
                for i = 1:500
                    for j = 1:378
                        if U(i,j) ~= 0
                            U(i,j) = U(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat U];
        case 'V'
                V = imread('..\Letters\V.png');
                V = 255-V;
                for i = 1:500
                    for j = 1:378
                        if V(i,j) ~= 0
                            V(i,j) = V(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat V];
        case 'W'
                W = imread('..\Letters\W.png');
                W = 255-W;
                for i = 1:500
                    for j = 1:378
                        if W(i,j) ~= 0
                            W(i,j) = W(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat W];
        case 'X'
                X = imread('..\Letters\X.png');
                X = 255-X;
                for i = 1:500
                    for j = 1:378
                        if X(i,j) ~= 0
                            X(i,j) = X(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat X];
        case 'Y'
                Y = imread('..\Letters\Y.png');
                Y = 255-Y;
                for i = 1:500
                    for j = 1:378
                        if Y(i,j) ~= 0
                            Y(i,j) = Y(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat Y];
        case 'Z'
                Z = imread('..\Letters\Z.png');
                Z = 255-Z;
                for i = 1:500
                    for j = 1:378
                        if Z(i,j) ~= 0
                            Z(i,j) = Z(i,j)*depth(k);
                        end
                    end
                end
                mat = [mat Z];
        case ' '
                space = zeros(500,50);
                mat = [mat space];
    end
end

mat = double(mat);
for i = 1:3
    colormat(:,:,i) = RGB(i)*mat/255;
end
colormat1 = uint8(colormat);
colormat2 = uint8(255-colormat);
imwrite(colormat1,'..\Results\colorLogo1.png');
imwrite(colormat2,'..\Results\colorLogo2.png');