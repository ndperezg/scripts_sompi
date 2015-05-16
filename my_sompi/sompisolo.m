function [ff,gg]=sompisolo(mmin,mmax,x)
ff=[];
gg=[];
N=length(x);
for m=mmin:mmax
c=1/(N-m);
for k=0:m
for l=0:m
    Po(k+1,l+1)=0;
for t=m:N-1
    Po(k+1,l+1)=x(t-k+1)*x(t-l+1)+Po(k+1,l+1);
end
end
end

P=c*Po;

[evec,eval]=eig(P);

veval=diag(eval);

[mineval indi]=min(veval);

a=evec(:,indi);

a=a';

z=roots(a);

zv=log(z);

gama=real(zv);

omega=imag(zv);

g=gama/(2*pi);

f=omega/(2*pi);

ff=[ff;f];

gg=[gg;g];

Q1=f./(-2*g);

end