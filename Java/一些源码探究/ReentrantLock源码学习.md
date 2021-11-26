学习ReentrantLock之前，先了解一下可重入锁的概念。何为可重入锁，顾名思义，就是可重入的。真是听君一席话，胜听一席话啊。

![img](ReentrantLock源码学习.assets/22C3A36F.jpg)

正经点，可重入锁就是能够支持**同一个线程**对资源的**重复**加锁。注意两个关键字：同一线程和重复。

像synchronized关键字也实现了可重入。用synchronized修饰的方法，在进行递归调用时，执行线程在获取了锁之后仍然能够连续多次获得该锁，并不会出现阻塞的情况。

再比如说，这篇文章要学习的`ReentrantLock`，也实现了可重入锁。并且`ReentrantLock`还支持公平锁和非公平锁（默认是非公平锁）。

#### 1、ReentrantLock源码学习

##### 1.1 构造方法

`ReentrantLock`的源码比较简单，并且它也是基于AQS实现的。先看看它的构造函数

```java
    /**
     * Creates an instance of {@code ReentrantLock}.
     * This is equivalent to using {@code ReentrantLock(false)}.
     */
    public ReentrantLock() {
        sync = new NonfairSync();
    }

    /**
     * Creates an instance of {@code ReentrantLock} with the
     * given fairness policy.
     *
     * @param fair {@code true} if this lock should use a fair ordering policy
     */
    public ReentrantLock(boolean fair) {
        sync = fair ? new FairSync() : new NonfairSync();
    }
```

默认就是非公平锁。

##### 1.2 锁的释放

`Sync`类就是继承自AQS的，`FairSync`类和`NonfairSync`类又是继承自`Sync`。对于公平锁和非公平锁，其释放锁的逻辑都是一样的，所以在`Sync`类中实现。

```java
    abstract static class Sync extends AbstractQueuedSynchronizer {
        protected final boolean tryRelease(int releases) {
            int c = getState() - releases;
            // 判断当前线程是不是占有锁的线程，如果不是，抛异常
            if (Thread.currentThread() != getExclusiveOwnerThread())
                throw new IllegalMonitorStateException();
            boolean free = false;
            // 同步变量state的值为0时，才释放锁，返回true
            if (c == 0) {
                free = true;
                setExclusiveOwnerThread(null);
            }
            // 设置同步变量的值
            setState(c);
            return free;
        }
    }
```

可以发现可重入锁的释放逻辑，对于占有锁的线程来说，只有在同步变量state的值为0的时候，才算是释放了锁。

##### 1.3 锁的获取

锁的获取分公平锁和非公平锁。非公平锁的获取逻辑实现在`Sync`类中

```java
abstract static class Sync extends AbstractQueuedSynchronizer {
        /**
         * Performs non-fair tryLock.  tryAcquire is implemented in
         * subclasses, but both need nonfair try for trylock method.
         * 非公平锁，获取锁
         */
        final boolean nonfairTryAcquire(int acquires) {
            final Thread current = Thread.currentThread();
            int c = getState();
            // 同步变量为0，说明没有线程占用锁
            if (c == 0) {
                // CAS获取锁，注意这里并没有判断该线程是不是同步队列的队头
                if (compareAndSetState(0, acquires)) {
                    setExclusiveOwnerThread(current);
                    return true;
                }
            }
            // 判断当前线程是不是占有锁的线程
            else if (current == getExclusiveOwnerThread()) {
                // 增加同步变量state的值
                int nextc = c + acquires;
                if (nextc < 0) // overflow
                    throw new Error("Maximum lock count exceeded");
                setState(nextc);
                return true;
            }
            return false;
        }
    }
```

可以发现`Sync`类似并没有重写AQS的`tryAcquire`方法，而是放到了它的子类`FairSync`类和`NonfairSync`类中去实现的。

看看`NonfairSync`类的源码

```java
    // 非公平锁
    static final class NonfairSync extends Sync {
        private static final long serialVersionUID = 7316153563782823691L;

        // 上来先CAS获取一下锁，如果获取失败，再调用AQS的acquire方法
        final void lock() {
            if (compareAndSetState(0, 1))
                setExclusiveOwnerThread(Thread.currentThread());
            else
                acquire(1);
        }
		// 调用Sync类的nonfairTryAcquire方法
        protected final boolean tryAcquire(int acquires) {
            return nonfairTryAcquire(acquires);
        }
    }
```

看看`FairSync`类的源码

```java
    // 公平锁
    static final class FairSync extends Sync {
        private static final long serialVersionUID = -3000897897090466540L;
		// 直接调用AQS的acquire方法
        final void lock() {
            acquire(1);
        }

        /**
         * Fair version of tryAcquire.  Don't grant access unless
         * recursive call or no waiters or is first.
         */
        protected final boolean tryAcquire(int acquires) {
            final Thread current = Thread.currentThread();
            int c = getState();
            // 同步变量为0，说明没有线程占有锁
            if (c == 0) {
                /**
                 * 判断同步队列中当前节点是否有前驱节点，也就是只有当前节点是头结点并且CAS成功的情况下，当
                 * 前线程才能占有锁
                 */
                if (!hasQueuedPredecessors() &&
                    compareAndSetState(0, acquires)) {
                    setExclusiveOwnerThread(current);
                    return true;
                }
            }
            // 当前线程已经占有锁，则增加state变量的值
            else if (current == getExclusiveOwnerThread()) {
                int nextc = c + acquires;
                if (nextc < 0)
                    throw new Error("Maximum lock count exceeded");
                setState(nextc);
                return true;
            }
            return false;
        }
    }
```

可以发现公平锁和非公平锁在获取锁的时候，唯一的差别就是公平锁判断了当前节点是不是头结点，只有是头结点的情况下才可能获取到锁。非公平锁就不一样了，上来就直接CAS。

上面的方法都是在`ReentrantLock`类内部用的，对外提供的接口如下

```java
// 获取锁，在等待获取锁的过程中休眠并禁止一切线程调度
public void lock() {
    sync.lock();
}

// 在等待获取锁的过程中可被中断
public void lockInterruptibly() throws InterruptedException {
    sync.acquireInterruptibly(1);
}

// 尝试获取锁，获取到锁并返回true；获取不到并返回false
public boolean tryLock() {
    return sync.nonfairTryAcquire(1);
}

// 在指定时间内等待获取锁；过程中可被中断
public boolean tryLock(long timeout, TimeUnit unit)
    throws InterruptedException {
    return sync.tryAcquireNanos(1, unit.toNanos(timeout));
}

// 释放锁
public void unlock() {
    sync.release(1);
}
```

#### 2、测试

测试一下`ReentrantLock`的公平锁和非公平锁。

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.locks.ReentrantLock;

public class FairAndUnfairTest {

    private static Sync fairLock = new Sync(true);
    private static Sync noFairLock = new Sync(false);

    public static void testLock(Sync lock) {
        // 开启5个线程
        for (int i = 0; i < 5; i++) {
            new Thread(new Job(lock), String.valueOf(i)).start();
        }
    }

    private static class Job extends Thread {
        private Sync lock;
        public Job(Sync lock) {
            this.lock = lock;
        }

        public void run() {
            for (int i = 0; i < 2; i++) {
                lock.lock();
                System.out.println("locked by " + currentThread().getName() + ", waiting by " + lock.getQueueThreads());
                lock.unlock();
            }
        }
    }

    private static class Sync extends ReentrantLock {
        public Sync(boolean fair) {
            super(fair);
        }

        /**
         * 获取等待队列
         * @return
         */
        public List<String> getQueueThreads() {
            List<Thread> arrayList = new ArrayList<Thread>(super. getQueuedThreads());
            Collections.reverse(arrayList);
            List<String> list = new ArrayList<>();
            arrayList.forEach(el -> {
                list.add(el.getName());
            });
            return list;
        }
    }

    public static void main(String[] args) {
        //testLock(fairLock);
        testLock(noFairLock);
    }
}
```

公平锁输出如下

```java
locked by 0, waiting by [1, 2]
locked by 1, waiting by [2, 4, 3, 0]
locked by 2, waiting by [4, 3, 0, 1]
locked by 4, waiting by [3, 0, 1, 2]
locked by 3, waiting by [0, 1, 2, 4]
locked by 0, waiting by [1, 2, 4, 3]
locked by 1, waiting by [2, 4, 3]
locked by 2, waiting by [4, 3]
locked by 4, waiting by [3]
locked by 3, waiting by []
```

非公平锁输出如下

```java
locked by 0, waiting by [2]
locked by 0, waiting by [2, 3, 1, 4]
locked by 2, waiting by [3, 1, 4]
locked by 2, waiting by [3, 1, 4]
locked by 3, waiting by [1, 4]
locked by 3, waiting by [1, 4]
locked by 1, waiting by [4]
locked by 1, waiting by [4]
locked by 4, waiting by []
locked by 4, waiting by []
```

可以发现公平锁总是按照顺序来依次获取锁。而非公平锁却是连续获取。回顾`nonfairTryAcquire(int acquires)`方法，当一 个线程请求锁时，只要获取了同步状态即成功获取锁。在这个前提下，刚释放锁的线程再次获取同步状态的几率会非常大，使得其他线程只能在同步队列中等待。

非公平锁可能会出现**线程饥饿**的情况，当竞争的线程很多时，后面的线程可能一直都获取不到锁。那为啥`ReentrantLock`默认是非公平锁呢？经过上面的测试可以发现，在公平锁的情况下，线程进行了10次上下文切换，非公平锁情况下只进行了5次。

线程上下文切换是一个耗费时间和资源的操作，所以在线程竞争激烈的情况下，非公平锁无疑能够节省很多的资源。

总结一下就是：公平性锁保证了锁的获取按照FIFO原则，而代价是进行大量的线程切换。非公平性锁虽然可能造成线程“饥饿”，但极少的线程切换，保证了其更大的吞吐量。