//Xuan Thanh Le
//Student ID: 500962159


// Read from file using scanner
// Demo throw exception with 2 methods printClassList and sortCourseByName  
import java.util.Set;
import java.util.TreeMap;
import java.util.ArrayList;
import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class Registry 
{
	private TreeMap<String,Student> students = new TreeMap<String, Student>();
	private TreeMap<String,ActiveCourse> courses = new TreeMap<String, ActiveCourse>();

	public Registry() 
	{
		// implements Scanner to read from file students.txt
		File studentFile = new File("students.txt");
		try 
		{

			Scanner sc = new Scanner(studentFile);

			while (sc.hasNextLine()) 
			{
				String st = sc.nextLine();
				String[] result = st.split(",");
				students.put(result[0], new Student(result[1], result[0]));
			}
			sc.close();
		} catch (FileNotFoundException e) 
		{
			e.printStackTrace();
		}

		Student s1 = students.get("34562");
		Student s2 = students.get("38467");
		Student s3 = students.get("98345");
		Student s4 = students.get("57643");
		Student s5 = students.get("25347");
		Student s6 = students.get("46532");

		ArrayList<Student> list = new ArrayList<Student>();
		ArrayList<ArrayList<Student>> list2 = new ArrayList<ArrayList<Student>>();
		list.add(s2);
		list.add(s3);
		list.add(s4);
		list2.add(list);
		list = new ArrayList<Student>();
		list.add(s1);
		list.add(s5);
		list.add(s6);
		list2.add(list);
		list = new ArrayList<Student>();
		list.add(s1);
		list.add(s2);
		list.add(s4);
		list.add(s6);
		list2.add(list);

		// implements Scanner to read from file courses.txt
		File courseFile = new File("courses.txt");
		try 
		{
			Scanner sc2 = new Scanner(courseFile);
			int i = 0;
			while (sc2.hasNextLine()) 
			{
				String line = sc2.nextLine();
				String[] coursesInfo = line.split(",");
				String courseName = coursesInfo[0];
				String courseCode = coursesInfo[1];
				String descr = coursesInfo[2];
				String format = coursesInfo[3];
				String semester = coursesInfo[4];
				ArrayList<Student> courseList = list2.get(i);
				courses.put(coursesInfo[1], new ActiveCourse(courseName, courseCode, descr, format, semester, courseList));
				for (Student s : courseList) 
				{
					s.addCourse(courseName, courseCode, descr, format, semester, 0);
				}
				i++;
			}
			sc2.close();
		} catch (FileNotFoundException e) 
		{
			System.out.println("File course.txt not found");
		}
	}

	public TreeMap<String, ActiveCourse> getCourses()
	{
		return courses;
	}
	// Add new student to the registry (students arraylist above)
	public boolean addNewStudent(String name, String id) 
	{
		Student st = new Student(name, id);
		if (students.containsKey(st.getId()))
		{
			System.out.println("Student " + st.getName() + " already registered");
			return false;
		}
		students.put(st.getId(), st);
		System.out.println("Succeeded!");
		// Create a new student object
		// check to ensure student is not already in registry
		// if not, add them and return true, otherwise return false
		// make use of equals method in class Student
		return true;
	}

	// Remove student from registry
	public boolean removeStudent(String studentId) 
	{
		if (students.containsKey(studentId))
		{
			students.remove(studentId);
			return true;
		}
		// Find student in students arraylist
		// If found, remove this student and return true
		return false;
	}

	// Print all registered students
	public void printAllStudents() 
	{
		Set<String> ids = students.keySet();
		for (String id: ids) 
		{
			System.out.println("ID: " + id + " Name: " + students.get(id).getName());
		}

	}

	// Given a studentId and a course code, add student to the active course
	public void addCourse(String studentId, String courseCode) throws Exception
	{
		if(students.containsKey(studentId)) 
		{
			Student s = students.get(studentId);
				Set<String> cc = s.courses.keySet();
				for (String c: cc) 
				{
					if (s.courses.get(c).getActive()) 
					{
						if (courses.containsKey(courseCode)) 
						{
							System.out.print("Student already registered to this course");
							return;
						}
					}
				}
				if (courses.containsKey(courseCode)) 
				{
					ActiveCourse ac = courses.get(courseCode);
					s.addCourse(ac.getName(), ac.getCode(), ac.getDescription(), ac.getFormat(), ac.getSemester(),
							0);
					ac.addStudents(s);
						return;
				}
				else
				{
					throw new Exception("Student ID not found") ;
				}
				
		}
		else
		{
			throw new Exception("CourseCode not found"); 
		}		
		// Find student object in registry (i.e. students arraylist)
		// Check if student has already taken this course in the past Hint: look at
		// their credit course list
		// If not, then find the active course in courses array list using course code
		// If active course found then check to see if student already enrolled in this
		// course
		// If not already enrolled
		// add student to the active course
		// add course to student list of credit courses with initial grade of 0
	}

	// Given a studentId and a course code, drop student from the active course
	public void dropCourse(String studentId, String courseCode) throws Exception
	{
	if (courses.containsKey(courseCode)) 
	{
		if (students.containsKey(studentId)) 
		{
					students.get(studentId).removeActiveCourse(courseCode);
		}
		else
		{
			throw new Exception("Student ID not found");
		}

		courses.get(courseCode).removeStudent(studentId);
	}
	else
	{
		throw new Exception("CourseCode not found");
	}	
		// Find the active course
		// Find the student in the list of students for this course
		// If student found:
		// remove the student from the active course
		// remove the credit course from the student's list of credit courses
	}

	// Print all active courses
	public void printActiveCourses() 
	{
		for (String courseCode: courses.keySet()) 
		{
			System.out.println(courses.get(courseCode).getCourseDescription());
		}
	}

	// Print the list of students in an active course
	// Throw Exception when CourseCode not found
	public void printClassList(String courseCode) throws Exception 
	{ 
		if (courses.containsKey(courseCode)) 
		{
			for (Student st : courses.get(courseCode).getStudents()) 
			{
				System.out.println(st.toString());
			}
		}
		else
		{
			throw new Exception("CourseCode not found");
		}
	}

	// Given a course code, find course and sort class list by student name
	// Throw Exception when CourseCode not found
	public void sortCourseByName(String courseCode) throws Exception 
	{
		if (courses.containsKey(courseCode)) 
		{
			courses.get(courseCode).sortByName();
		}
		
		else 
		{
			throw new Exception("CourseCode not found");
		}
	}

	// Given a course code, find course and sort class list by student id
	public void sortCourseById(String courseCode)  throws Exception
	{
		if (courses.containsKey(courseCode))
		{
			courses.get(courseCode).sortById();
		}
		
		else
		{
			throw new Exception("CourseCode not found");
		}
	}

	// Given a course code, find course and print student names and grades
	public void printGrades(String courseCode) throws Exception
	{
		if (courses.containsKey(courseCode)) 
			{
				courses.get(courseCode).printGrades();
			}
		else
		{
			throw new Exception("CourseCode not found");
		}
	}

	// Given a studentId, print all active courses of student
	public void printStudentCourses(String studentId) throws Exception
	{
		if (students.containsKey(studentId)) 
			{
				students.get(studentId).printActiveCourses();
			}
		else
		{
			throw new Exception("Student ID not found");
		}
	}

	// Given a studentId, print all completed courses and grades of student
	public void printStudentAlphabetTranscript(String studentId) throws Exception
	{
		if (students.containsKey(studentId)) 
		{
			students.get(studentId).printAlphabetTranscript();
		}
		else
		{
			throw new Exception("Student ID not found");
		}
	}

	// Given a course code, student id and numeric grade
	// set the final grade of the student
	public void setFinalGrade(String courseCode, String studentId, double grade) throws Exception
	{
		if (courses.containsKey(courseCode)) 
		{
			if (students.containsKey(studentId)) 
			
			{
				if(students.get(studentId).courses.containsKey(courseCode))	
				
				{
					CreditCourse cc = students.get(studentId).courses.get(courseCode);
					cc.grade = grade;
					cc.setInactive();
					
				}
				
				else
				{
					throw new Exception("CourseCode not found in CreditCourse");
				}
			}
			
			else
			{
				throw new Exception("Student ID not found");
			}
		}
		else
		{
			throw new Exception("Course Code not found");
		}

			// find the active course
			// If found, find the student in class list
			// then search student credit course list in student object and find course
			// set the grade in credit course and set credit course inactive
	}

	// given student id, print description of all courses the students are in
	public void printCreditCourses(String studentId) throws Exception
	{
		if (students.containsKey(studentId)) 
			{
				Set<String> cc = students.get(studentId).courses.keySet();
				for (String c: cc) 
				{
					System.out.println(students.get(studentId).courses.get(c).getDescription());
				}
			}
		else
		{
			throw new Exception("Student ID not found");
		}
	}
	
}
