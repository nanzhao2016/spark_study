name := "word-count"

version := "0.0.1"

pythonVersion := "3.5.2"

// additional libraries
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "1.6.2" % "provided"
)
