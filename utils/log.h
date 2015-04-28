#ifndef MINI_LOG_H_
#define MINI_LOG_H_

#include <stdio.h>
#include <sstream>

class Log {
public:
	Log(const char *func, const char *file, int line) {
		ss << "LOG ( " << file << ":" << line << " ) ";
	}
	~Log() { fprintf(stderr, "%s\n", ss.str().c_str()); }	
	inline std::ostream &stream() { return ss; }
private:
	std::ostringstream ss;
};

#define LOG Log(__func__, __FILE__, __LINE__).stream()
#endif
