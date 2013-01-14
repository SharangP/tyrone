% analyze bitly data

CSVFILE = 'bitly2.csv';
D = importdata(CSVFILE);

Unique = unique(D.textdata);
Cells = cell(length(Unique),3);

%% never again

for i = 1:length(Unique)
    display(i)
    Cells{i,1} = Unique(i);
    Cells{i,2} = [D.data(find(strcmp(D.textdata,Unique(i)),1,'first'),2)];
    Cells{i,3} = [D.data(strcmp(D.textdata,Unique(i)),1)];
end

%% again

for i = 1:length(Cells(:,3))
    sums(i) = sum(Cells{i,3});
    lens(i) = length(Cells{i,3});
end