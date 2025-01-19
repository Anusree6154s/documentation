---
layout: post
date: 18 jan 2025
title: Typescript learners guide
excerpt: To study basic and advanced typescript
permalink: typescript-learners-guide
tags: [typescript]
---

To study basic and advanced typescript:

<br>
<br>

### <ins>Table of Contents</ins>

- [Basic](#basic-typescript-concepts)
  1. [Basic Types](#1-basic-types)
  2. [Type Annotations](#2-type-annotations)
  3. [Interfaces](#3-interfaces)
  4. [Classes](#4-classes)
  5. [Enums](#5-enums)
  6. [Functions](#6-functions)
  7. [Arrays and Tuples](#7-arrays-and-tuples)
  8. [Union and Intersection Types](#8-union-and-intersection-types)
  9. [Type Aliases](#9-type-aliases)
  10. [Generics](#10-generics)
  11. [Modules](#11-modules)
  12. [Type Inference](#12-type-inference)
- [Advanced](#advanced-typescript-concepts)
  1. [Advanced Types](#1-advanced-types)
  2. [Type Guards](#2-type-guards)
  3. [Discriminated Unions](#3-discriminated-unions)
  4. [Keyof and Lookup Types](#4-keyof-and-lookup-types)
  5. [Indexed Access Types](#5-indexed-access-types)
  6. [Template Literal Types](#6-template-literal-types)
  7. [Decorators](#7-decorators)
  8. [Declaration Merging](#8-declaration-merging)
  9. [Namespace](#9-namespace)
  10. [Type Manipulation](#10-type-manipulation)
  11. [Module Augmentation](#11-module-augmentation)
  12. [Strict Type Checking](#12-strict-type-checking)
  13. [Advanced Generics](#13-advanced-generics)
  14. [Dynamic Import Types](#14-dynamic-import-types)
  15. [Compiler Configuration](#15-compiler-configuration)
  16. [Advanced Decorator Usage](#16-advanced-decorator-usage)

<br>
<br>

### <ins>Basic Typescript Concepts</ins>

#### 1. **Basic Types**

TypeScript provides a set of basic types for handling data:

##### `string`, `number`, `boolean`

```typescript
let name: string = "Alice";
let age: number = 30;
let isActive: boolean = true;
```

##### `null`, `undefined`, `void`

- `null` and `undefined` represent absence of value.
- `void` is used for functions that don’t return a value.

```typescript
let emptyValue: null = null;
let notAssigned: undefined = undefined;

function logMessage(): void {
  console.log("Hello!");
}
```

##### `any`, `unknown`

- `any` allows any type and essentially disables type checking.
- `unknown` is similar to `any`, but more restrictive, requiring type checking before usage.

```typescript
let anything: any = 42;
anything = "Now a string"; // No error

let uncertain: unknown = 42;
if (typeof uncertain === "string") {
  console.log(uncertain.toUpperCase()); // OK after checking the type
}
```

##### `never`

`never` is used for functions that never return a value, like functions that throw exceptions or enter infinite loops.

```typescript
function throwError(message: string): never {
  throw new Error(message);
}
```

#### 2. **Type Annotations**

Type annotations specify the type of variables, function parameters, and return values explicitly.

```typescript
let x: number = 10; // Type annotation for a number

function greet(name: string): string {
  return `Hello, ${name}`;
}
```

#### 3. **Interfaces**

An interface defines the structure of an object, specifying its properties and methods.

```typescript
interface Person {
  name: string;
  age: number;
  greet(): string;
}

const person: Person = {
  name: "Alice",
  age: 30,
  greet() {
    return `Hello, my name is ${this.name}`;
  },
};
```

#### 4. **Classes**

Classes allow you to define blueprints for objects, including properties and methods.

```typescript
class Animal {
  name: string;
  constructor(name: string) {
    this.name = name;
  }

  speak(): void {
    console.log(`${this.name} makes a sound`);
  }
}

class Dog extends Animal {
  constructor(name: string) {
    super(name);
  }

  speak(): void {
    console.log(`${this.name} barks`);
  }
}

let dog = new Dog("Buddy");
dog.speak(); // Buddy barks
```

##### Access Modifiers

- `public`: Can be accessed from anywhere (default).
- `private`: Can only be accessed within the class.
- `protected`: Can be accessed within the class and subclasses.

```typescript
class User {
  public name: string;
  private password: string;

  constructor(name: string, password: string) {
    this.name = name;
    this.password = password;
  }

  showName() {
    console.log(this.name);
  }
}
```

#### 5. **Enums**

Enums define named constant values. TypeScript supports numeric and string enums.

##### Numeric Enum:

```typescript
enum Direction {
  Up = 1,
  Down,
  Left,
  Right,
}

console.log(Direction.Up); // 1
```

##### String Enum:

```typescript
enum Status {
  Pending = "PENDING",
  InProgress = "IN_PROGRESS",
  Completed = "COMPLETED",
}

console.log(Status.Pending); // "PENDING"
```

#### 6. **Functions**

TypeScript allows specifying types for function parameters and return values. It also supports optional, default, and rest parameters.

##### Parameter Types and Return Types

```typescript
function add(a: number, b: number): number {
  return a + b;
}
```

##### Optional Parameters (`?`)

```typescript
function greet(name: string, age?: number): string {
  return age ? `${name} is ${age} years old` : `${name}`;
}

console.log(greet("Alice")); // Alice
console.log(greet("Bob", 30)); // Bob is 30 years old
```

##### Default Parameters

```typescript
function greet(name: string, age: number = 25): string {
  return `${name} is ${age} years old`;
}
```

##### Rest Parameters (`...args`)

```typescript
function sum(...numbers: number[]): number {
  return numbers.reduce((acc, num) => acc + num, 0);
}

console.log(sum(1, 2, 3, 4)); // 10
```

#### 7. **Arrays and Tuples**

##### Typed Arrays

Arrays can be strongly typed.

```typescript
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ["a", "b", "c"];
```

##### Tuples

Tuples are arrays with fixed sizes and types for each element.

```typescript
let tuple: [string, number] = ["Alice", 30];
```

#### 8. **Union and Intersection Types**

##### Union Types (`|`)

A variable can hold multiple types.

```typescript
function print(value: string | number): void {
  console.log(value);
}

print("Hello");
print(42);
```

##### Intersection Types (`&`)

Combining multiple types into one.

```typescript
interface Person {
  name: string;
  age: number;
}

interface Employee {
  employeeId: string;
  role: string;
}

type EmployeePerson = Person & Employee;

const emp: EmployeePerson = {
  name: "Alice",
  age: 30,
  employeeId: "E123",
  role: "Engineer",
};
```

#### 9. **Type Aliases**

Type aliases allow creating custom types that can be reused across the codebase.

```typescript
type ID = string | number;

function getUser(id: ID): void {
  console.log(`Fetching user with ID: ${id}`);
}

getUser(1);
getUser("abc123");
```

#### 10. **Generics**

Generics allow writing functions, classes, and interfaces that work with any data type, providing more flexibility and reusability.

```typescript
function identity<T>(arg: T): T {
  return arg;
}

let output = identity<string>("Hello");
console.log(output); // Hello

let numberOutput = identity<number>(100);
console.log(numberOutput); // 100
```

##### Generic Classes

```typescript
class Box<T> {
  value: T;
  constructor(value: T) {
    this.value = value;
  }

  getValue(): T {
    return this.value;
  }
}

const stringBox = new Box<string>("Hello");
console.log(stringBox.getValue()); // Hello
```

#### 11. **Modules**

Modules allow code to be split into separate files, which can be imported/exported.

```typescript
// file1.ts
export function greet(name: string): string {
  return `Hello, ${name}`;
}

// file2.ts
import { greet } from "./file1";

console.log(greet("Alice")); // Hello, Alice
```

#### 12. **Type Inference**

TypeScript automatically infers the type of a variable when the type is not explicitly declared.

```typescript
let inferredString = "Hello"; // inferred as string
let inferredNumber = 42; // inferred as number

// TypeScript can infer types from function return values as well
function multiply(x: number, y: number) {
  return x * y; // inferred return type is number
}

let result = multiply(3, 4);
```

Sure! Below is an elaboration on the **Advanced TypeScript** topics you mentioned, along with examples to illustrate each concept.


<br>
<br>

### <ins>Advanced Typescript Concepts</ins>
#### 1. **Advanced Types**

##### **Mapped Types**

Mapped types allow you to create a new type based on an existing one by transforming its properties. You can modify the properties or their types.

Example: Create a `Readonly` type that marks all properties of an object as `readonly`:

```typescript
type Readonly<T> = { readonly [K in keyof T]: T[K] };

interface Person {
  name: string;
  age: number;
}

type ReadonlyPerson = Readonly<Person>;

const person: ReadonlyPerson = { name: "Alice", age: 30 };
// person.name = 'Bob'; // Error: cannot assign to 'name' because it is a read-only property.
```

##### **Conditional Types**

Conditional types use the `extends` keyword to define conditional logic based on the type of a variable.

Example: Check if a type `T` is `string`:

```typescript
type IsString<T> = T extends string ? true : false;

type Test1 = IsString<string>; // true
type Test2 = IsString<number>; // false
```

##### **Utility Types**

TypeScript provides several built-in utility types that help manipulate types.

- **`Partial<T>`**: Makes all properties of `T` optional.
- **`Required<T>`**: Makes all properties of `T` required.
- **`Readonly<T>`**: Makes all properties of `T` read-only.
- **`Pick<T, K>`**: Picks a subset of properties `K` from type `T`.
- **`Omit<T, K>`**: Omits properties `K` from type `T`.

```typescript
interface Person {
  name: string;
  age: number;
  address?: string;
}

type PartialPerson = Partial<Person>; // All properties are optional
type RequiredPerson = Required<Person>; // All properties are required
type NameOnly = Pick<Person, "name">; // Only `name` is picked
type WithoutAddress = Omit<Person, "address">; // `address` is omitted
```



#### 2. **Type Guards**

Type guards help narrow the type within a conditional block using `x is Type` syntax or built-in checks.

##### Custom Type Guard

You can create your own type guards to narrow types based on logic.

```typescript
function isString(value: any): value is string {
  return typeof value === "string";
}

const input: any = "Hello, world!";
if (isString(input)) {
  // TypeScript now knows that `input` is a string here.
  console.log(input.toUpperCase()); // OK
}
```

##### `instanceof` and `typeof`

`instanceof` and `typeof` are used for runtime type checks.

```typescript
class Dog {
  bark() {
    console.log("Woof!");
  }
}

const pet = new Dog();

if (pet instanceof Dog) {
  pet.bark(); // OK, `pet` is now recognized as a `Dog`
}

const value = 42;
if (typeof value === "number") {
  console.log(value.toFixed(2)); // OK
}
```



#### 3. **Discriminated Unions**

Discriminated unions allow for union types that include a tag (discriminant) to help narrow down types.

Example: Different actions for different shapes using a `type` property:

```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; sideLength: number };

function area(shape: Shape): number {
  if (shape.kind === "circle") {
    return Math.PI * shape.radius ** 2;
  } else {
    return shape.sideLength ** 2;
  }
}
```



#### 4. **Keyof and Lookup Types**

`keyof` and lookup types allow you to dynamically access the keys and values of a type.

##### `keyof` Operator

Get the keys of an object type as a union of string literals.

```typescript
interface Person {
  name: string;
  age: number;
}

type Key = keyof Person; // "name" | "age"
```

##### Lookup Types

Access the value of a specific property dynamically.

```typescript
type Value = Person["name"]; // string
```



#### 5. **Indexed Access Types**

Indexed access types allow you to retrieve the type of a property of an object type.

```typescript
interface Person {
  name: string;
  age: number;
}

type NameType = Person["name"]; // string
```



#### 6. **Template Literal Types**

Template literal types allow you to construct types by combining string literals, creating dynamic string types.

```typescript
type Greeting = `Hello, ${string}!`;

const greeting: Greeting = "Hello, Alice!"; // Valid
// const invalidGreeting: Greeting = "Hi, Alice!";  // Error: doesn't match `Hello, ${string}!`
```



#### 7. **Decorators**

Decorators are an experimental feature that allows you to modify the behavior of classes, methods, or properties.

Example: A simple class decorator that logs class creation.

```typescript
function logClass(target: Function) {
  console.log(`${target.name} class is being created!`);
}

@logClass
class MyClass {}

const instance = new MyClass(); // Logs: MyClass class is being created!
```



#### 8. **Declaration Merging**

Declaration merging occurs when multiple declarations of the same type or interface are combined into one.

Example:

```typescript
interface Person {
  name: string;
}

interface Person {
  age: number;
}

const person: Person = {
  name: "Alice",
  age: 30,
}; // Declaration of `Person` is merged
```



#### 9. **Namespace**

Namespaces are used to organize code into logical groups (legacy feature but still used in some scenarios).

```typescript
namespace Shapes {
  export interface Circle {
    radius: number;
  }

  export interface Square {
    sideLength: number;
  }
}

const circle: Shapes.Circle = { radius: 5 };
const square: Shapes.Square = { sideLength: 10 };
```



#### 10. **Type Manipulation**

Advanced type manipulation allows you to infer types using `infer` and perform conditional type transformations.

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

type MyFunction = (x: number, y: number) => string;

type Result = ReturnType<MyFunction>; // string
```



#### 11. **Module Augmentation**

Module augmentation allows you to extend or modify existing modules, adding new functionality.

Example: Augmenting a module to add new properties to an existing interface.

```typescript
// Augmenting a global module or third-party library
declare module "express" {
  interface Request {
    user?: string;
  }
}

// Now you can access `user` property on `Request`
```



#### 12. **Strict Type Checking**

Enable strict type checking options to enforce safer coding practices.

In `tsconfig.json`:

```json
{
  "compilerOptions": {
    "strict": true,
    "strictNullChecks": true,
    "noImplicitAny": true
  }
}
```

`strictNullChecks` ensures that `null` and `undefined` are not assignable to other types by default. `noImplicitAny` disallows variables from being implicitly typed as `any`.



#### 13. **Advanced Generics**

##### Generic Constraints (`T extends U`)

Restrict the types that can be used with generics.

```typescript
function echo<T extends string>(value: T): T {
  return value;
}

echo("Hello"); // OK
// echo(123);  // Error: Argument of type 'number' is not assignable to parameter of type 'string'.
```

##### Default Generic Parameters

You can set default types for generics.

```typescript
function identity<T = string>(value: T): T {
  return value;
}

identity("Hello"); // string
identity(42); // number
```

##### Recursive Generics

Generics can be recursive, allowing more complex types.

```typescript
type List<T> = T | List<T>[];

const stringList: List<string> = ["Alice", ["Bob", "Charlie"]];
```



#### 14. **Dynamic Import Types**

Using `import()` syntax to dynamically load modules at runtime.

```typescript
type Module = typeof import("./module");

async function loadModule() {
  const module = await import("./module");
  module.someFunction(); // Access the dynamically imported function
}
```



#### 15. **Compiler Configuration**

`tsconfig.json` is the configuration file for TypeScript. It lets you set compiler options, such as module resolution, strict settings, and more.

Example `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist"
  }
}
```



#### 16. **Advanced Decorator Usage**

For frameworks like Angular, decorators play an essential role in metadata reflection. This enables functionality such as dependency injection.

Example: An Angular-style decorator for a class:

```typescript
function Injectable(target: Function) {
  console.log(`Injectable: ${target.name}`);
}

@Injectable
class MyService {}
```

##### **Key Use Cases for Advanced Topics**

Advanced TypeScript concepts often come into play when building:

- Frameworks or libraries.
- Complex type-safe APIs.
- Enterprise-level projects requiring strict type safety.
- Integration with JavaScript libraries using type declarations.
