//Xuan Thanh Le
//Student ID: 500962159
import java.util.TreeMap;
import java.util.Set;

// Make class Student implement the Comparable interface
// Two student objects should be compared by their name
public class Student 
{
  private String name; 
  private String id; 
  public  TreeMap<String, CreditCourse> courses; 

  public Student(String name, String id) 
  {
    this.name = name; 
    this.id = id; 
    courses = new TreeMap <String, CreditCourse > (); 
  }

  // get student id
  public String getId() 
  {
    return id; 
  }

  // get student name
  public String getName() 
  {
    return name; 
  }

  // add a credit course to list of courses for this student
  public void addCourse(String courseName, String courseCode, String descr, String format, String sem, double grade) 
  {
    CreditCourse cc = new CreditCourse(courseName, courseCode, descr, format, sem, grade); 
    cc.setActive(); 
    courses.put(courseCode, cc); 
    // create a CreditCourse object
    // set course active
    // add to courses array list
  }

  // get the final grade of student
  public double getStudentGrade() 
  {
    Set<String> cc = courses.keySet();
    for (String c: cc) 
    {
      if (courses.get(c).getActive() == false) 
      {
        return courses.get(c).getGrade(); 
      }
    }
    return 0; 
  }

  // Prints a student transcript
  // Prints all completed (i.e. non active) courses for this student (course code,
  // course name,
  // semester, letter grade
  // see class CreditCourse for useful methods
  // print Alphabetic transcript of students.
  public void printAlphabetTranscript() 
  {
    boolean complete = false;
    for (String c: courses.keySet()) 
    {
      if (!courses.get(c).getActive()) 
      { 
        complete = true;
        System.out.print(courses.get(c).displayAlphabetGrade()); 
      }
    }
    if (!complete) 
    {
      System.out.println("This student hasn't complete any course"); 
    }
  }

  // Prints all active courses this student is enrolled in
  // see variable active in class CreditCourse
  public void printActiveCourses() 
  {
    for (String c: courses.keySet()) 
    {
      if (courses.get(c).getActive()) 
      {
        System.out.println(courses.get(c)); 
      }
    }
  }

  // Drop a course (given by courseCode)
  // Find the credit course in courses arraylist above and remove it
  // only remove it if it is an active course
  public void removeActiveCourse(String courseCode) 
  {
     if (courses.containsKey(courseCode)) 
      {
        courses.remove(courseCode); 
      }
  }

  public String toString() 
  {
    return "Student ID: " + id + " Name: " + name; 
  }

  // override equals method inherited from superclass Object
  // if student names are equal *and* student ids are equal (of "this" student
  // and "other" student) then return true
  // otherwise return false
  // Hint: you will need to cast other parameter to a local Student reference
  // variable
  @Override
  public boolean equals(Object other) 
  {
    Student s = (Student)other; 
    return this.name.equals(s.getName()) && this.id.equals(s.getId()); 
  }
}
