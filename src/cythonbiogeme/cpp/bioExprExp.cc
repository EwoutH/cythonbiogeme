//-*-c++-*------------------------------------------------------------
//
// File name : bioExprExp.cc
// @date   Tue Apr 17 12:13:00 2018
// @author Michel Bierlaire
// @version Revision 1.0
//
//--------------------------------------------------------------------

#include "bioExprExp.h"
#include "bioExceptions.h"
#include "bioDebug.h"
#include "bioConstants.h"
#include <cmath>
#include <sstream> 

bioExprExp::bioExprExp(bioExpression* c) :
  child(c) {

  listOfChildren.push_back(c) ;
}

bioExprExp::~bioExprExp() {

}

const bioDerivatives* bioExprExp::getValueAndDerivatives(std::vector<bioUInt> literalIds,
							 bioBoolean gradient,
							 bioBoolean hessian) {

  theDerivatives.with_g = gradient ;
  theDerivatives.with_h = hessian ;

  bioUInt n = literalIds.size() ;
  theDerivatives.resize(n) ;

  const bioDerivatives* childResult = child->getValueAndDerivatives(literalIds,gradient,hessian) ;
  if (childResult->f <= constants::log_sqrt_max_float()) {
    theDerivatives.f = exp(childResult->f) ;
    if (gradient) {
      for (bioUInt i = 0 ; i < n ; ++i) {
        theDerivatives.g[i] = theDerivatives.f * childResult->g[i] ;
        if (hessian) {
	      for (bioUInt j = 0 ; j < n ; ++j) {
	        theDerivatives.h[i][j] =
	        theDerivatives.f *
	        (
	            childResult->h[i][j] +
	            childResult->g[i] * childResult->g[j]
	        );
	      }
        }
      }
    }
    theDerivatives.dealWithNumericalIssues() ;
    return &theDerivatives ;
  }

  static const bioReal sqrt_max_float = constants::get_sqrt_max_float();
  theDerivatives.f = sqrt_max_float ;
    if (gradient) {
        for (bioUInt i = 0 ; i < n ; ++i) {
          theDerivatives.g[i] = sqrt_max_float ;
          if (hessian) {
            theDerivatives.h[i][i] = sqrt_max_float ;
            for (bioUInt j = i+1 ; j < n ; ++j) {
                theDerivatives.h[i][j] = theDerivatives.h[j][i] = sqrt_max_float ;
            }
          }
        }
    }

    return &theDerivatives ;
  }


bioString bioExprExp::print(bioBoolean hp) const {
  std::stringstream str ; 
  str << "exp(" << child->print(hp) << ")";
  return str.str() ;

}
