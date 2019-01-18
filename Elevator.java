import java.util.Scanner;

public class Elevator {
	
	static int floor = 0, choice1,choice2, person = 0;
	
	public static void main(String[] args) {	
		
		
		floor= 0+ ((int) (Math.random() * 10));
		
        System.out.println("The elevator is on floor:  " + floor);
        
        System.out.print("\nWhich floor are you at now (0-10)");
        
        Scanner input=new Scanner(System.in);
        int floorstart=input.nextInt();
        
        if(floorstart>10||floorstart<0) {
        	System.out.println("enter valid floor number! (0-10)");
        	
        }
        else if(floor == floorstart){
            System.out.println("\nEnter the elevator");
        }

        else if(floor > floorstart){
            ElevatorDown();
        }

        else if(floor < floorstart){
            ElevatorUp();
        }
        
        choice1 = floorstart;

        System.out.println("\nTo which floor would you want to go (0-10)");
        
        Scanner input2 = new Scanner(System.in);
        int floorchoice2 = input2.nextInt();
        
        choice2=floorchoice2;
        
        if(floorchoice2>10||floorchoice2<0) {
        	System.out.println("enter valid floor number! (0-10)");
        }
        
        else if(floor > floorchoice2){
            ElevatorDown();
        }

        else if(floor < floorchoice2){
            ElevatorUp();
        }
        //else if (floorchoice2 > 10 || floorchoice2 < 0) {
        //	System.out.println("input value between 0 and 10!");
        //}

    }

    public static void ElevatorUp()
    {
        System.out.println("\nThe elevator is on it's way up...");

        for (person = choice2; choice2>=floor; floor++)

            System.out.println("passing floor.. " + floor);

        System.out.println("\nPLING!... The elevator has arrived");
    }

    public static void ElevatorDown()
    {
        System.out.println("\nThe elevator is on it's way down...");
        
        for (person = choice2; choice2<=floor; floor--)

            System.out.println("passing floor.. " + floor);

        System.out.println("\nPLING!... the elevator has arrived ");
        
	}

    
}




