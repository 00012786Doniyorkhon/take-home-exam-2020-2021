// primitive sorting - bubble sort
function bubbleSort(arr){
   var len = arr.length;
   for (var i = len-1; i>=0; i--){
     for(var j = 1; j<=i; j++){
       if(arr[j-1]>arr[j]){
           var temp = arr[j-1];
           arr[j-1] = arr[j];
           arr[j] = temp;
        }
     }
   }
   return arr;
}

// ID number + 4,5,3,2,7
var arr = [4,5,2,3,7,1,2,7,8,6];

// sorted number array
var sorted_arr = bubbleSort(arr);

// binary search algorithm
var binarySearch = (array, target) => {
  let startIndex = 0;
  let endIndex = array.length - 1;
  let i = 0;
  while(startIndex <= endIndex) {
    let middleIndex = Math.floor((startIndex + endIndex) / 2);
    if(target === array[middleIndex]) {
      return console.log("Target was found at index " + middleIndex + ", iteration " + i);
    }
    if(target > array[middleIndex]) {
      console.log("Searching the right side of Array")
      startIndex = middleIndex + 1;
    }
    if(target < array[middleIndex]) {
      console.log("Searching the left side of array")
      endIndex = middleIndex - 1;
    }
    else {
      console.log("Not Found this loop iteration. Looping another iteration.")
    }
    ++i;
  }
  
  console.log("Target value not found in array");
}

binarySearch(sorted_arr, 8);