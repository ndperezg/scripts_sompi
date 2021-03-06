%function [ffinal,gfinal,Qrfinal,stffinal,stgfinal,stQfinal]=sompik(mmin,mmax,x)
%sompi(mmin,mmax,x) calcula el valor de Q radiativo para una o varias
%frecuencias del vector x superponiendo soluciones (namisos) de ecuaciones
%entre los ordenes mmin y mmax. El c�lculo se realiza hallando las
%frecuencias complejas mediante el algor�tmo de Kumazawa.
close all
cabeza=char(textdata);
tipo=substr(cabeza(1,:),10,3);
estacion=substr(cabeza(2,:),1,4);
fecha=substr(cabeza(3,:),1,19);
mmin = 15;
mmax = 60;
cellfrec = 50;
cellgrow = 40;
anchban = 0.2;
%Preparar y graficar la se�al original

%%%%%%%%%%%%%%%%%%%%%%
x=data;
%%%%%%%%%%%%%%%%%%%%%%
x=x-mean(x);
x=x/max(x);
N=length(x);

%para graficar con filtro
fil=x;
[C,D]=butter(6,0.016,'high');
fil1=filter(C,D,fil);

%figure(1)
%plot(fil1)

%para seleccionar comienzo y fin del evento
%[f1]=ginput(2);
%fil1=fil1(f1(1):f1(2));
%plot(fil1)

%Elegir el inicio y fin de la se�al. Es importante evitar el onset del
%sismo para eliminar la parte no homogenea de la ecuaci�n.

%[x1]=ginput(2);
%x=x((f1(1)+x1(1)-1):(f1(1)+x1(2))-1);
%x = x(x(1):x(floor(length(x)/2)))
%plot(x)


%C�lculo del espectro de Fourier
N=length(x);
esp=abs(fft(x));
Nesp=length(esp);
fs=100;
fre=0.0:fs/Nesp:(fs-fs/Nesp);
%figure(2)
%plot(fre,esp)
%axis([0 15 0 max(esp)]);

%Elecci�n de las frecuencias de inter�s
%[xbi,ybi] = ginput;
%sizeesp=size(esp);
%sizefre=size(fre);
xbi = [1.5;14.5];
ybi = [300;320];
ginf=[xbi ybi];     %Se encierra la frecuencia de inter�s con dos clic y
                    %enter para continuar.
xbi
ybi
ginf
[numfrec numfrecy]=size(ginf);

%Busca los valores de frecuencia m�ximos dentro de los intervalos elegidos 
k=1;
for j=1:(numfrec/2)
    for i=1:length(fre)
        if ginf(k,1) > fre(i) &&  ginf(k,1) < fre(i+1)
            pos(k)=i;
        break
        end
    end
    
    for i=1:length(fre)
        if ginf(k+1,1) > fre(i) &&  ginf(k+1,1) < fre(i+1)
            pos(k+1)=i;
        break
        end
    end
    k=k+2;
end

%Matrices para almacenar resultados finales
ffinal=[];
gfinal=[];
Qrfinal=[];
stffinal=[];
stgfinal=[];
stQfinal=[];

%Bucle para aplicar el m�todo sompi sobre cada una de las frecuencias
%escogidas
xx=x;
kk=1;
for ii=1:(numfrec/2)
    
%Proceso de filtrado al rededor de las frecuencias escogidas    
posmaxesp=find(esp((pos(kk):pos(kk+1))) == max(esp(pos(kk):pos(kk+1))));
mfrec=fre(pos(kk)+posmaxesp);
f1=mfrec-anchban;
f2=mfrec+anchban;
[cb,ca]=butter(4,[f1/50 f2/50]);
xfilter=filter(cb,ca,xx);
posxmax=find(abs(xfilter) == max(abs(xfilter)));
xcut=xfilter(posxmax : length(xfilter));
%figure(3)
%plot(xcut)

%Aplicaci�n del m�todo sompi
[ff,gg]=sompisolo(mmin,mmax,xcut);
plot(ff,gg,'o')
axis([0 0.15 -0.0005 0]);
hold on

%Se ordenan descendentemente las frecuencias y los ratas de decaimiento
%(para agilizar los c�lculos)
for i=1:length(ff);
    for j=1:length(ff);
        if ff(i)>ff(j)
            t=ff(i);
            ff(i)=ff(j);
            ff(j)=t;
            t=gg(i);
            gg(i)=gg(j);
            gg(j)=t;
        end
    end
end
Nff=floor(length(ff)/2);
ff=ff(1:Nff);
gg=gg(1:Nff);

%Preparaci�n de la grilla de b�squeda de concentraci�n de namisos 
ming=-0.0005;
maxg=0;

minf=0;
maxf=0.15;

deltag=(maxg-ming)/cellgrow;
deltaf=(maxf-minf)/cellfrec;

df=minf:deltaf:maxf;
dg=ming:deltag:maxg;

%Graficaci�n de la grilla
if ii==1
for i=1:length(df)
xf=df(i)+zeros(1,length(dg));
yg=ming:deltag:maxg;
plot(xf,yg,'Color',[0.77 0.77 0.77])
hold on
end

for i=1:length(dg)
yg=dg(i)+zeros(1,length(df));
xf=minf:deltaf:maxf;
plot(xf,yg,'Color',[0.77 0.77 0.77])
hold on
end
end

Ndf=length(df);
Ndg=length(dg);
fcount=[];
gcount=[];

%B�squeda de namisos dentro de cada celda de la grilla
for i=1:Ndf-1
    for j=1:Ndg-1
            for k=1:length(ff)
                if ((ff(k) >= df(i)) && (ff(k) < df(i+1)) && (gg(k) >= dg(j)) && (gg(k) < dg(j+1)))
                   l=l+1;
                    fcount=[fcount;l ff(k)];
                    gcount=[gcount;l gg(k)];
                end        
            end
            l=0;
    end
end

%Selecci�n de la celda con mayor cantidad de namisos
maxlr=[];
numfg=[];
[maxlr,maxlc]=find(fcount(:,1) == max(fcount(:,1)));
numfg(1,1)=maxlr(1,1)-fcount(maxlr(1,1));
if numfg(1,1)==0
   numfg(1,1)=1;
end

%Vectores con los valores de los namisos seleccionados
fff=fcount(numfg(1,1):maxlr(1,1),2);
ggg=gcount(numfg(1,1):maxlr(1,1),2);

%Valores finales promedio de frecuencia, tasa de decaimiento y Q radiativo
fprom=mean(fff);
gprom=mean(ggg);
Qr=fff./(-2*ggg);
Qrprom=mean(Qr);

%Vectores con las respectivas desviaciones estandar
stf=[];
stg=[];
stq=[];
stf=[stf;std(fff,1)];
stg=[stg;std(ggg,1)];
stq=[stq;std(Qr,1)];

%Preparaci�n de las gr�ficas con lineas de iso-Q
if ii==1
r=0:0.01:0.5;
Q=1:(50):900;
invQ=1./(2*Q);
    for i=1:length(Q)
    cuasiQ=-r*invQ(i);
    plot(r,cuasiQ)
    end
    xlabel('Frequency /Hz');
    ylabel('Gradient /sec-1');
    grid off
end
%Vectores donde se almacenan los resultados finales
ffinal=[ffinal,fprom];
gfinal=[gfinal,gprom];
Qrfinal=[Qrfinal,Qrprom];
stffinal=[stffinal,stf];
stgfinal=[stgfinal,stg];
stQfinal=[stQfinal,stq];
%hold on
kk=kk+2;

end
clc
%Mostrando los resultados en pantalla
stfporc=100*stffinal./ffinal;
stgporc=abs(100*stgfinal./gfinal);
stQporc=100*stQfinal./Qrfinal;

resultados=[100*ffinal' stfporc' gfinal' stgporc' Qrfinal' stQporc'];
[rres cres]=size(resultados);

disp('      f       Err-f(%)    G       Err-G(%)    Qr      Err-Qr(%)')
disp(resultados)

%Escritura de los resultados finales en un archivo de texto con nombre
%Resultados_Sompi.txt. Este archivo se genera en el directorio de trabajo
fid = fopen('/home/nelson/tesis/my_sompi/pruebas_sompik_2012.txt','a+t');
for i=1:length(ffinal)
    fprintf(fid,'%s %s %s %6.2f  %8.4f  %10.7f %10.7f %6.2f %6.2f %6.2f \n',fecha,estacion,tipo,100*ffinal(i),stffinal(i),gfinal(i),stgfinal(i),Qrfinal(i),stQfinal(i), stQporc(i));
end       
    fclose(fid);
    
        
