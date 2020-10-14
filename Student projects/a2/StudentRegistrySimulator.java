//Xuan Thanh Le
//Student ID: 500962159

import java.util.Scanner;


// import Scheduler.UnknownCourseException;
public class StudentRegistrySimulator 
{
	public static void main(String[] args) 
	{
		try
		{
		Registry registry = new Registry();
		Scheduler scheduler = new Scheduler(registry.getCourses());
		Scanner scanner = new Scanner(System.in);
		System.out.println(">");
		while (scanner.hasNextLine()) 
		{
			String inputLine = scanner.nextLine();
			if (inputLine == null || inputLine.equals(""))
				continue;

			Scanner commandLine = new Scanner(inputLine);
			String command = commandLine.next();

			if (command == null || command.equals(""))
				continue;

			else if (command.equalsIgnoreCase("L") || command.equalsIgnoreCase("LIST")) 
			{
				registry.printAllStudents();
			} else if (command.equalsIgnoreCase("Q") || command.equalsIgnoreCase("QUIT")) 
			{
				commandLine.close();
				return;
			} else if (command.equalsIgnoreCase("REG")) 
			{
				String name;
				String id;

				try 
				{
					name = commandLine.next();
					id = commandLine.next();
				}

				catch (Exception e) 
				{
					System.out.println("Expect name and id student");
					continue;
				}
				if (isNumeric(id) && isStringOnlyAlphabet(name)) 
				{
					registry.addNewStudent(name, id);
				} else if (!isNumeric(id)) 
				{
					System.out.println("Invalid Characters in ID " + id);
				} else if (!isStringOnlyAlphabet(name)) 
				{
					System.out.println("Invalid Characters in Name " + name);
				} else if (id == null)
				{
					continue;
				}
				// register a new student in registry
				// get name and student id string
				// e.g. reg JohnBoy 74345
				// Checks:
				// ensure name is all alphabetic characters
				// ensure id string is all numeric characters

			} else if (command.equalsIgnoreCase("DEL")) 
			{
				String id;
				try 
				{
					id = commandLine.next();
				} catch (Exception e) 
				{
					System.out.println("Error");
					continue;
				}
				if (isNumeric(id)) 
				{
					registry.removeStudent(id);
				} else if (!isNumeric(id)) 
				{
					System.out.println("Invalid Characters in ID " + id);
				}
				// delete a student from registry
				// get student id
				// ensure numeric
				// remove student from registry
			}

			else if (command.equalsIgnoreCase("ADDC")) 
			{
				String id;
				String courseCode;
				try 
				{
					id = commandLine.next();
					courseCode = commandLine.next().toUpperCase();
				} 
				catch (Exception e) 
				{
					System.out.println("Expect ID and CourseCode");
					continue;
				}
				if (isNumeric(id)) 
				{
					try{
					registry.addCourse(id, courseCode);}
					catch(Exception e)
					{
						System.out.println(e);
						continue;
					}
				} else if (!isNumeric(id)) 
				{
					System.out.println("Invalid Characters in ID " + id);
				}
				// add a student to an active course
				// get student id and course code strings
				// add student to course (see class Registry)

			} else if (command.equalsIgnoreCase("DROPC")) 
			{
				String id;
				String courseCode;
				try 
				{
					id = commandLine.next();
					courseCode = commandLine.next().toUpperCase();
				} 
				catch (Exception e) 
				{
					System.out.println("Expect ID and CourseCode");
					continue;
				}
				if (isNumeric(id)) 
				{
					try{
					registry.dropCourse(id, courseCode);}
					catch(Exception e)
					{
						System.out.println(e);
						continue;
					}
				} else if (!isNumeric(id)) 
				{
					System.out.println("Invalid Characters in ID " + id);
				}
				// get student id and course code strings
				// drop student from course (see class Registry)
			} else if (command.equalsIgnoreCase("PAC")) 
			{
				registry.printActiveCourses();
				// print all active courses
			} else if (command.equalsIgnoreCase("PCL")) 
			{
				String courseCode;
				try 
				{
					courseCode = commandLine.next().toUpperCase();
				} 
				catch (Exception e) 
				{
					System.out.println("Expect courseCode");
					continue;
				}
				try 
				{
					registry.printClassList(courseCode);
				} 
				catch (Exception e) 
				{
					System.out.println(e);
					continue;
				}
				// get course code string
				// print class list (i.e. students) for this course

			} else if (command.equalsIgnoreCase("PGR")) 
			{
				String courseCode;
				try 
				{
					courseCode = commandLine.next().toUpperCase();
				} 
				catch (Exception e) 
				{
					System.out.println("Expect courseCode");
					continue;
				}
				try
				{
				registry.printGrades(courseCode);
				}
				catch(Exception e)
				{
					System.out.println(e);
					continue;
				}
				// get course code string
				// print name, id and grade of all students in active course
			} else if (command.equalsIgnoreCase("PSC")) 
			{
				String id;
				try 
				{
					id = commandLine.next();
				} 
				catch (Exception e) 
				{
					System.out.println("Expect ID Student");
					continue;
				}
				if (isNumeric(id)) 
				{
					try
					{
					registry.printCreditCourses(id);
					}
					catch(Exception e)
					{
						System.out.println(e);
						continue;
					}
				} else if (!isNumeric(id)) 
				{
					System.out.println("Invalid Characters in ID " + id);
				}
				// get student id string
				// print all credit courses of student

			} else if (command.equalsIgnoreCase("PST")) 
			{
				String id;
				try 
				{
					id = commandLine.next();
				} 
				catch (Exception e) 
				{
					System.out.println("Expect ID Student");
					continue;
				}
				if (isNumeric(id)) 
				{
					try
					{
						registry.printStudentAlphabetTranscript(id);
					}
					catch(Exception e)
					{
						System.out.println(e);
						continue;
					}
				} else if (!isNumeric(id)) 
				{
					System.out.println("Invalid Characters in ID " + id);
				}
				// get student id string
				// print student transcript

			} else if (command.equalsIgnoreCase("SFG")) 
			{
				String courseCode;
				String id;
				double grade;
				try 
				{
					courseCode = commandLine.next().toUpperCase();
					id = commandLine.next();
					grade = commandLine.nextDouble();
				} 
				catch (Exception e) 
				{
					System.out.println("Expect CourseCode, ID Student and numeric grade, please try again");
					continue;
				}
				if (isNumeric(id)) 
				{
					try
					{
					registry.setFinalGrade(courseCode, id, grade);
					}
					catch(Exception e)
					{
						System.out.println(e);
						continue;
					}
				} else if (!isNumeric(id)) 
				{
					System.out.println("Invalid Characters in ID " + id);
				}
				// set final grade of student
				// get course code, student id, numeric grade
				// use registry to set final grade of this student (see class Registry)
			} else if (command.equalsIgnoreCase("SCN")) 
			{
				String courseCode;
				try 
				{
					courseCode = commandLine.next().toUpperCase();
				} 
				catch (Exception e) 
				{
					System.out.println("Expect courseCode");
					continue;
				}
				try 
				{
					registry.sortCourseByName(courseCode);
				} 
				catch (Exception e) 
				{
					System.out.println(e);
					continue;
				}
				// get course code
				// sort list of students in course by name (i.e. alphabetically)
				// see class Registry

			} else if (command.equalsIgnoreCase("SCI")) 
			{
				String courseCode;
				try 
				{
					courseCode = commandLine.next().toUpperCase();
				} 
				catch (Exception e) 
				{
					System.out.println("Expect courseCode");
					continue;
				}
				try
				{
				registry.sortCourseById(courseCode);
				}
				catch(Exception e)
				{
					System.out.println(e);
					continue;
				}
				// get course code
				// sort list of students in course by student id
				// see class Registry
			} 
			else if (command.equalsIgnoreCase("SCH"))
			{
				String courseCode, lectureDay;
				int startTime;
				int duration;
				try
				{
					courseCode = commandLine.next().toUpperCase();
					lectureDay = commandLine.next();
					startTime = commandLine.nextInt();
					duration = commandLine.nextInt();
					scheduler.setDayAndTime(courseCode, lectureDay, startTime, duration);
				}
				catch(Exception e)
				{
					System.out.println(e.getMessage());
					continue;
				}
			}
			else if(command.equalsIgnoreCase("CSCH"))
			{
				String courseCode;
				try
				{
					courseCode = commandLine.next().toUpperCase();
					scheduler.clearSchedule(courseCode);
				}
				catch(Exception e)
				{
					System.out.println(e.getMessage());
				}
			}
			else if(command.equalsIgnoreCase("PSCH"))
			{
				scheduler.printSchedule();
			}
			else if(command.equalsIgnoreCase("ASCH"))
			{
				String courseCode;
				int duration;
				try
				{
					courseCode = commandLine.next().toUpperCase();
					duration = commandLine.nextInt();
					scheduler.autoSetup(courseCode, duration);
				}
				catch(Exception e)
				{
					System.out.println(e.getMessage());
				}
			}
			else 
			{
				System.out.println("Command not exist");
			}
			commandLine.close();
			System.out.println("\n");

		}
		scanner.close();
		}
		catch(Exception e)
		{
			System.out.print(e);
		}
	}

	private static boolean isStringOnlyAlphabet(String str) 
	{
		for (char c : str.toCharArray()) 
		{
			if (!Character.isAlphabetic(c))
				return false;
		}
		// write method to check if string str contains only alphabetic characters
		return true;
	}

	public static boolean isNumeric(String str) 
	{
		for (char c : str.toCharArray()) 
		{
			if (!Character.isDigit(c))
				return false;
		}
		// write method to check if string str contains only numeric characters
		return true;
	}

}