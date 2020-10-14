import java.util.ArrayList;
import java.util.TreeSet;


import java.util.Set;
import java.util.Map;
import java.util.TreeMap;
import java.lang.RuntimeException;
import java.lang.Math;	

public class Scheduler
{
    // In main() after you create a Registry object, create a Scheduler object and pass in the students ArrayList/TreeMap
	// If you do not want to try using a Map then uncomment
	// the line below and comment out the TreeMap line
	
	//ArrayList<Student> students;
	

	
	public TreeMap<String,ActiveCourse> schedule;
	private Set<String> days;
	public Scheduler(TreeMap<String,ActiveCourse> courses)
	{
	  	schedule = courses;
		days = new TreeSet<>();
		days.add("Mon");
		days.add("Tue");
		days.add("Wed");
		days.add("Thu");
		days.add("Fri");
	}
	
	public void setDayAndTime(String courseCode, String day, int startTime, int duration) throws UnknownCourseException, InvalidDayException, InvalidDurationException, InvalidTimeException, LectureTimeCollisionException

	{
		

		try
		{
			TreeMap<String, ArrayList<int[]>> existBlock = new TreeMap<>();
			for (String s : schedule.keySet())
			{
				ActiveCourse ac = schedule.get(s);
				TreeMap<String, ArrayList<int[]>> courseInfo;
				courseInfo = ac.getLectureInfo();
				for (String d : days)
				{
					ArrayList<int[]> blockList = courseInfo.get(d);
					if (existBlock.containsKey(d)) {
						existBlock.get(d).addAll(blockList);
					}
					else
					{
						existBlock.put(d, blockList);
					}

				}
			}
			ActiveCourse c;
			if(!schedule.containsKey(courseCode))
			{
				throw new UnknownCourseException("Unknown Course: " + courseCode);
			}
			if(!days.contains(day))
			{
				throw new InvalidDayException("Invalid Day: " + day);
			}
			if(startTime < 800 || startTime > 1700)
			{
				throw new InvalidTimeException("Invalid Time: " + startTime);
			}
			if(duration < 1 || duration > 3)
			{
				throw new InvalidDurationException("Invalid Duration: " + duration);
			}
			ArrayList<int[]> blockList = existBlock.get(day);
			for (int[] block : blockList)
			{

				int endTime = startTime + duration * 100;
				if ((startTime >= block[0] && startTime < block[1]) || (endTime > block[0] && endTime <= block[1]))
				{
					throw new LectureTimeCollisionException("The day, startTime, and duration should be such that it does not create any overlap with another scheduled course.");
				}
			}
			c = schedule.get(courseCode);
			c.setLectureInfo(startTime, duration, day);
		}
		catch (Exception e)
		{
			System.out.println(e);
		}
	}

	public void autoSetup(String courseCode, int duration)
	{
		if(!schedule.containsKey(courseCode))
		{
			throw new UnknownCourseException("Unknown Course: " + courseCode);
		}
		if(duration < 1 || duration > 3)
		{
			throw new InvalidDurationException("Invalid Duration: " + duration);
		}
		boolean[] hours = {false, false, false, false, false, false, false, false, false, false};
		Map<String, boolean[]> timeTable = new TreeMap<>();
		timeTable.put("Mon", hours.clone());
		timeTable.put("Tue", hours.clone());
		timeTable.put("Wed", hours.clone());
		timeTable.put("Thu", hours.clone());
		timeTable.put("Fri", hours.clone());

		for (String code: schedule.keySet()) {
			ActiveCourse c = schedule.get(code);
			for (String d: days)
			{
				boolean[] t = timeTable.get(d);
				ArrayList<int[]> blockList = c.getLectureInfo().get(d);
				for (int[] block: blockList) {
					int startTime = block[0]/100 - 8;
					int endTime = block[1]/100 - 8;
					if (endTime > 9) {
						break;
					}
					for (int i = startTime; i < endTime; i++) {
						t[i] = true;
					}
				}

			}
		}
		int startTime = -1;
		String day = "";
		for (String d: timeTable.keySet()) {
			boolean[] t = timeTable.get(d);
			for (int i = 0; i < t.length - duration; i++) {
				boolean fit = true;
				for (int j = i; j < i + duration; j++) {
					if (t[j]) {
						fit = false;
					}
				}
				if (fit) {
					startTime = i;
					break;
				}
			}
			if (startTime >= 0) {
				day = d;
				break;
			}
		}
		ActiveCourse c = schedule.get(courseCode);
		if (day != "" && startTime != -1) {
			c.setLectureInfo(startTime * 100 + 800, duration, day);
		} else {
			System.out.println("timeTable not working");
		}
	}
	
	class UnknownCourseException extends RuntimeException
	{
		public UnknownCourseException(String message)
		{
			super(message);
		}
	}

	class InvalidDayException extends RuntimeException
	{
		public InvalidDayException(String message)
		{
			super(message);
		}
	}

	class InvalidTimeException extends RuntimeException
	{
		public InvalidTimeException(String message)
		{
			super(message);
		}
	}

	class InvalidDurationException extends RuntimeException
	{
		public InvalidDurationException(String message)
		{
			super(message);
		}
	}

	class LectureTimeCollisionException extends RuntimeException
	{
		public LectureTimeCollisionException(String message)
		{
			super(message);
		}
	}
	public void clearSchedule(String courseCode) throws UnknownCourseException
	{
		if(schedule.containsKey(courseCode)){
			ActiveCourse ac = schedule.get(courseCode);
			TreeMap<String, ArrayList<int[]>> info = ac.getLectureInfo();
			for (String d: info.keySet()) {
				info.get(d).clear();
			}
		} else {
			throw new UnknownCourseException("Unknown Course: " + courseCode);
		}
	}
	
	public void fillTable(String[][] timetable, String courseCode, String day, int hour, int duration)
	{
		int rowIndex = 0;
		int colIndex = 0;
		for(int i = 0; i < timetable.length; i++)
		{
			if(i == 0){
				continue;
			}
			try{
				int h = Integer.parseInt(timetable[i][0]);
				if(h == hour)
				{
					rowIndex = i;
					break;
				} 	
			}
			catch(NumberFormatException ignored)
			{
			}
			
		}
		for(int j = 1; j < timetable[0].length; j++)
		{
			if(timetable[0][j].equalsIgnoreCase(day))
			{
				colIndex = j;
				break;
			} 	
		}
		for(int i = rowIndex; i < Math.min(timetable.length,rowIndex + duration); i++)
		{
			timetable[i][colIndex] = courseCode;
		}
		timetable[0][0] = "0";
	}
	public void printSchedule()
	{
		String[] weekDay = {"","Mon", "Tue","Wed","Thu","Fri"};
		String[] hours = {"","0800","0900","1000","1100","1200","1300","1400","1500","1600","1700"};
		String[][] timetable = new String[11][6];
		for(int i = 0; i < timetable.length; i++)
		{
		  for (int j = 0; j < timetable[i].length; j++)
		  {      
			timetable[0][0] = "\t";
			timetable[0][j] = weekDay[j];
		  }
		  timetable[i][0] = hours[i];
		}
		  for(String s: schedule.keySet())
	  		{
			ActiveCourse ac = schedule.get(s);
			String courseCode = ac.getCode();
			TreeMap<String, ArrayList<int[]>> courseInfo = ac.getLectureInfo();
			for (String day: courseInfo.keySet())
			{
				ArrayList<int[]> info = courseInfo.get(day);
				for (int[] block: info)
				{
					int hour = block[0];
					int duration = (block[1] - block[0]) / 100;
					fillTable(timetable, courseCode, day, hour, duration);
				}
			}
		   }

		for (String[] a : timetable)
		{
		  for(String b: a)
		  {
			if(b == null || b.equals("0"))
			{
				System.out.print("\t");
			}
      		else System.out.print(b + "\t");
		  }
		  System.out.println();
		}
	}
}


