function [ x1,y1 ] = delrepeat( x1,y1 )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
for i = 1:length(x1)
    for j = (i+1) : length(x1)
        if x1(i) == x1(j) && y1(i)==y1(j)
            x1(i)= [0];
            y1(i) = [0];
        end
    end
end
x1(x1==0) =[];
y1(y1==0) =[];

end


