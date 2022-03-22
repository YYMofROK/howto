## [JAVA]오버로딩이란..?
>
>  - CLASS 안에서 이름이 동일한 복수의 METHOD 를 정의하여 사용하는 방법
>  >
>  >```
>  > // EX.01)------------------------------------------
>  >class A {
>  >	public function println(){...}
>  >	public function println(boolean x){...}
>  >	public function println(char x){...}
>  >	public function println(char[] x){...}
>  >	public function println(double x){...}
>  >	public function println(float x){...}
>  >	public function println(int x){...}
>  >	public function println(long x){...}
>  >	public function println(Object x){...}
>  >	public function println(String x){...}
>  >}
>  >```
> - 위 EX.01 에서 모든 METHOD의 이름은 같다. => "public function println()"
> 
> - 위 EX.01 에서 모든 METHOD 는 다른 호출 매개변수형태( 시그니처 )를 가진다.
> 
>   실행시 전달반은 매개변수의 타입( 시그니처 )에 따라 적절한 METHOD를 호출하게 된다.
>
