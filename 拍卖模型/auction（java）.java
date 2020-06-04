public class auction{
	public static void main (String[] args) {
		double V1=100.0,V2=1000.0;
		double v1=0.0,b1=0.0,b2=0.0;
		int n=100;
	
		double result=0.0;
		double index=0.0,sum=0.0;
		v1=100.0+900*(Math.random());
		System.out.println(v1);
		for(b1=V1;b1<=V2;b1++){
			double y=0.0;
			//b2=0.0;
			b2=b1-(b1-V1)/n;
			//for(double i=V1;i<b1;i++){
				//double x=(i-V1)/(b1-V1);
				//b2+=(Math.pow(x,n-2))*i;	
			//}
			y=(b1-V1)/(V2-V1);
			result=(Math.pow(y,n-1))*(v1-b2);
			System.out.println(b1+"  "+result+"  "+b2);
			if(result>sum){
				sum=result;
				index=b1;
			}
		}
		System.out.print(index);
	}
}
