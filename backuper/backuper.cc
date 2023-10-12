#include <cstdlib>
#include <chrono>
#include "date/include/date/date.h"


class Backuper {
private:
  static std::string get_home_directory() {
	return getenv("HOME");
  };

  static std::string get_current_time() {
	return date::format("%F", std::chrono::system_clock::now());
  }

  static std::string make_command(std::string archive,
								  std::string directory) {
	return "tar -cvf " + archive + " " + directory;
  }

public:
  std::string command;
  std::string target_archive = Backuper::get_home_directory() + "/" +
	Backuper::get_current_time() + ".tar";

  void backup() { system(command.c_str()); }

  Backuper(std::string target_directory) {
	command = Backuper::make_command(target_archive, target_directory);
  }
};
