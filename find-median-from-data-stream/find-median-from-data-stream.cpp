class MedianFinder {
public:
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if(maxHeap.empty()){
            maxHeap.push(num);
        }
        else{
            if(num > maxHeap.top()){
                minHeap.push(num);
            }else{
                maxHeap.push(num);
            }
        }
        
        while(maxHeap.size() > minHeap.size()+1){
            int top = maxHeap.top();
            maxHeap.pop();
            minHeap.push(top);
        }
        
        while(minHeap.size() > maxHeap.size()){
            int top = minHeap.top();
            minHeap.pop();
            maxHeap.push(top);
        }
        
    }
    
    double findMedian() {
        if(minHeap.size() == maxHeap.size()){
            return (minHeap.top() + maxHeap.top()) / 2.0;
        }
        else{
            return maxHeap.top();
        }
        
    }
};
​
/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
