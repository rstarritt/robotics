#include "../flite-1.4-release/include/flite.h"
register_cmu_us_kal();
int main(int argc, char **argv){
	cst_voice *v;
	if (argc != 2){
		fprintf(stderr,"usage: flite_test FILE\n");
		exit(-1);
	}
	flite_init();
	v = register_cmu_us_kal(NULL);
	flite_file_to_speech(argv[1],v,"play");
}