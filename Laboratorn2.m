clc
close all 
clear all

x1 = [];
x2 = [];
y1 = [];
y2 = [];

add =0.5:0.1:5;
k = add(randi([1 length(add)]));
b=23;


abscissa_intersection = (100-b)/k; 

if abscissa_intersection < 100
abscissa_intersection = abscissa_intersection ; 
else
abscissa_intersection = 100; 
end

line_x = [];
line_y = [];

for i= 1:abscissa_intersection
line_x = [line_x,i];
line_y = [line_y,k*i+b];
end

for i = 1:500
if abscissa_intersection > 100
buff_x1 = randi(100);
else
buff_x1 = randi(round(abscissa_intersection) - 1); 
end
buff_y1 = round(randi(round(100 - (k*buff_x1 + b))) + (k*buff_x1+b) - 1);
buff_x2 = randi(100);
buff_y2 = mod(randi(round((k*buff_x2 + b))), 100);

x1 = [x1 , buff_x1];
x2 = [x2 , buff_x2];
y1 = [y1 , buff_y1];
y2 = [y2 , buff_y2];
end

[X1,Y1] = delrepeat(x1,y1);
[X2,Y2] = delrepeat(x2,y2);
classifiers1 =[]; classifiers2 =[]; 




for i=1:length(x1)
    classifiers1(i)=1;
end

for i=1:length(x2)
    classifiers2(i)= -1;
end

allx = [x1 x2]; ally =[y1 y2]; allc = [classifiers1 classifiers2];
MAIN=[];CONTROL=[];RESULT=[];
TRAINX=[];TRAINY=[];FCOPY=[];
mistakes = 0;
num_trees_generator = 1:5:50;
result_iter = 1;

for n=num_trees_generator
    
    for i = 1:length(allx) 
        
        CONTROLX = allx(i);
        CONTROLY = ally(i);
        Fclass = allc(i);
        
        TRAINX = allx;
        TRAINX(i)=[];
        
        TRAINY = ally;
        TRAINY(i)=[];
        
        FCOPY=allc;
        FCOPY(i) = [];
      
        MAIN = [TRAINX(:),TRAINY(:),FCOPY(:)];
        CONTROL = [CONTROLX(:) CONTROLY(:)];
       
        controlx=[]; trainx=[]; controly=[]; trainy=[]; copy=[];
        
        for j = 1:n
                u = ceil(length(TRAINX)*rand([1 length(TRAINX)]));
                c = unique(u);
                t = setdiff(1:length(TRAINX),c);
                
                for k = 1:length(c)
                    controlx(k)= TRAINX(c(k));
                    controly(k)= TRAINY(c(k));
                    copy1(k)=FCOPY(c(k));
                end
                
                for k = 1:length(t)
                    trainx(k)= TRAINX(t(k));
                    trainy(k)= TRAINY(t(k));
                    copy(k)=FCOPY(t(k));
                end
        
                main = [ trainx(:), trainy(:), copy(:)];
                control = [ controlx(:) controly(:)];
                
                Tree = fitctree(main(:,1:2), main(:,3));
                ResTree = predict(Tree, CONTROL(:,1:2));
                
                g=ResTree;
                
                if g == Fclass
                    RESULT(i)= g;
                    good = 1;
                else
                    RESULT(i)= g;
                    mistakes = mistakes+1;
                end
            controlx=[]; trainx=[]; controly=[]; trainy=[]; copy=[]; g=0;
        end
    end
    
    M(n) = ceil(mistakes/n)
    mean_M = mean(M);
    
    result(result_iter, :) = [n, mean_M];
    result_iter = result_iter + 1;
    mistakes=0;
    
end

hold on
plot(result(:, 1), result(:, 2), 'r-')
hold off


% for i=1:length(result)
%    if result(i, 2)== min(mean_M)
%       N=i;
%    end
% end



q = [1:100];
p = [1:100];

[XX,YY] = meshgrid(q,p);
result = [XX(:) YY(:)];

A= result(1:10000);
B= result(10001:20000);

for i = 1:length(x1)
    for j = 1:length(A)
        if A(j) == x1(i) && B(j)==y1(i)
            A(j) = [0];
            B(j) = [0];
        end
    end
end
A(A==0) =[];
B(B==0) =[];

for i = 1:length(x2)
    for j = 1:length(A)
        if A(j) == x2(i) && B(j)==y2(i)
            A(j)= [0];
            B(j) = [0];
        end
    end
end
A(A==0) =[];
B(B==0) =[];

MAIN1=[ allx(:), ally(:), allc(:)];
TRAIN1 = [ A(:) B(:)];

controlx1=[]; trainx1=[]; controly1=[]; trainy1=[]; fcopy1=[]; fcopy11=[];

        for j = 1:n
                u = ceil(length(allx)*rand([1 length(allx)]));
                c = unique(u);
                t = setdiff(1:length(allx),c);
                
                for m = 1:length(c)
                    controlx1(m)= allx(c(m));
                    controly1(m)= allx(c(m));
                    fcopy11(m)=allc(c(m));
                end
                
                for m = 1:length(t)
                    trainx1(m)= allx(t(m));
                    trainy1(m)= allx(t(m));
                    fcopy1(m)=allc(t(m));
                end
                
                main1 = [ trainx1(:), trainy1(:), fcopy1(:)];
                control1 = [ controlx1(:) controly1(:)];
                
                Tree1 = fitctree(main(:,1:2), main(:,3));
                ResTree1 = predict(Tree1, TRAIN1(:,1:2));
                
                g1=ResTree1;
                for i=1:length(g1)
                    if g1(i)  == 1
                        FX1(i)= A(i);
                        FY1(i)= B(i);
                    else
                        FX2(i)= A(i);
                        FY2(i)= B(i);
                    end
                end
                controlx1=[]; trainx1=[]; controly1=[]; trainy1=[]; fcopy1=[]; fcopy11=[]; g1=0;
        end
        
figure  
hold on
plot(line_x,line_y, 'g', 'LineWidth',2)
plot(x1,y1, 'k.', x2,y2,'r.',FX1,FY1,'y.',FX2,FY2,'g.')
%,FX2,FY2,'g.'