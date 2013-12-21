clear all;
close all;

%MNIST
mnist_test =[98.99 98.93 98.76 98.6 99.04 99.01];
mnist_train = [99.67 99.45 99.16 98.76 99.87 99.99];
mnist_size = [800 400 200 100 1600 6000];
%Sort stuff
[a ind_sort] = sort(mnist_size);
mnist_size = mnist_size(ind_sort);
mnist_test = mnist_test(ind_sort);
mnist_train = mnist_train(ind_sort);

slope = -(mnist_train(2) - mnist_train(1))*1./(1./mnist_size(2)^(1/4) - 1./mnist_size(1)^(1/4));
mnist_bound = mnist_train(1)-slope*(1./mnist_size.^(1/4) - 1./min(mnist_size)^(1/4));

slope = -(mnist_test(2) - mnist_test(1))*1./(1./mnist_size(2)^(1/4) - 1./mnist_size(1)^(1/4));
mnist_bound_test = mnist_test(1)-slope*(1./mnist_size.^(1/4) - 1./min(mnist_size)^(1/4));

mnist_bound(mnist_bound>100) = 100;
mnist_bound_test(mnist_bound_test>100) = 100;

figure;
plot(mnist_size,mnist_train,'r','LineWidth',3)
xlabel('Codebook size','fontsize',20);
ylabel('Accuracy','fontsize',20);
hold on
plot(mnist_size,mnist_bound,'r--','LineWidth',3)
plot(mnist_size,mnist_test,'LineWidth',3)
% plot(mnist_size,mnist_bound_test,'--','LineWidth',3)
legend('Empirical Train','Nystrom Bound Train','Empirical Test');
set(gca,'fontsize',20)
title('MNIST')


%CIFAR
cifar_data= [87.5	78.4	81.9	75.5	75.6	71.6	70.6	68.5	91.6	79.5	97	81.7	66.69	64.7];
cifar_test = cifar_data(2:2:end);
cifar_train = cifar_data(1:2:end);
cifar_size = [800 500 200 100 1600 6000 50];
%Sort stuff
[a ind_sort] = sort(cifar_size);
cifar_size = cifar_size(ind_sort);
cifar_test = cifar_test(ind_sort);
cifar_train = cifar_train(ind_sort);

slope = -(cifar_train(2) - cifar_train(1))*1./(1./cifar_size(2)^(1/4) - 1./cifar_size(1)^(1/4));
cifar_bound = cifar_train(1)-slope*(1./cifar_size.^(1/4) - 1./min(cifar_size)^(1/4));

slope = -(cifar_test(2) - cifar_test(1))*1./(1./cifar_size(2)^(1/4) - 1./cifar_size(1)^(1/4));
cifar_bound_test = cifar_test(1)-slope*(1./cifar_size.^(1/4) - 1./min(cifar_size)^(1/4));

figure;
plot(cifar_size,cifar_train,'r','LineWidth',3)
xlabel('Codebook size','fontsize',20);
ylabel('Accuracy','fontsize',20);
hold on
plot(cifar_size,cifar_bound,'r--','LineWidth',3)
plot(cifar_size,cifar_test,'LineWidth',3)
% plot(cifar_size,cifar_bound_test,'--','LineWidth',3)
legend('Empirical Train','Nystrom Bound Train','Empirical Test');
set(gca,'fontsize',20)
title('CIFAR')

% %TIMIT
timit_data= [50.5	47.1	46.2	44.1	41.4	40.3	36	35.4	54.7 	49.4	62.7	52.8	65.5	53.5];
timit_test = timit_data(2:2:end);
timit_train = timit_data(1:2:end);
timit_size = [800		400		200		100		1600		6000		8000];
%Sort stuff
[a ind_sort] = sort(timit_size);
timit_size = timit_size(ind_sort);
timit_test = timit_test(ind_sort);
timit_train = timit_train(ind_sort);

slope = -(timit_train(2) - timit_train(1))*1./(1./timit_size(2)^(1/4) - 1./timit_size(1)^(1/4));
timit_bound = timit_train(1)-slope*(1./timit_size.^(1/4) - 1./min(timit_size)^(1/4));

slope = -(timit_test(2) - timit_test(1))*1./(1./timit_size(2)^(1/4) - 1./timit_size(1)^(1/4));
timit_bound_test = timit_test(1)-slope*(1./timit_size.^(1/4) - 1./min(timit_size)^(1/4));

figure;
plot(timit_size,timit_train,'r','LineWidth',3)
xlabel('Codebook size','fontsize',20);
ylabel('Accuracy','fontsize',20);
hold on
plot(timit_size,timit_bound,'r--','LineWidth',3)
plot(timit_size,timit_test,'LineWidth',3)
% plot(timit_size,timit_bound_test,'--','LineWidth',3)
legend('Empirical Train','Nystrom Bound Train','Empirical Test');
set(gca,'fontsize',20)
title('TIMIT')

% %WSJ
wsj_data= [61.5	62	57.2	57.8	52.2	52.8	47.1	47.8	65.5	65.7	71.7	71.3	42.1	43.1];
wsj_test = wsj_data(2:2:end);
wsj_train = wsj_data(1:2:end);
wsj_size = [800		400		200		100		1600		6000		50];
%Sort stuff
[a ind_sort] = sort(wsj_size);
wsj_size = wsj_size(ind_sort);
wsj_test = wsj_test(ind_sort);
wsj_train = wsj_train(ind_sort);

slope = -(wsj_train(2) - wsj_train(1))*1./(1./wsj_size(2)^(1/4) - 1./wsj_size(1)^(1/4));
wsj_bound = wsj_train(1)-slope*(1./wsj_size.^(1/4) - 1./min(wsj_size)^(1/4));

slope = -(wsj_test(2) - wsj_test(1))*1./(1./wsj_size(2)^(1/4) - 1./wsj_size(1)^(1/4));
wsj_bound_test = wsj_test(1)-slope*(1./wsj_size.^(1/4) - 1./min(wsj_size)^(1/4));

figure;
plot(wsj_size,wsj_train,'r','LineWidth',3)
xlabel('Codebook size','fontsize',20);
ylabel('Accuracy','fontsize',20);
hold on
plot(wsj_size,wsj_bound,'r--','LineWidth',3)
plot(wsj_size,wsj_test,'LineWidth',3)
% plot(wsj_size,wsj_bound_test,'--','LineWidth',3)
legend('Empirical Train','Nystrom Bound Train','Empirical Test');
set(gca,'fontsize',20)
title('WSJ')