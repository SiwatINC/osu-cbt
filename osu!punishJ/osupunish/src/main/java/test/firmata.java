package test;

import org.firmata4j.firmata.FirmataDevice;
import org.firmata4j.*;
import jssc.*;
public class firmata {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		IODevice due = new FirmataDevice("COM14");
		due.start();
		due.ensureInitializationIsDone();
	}

}
