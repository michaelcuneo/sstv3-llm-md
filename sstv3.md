# What is SST

SST is a framework that makes it easy to build modern full-stack applications on your own infrastructure.
SST supports over 150 providers. Check out the [full list](https://sst.dev/docs/all-providers#directory).
What makes SST different is that your _entire_ app is **defined in code** — in a single `sst.config.ts` file. This includes databases, buckets, queues, Stripe webhooks, or any one of **150+ providers**.
With SST, **everything is automated**.
* * *

## [Components](https://sst.dev/docs/#components)

You start by defining parts of your app, _**in code**_.
For example, you can add your frontend and set the domain you want to use.

* [Next.js](https://sst.dev/docs/#tab-panel-18)
* [Remix](https://sst.dev/docs/#tab-panel-19)
* [Astro](https://sst.dev/docs/#tab-panel-20)
* [Svelte](https://sst.dev/docs/#tab-panel-21)
* [Solid](https://sst.dev/docs/#tab-panel-22)

sst.config.ts

```typescript

new sst.aws.Nextjs("MyWeb", {

domain: "my-app.com"

});

```

sst.config.ts

```typescript


new sst.aws.Remix("MyWeb", {




domain: "my-app.com"



});

```

sst.config.ts

```typescript

new sst.aws.Astro("MyWeb", {

domain: "my-app.com"

});

```

sst.config.ts

```typescript


new sst.aws.SvelteKit("MyWeb", {




domain: "my-app.com"



});

```

sst.config.ts

```typescript

new sst.aws.SolidStart("MyWeb", {

domain: "my-app.com"

});

```

Just like the frontend, you can configure backend features _in code_.
Like your API deployed in a container. Or any Lambda functions, Postgres databases, S3 Buckets, or cron jobs.

* [Containers](https://sst.dev/docs/#tab-panel-23)
* [Functions](https://sst.dev/docs/#tab-panel-24)
* [Postgres](https://sst.dev/docs/#tab-panel-25)
* [Bucket](https://sst.dev/docs/#tab-panel-26)
* [Cron](https://sst.dev/docs/#tab-panel-27)

sst.config.ts

```typescript


const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


loadBalancer: {



ports: [{ listen: "80/http" }]



}


});

```

sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

handler: "src/lambda.handler"

});

```

sst.config.ts

```typescript


new sst.aws.Postgres("MyDatabase", { vpc });


```

sst.config.ts

```typescript

new sst.aws.Bucket("MyBucket");

```

sst.config.ts

```typescript


new sst.aws.Cron("MyCronJob", {




job: "src/cron.handler",




schedule: "rate(1 minute)"



});

```

You can even set up your Stripe products in code.
sst.config.ts

```typescript

new stripe.Product("MyStripeProduct", {

name: "SST Paid Plan",

description: "This is how SST makes money",

});

```

You can check out the full list of components in the sidebar.
* * *

## [Infrastructure](https://sst.dev/docs/#infrastructure)

The above are called **Components**. They are a way of defining the features of your application in code. You can define any feature of your application with them.
In the above examples, they create the necessary infrastructure in your AWS account. All without using the AWS Console.
Learn more about [Components](https://sst.dev/docs/components/).
* * *

### [Configure](https://sst.dev/docs/#configure)

SST’s components come with sensible defaults designed to get you started. But they can also be configured completely.
For example, the `sst.aws.Function` can be configured with all the common Lambda function options.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




handler: "src/lambda.handler",




timeout: "3 minutes",




memory: "1024 MB"



});

```

But with SST you can take it a step further and transform how the Function component creates its low level resources. For example, the Function component also creates an IAM Role. You can transform the IAM Role using the `transform` prop.
sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

handler: "src/lambda.handler",

transform: {

role: (args)=> ({

name: `${args.name}-MyRole`

})

}

});

```

Learn more about [transforms](https://sst.dev/docs/components#transforms).
* * *

### [Providers](https://sst.dev/docs/#providers)

SST has built-in components for AWS and Cloudflare that make these services easier to use.
However it also supports components from any one of the **150+ Pulumi/Terraform providers**. For example, you can use Vercel for your frontends.
sst.config.ts

```typescript


new vercel.Project("MyFrontend", {




name: "my-nextjs-app"



});

```

Learn more about [Providers](https://sst.dev/docs/providers) and check out the full list in the [Directory](https://sst.dev/docs/all-providers#directory).
* * *

## [Link resources](https://sst.dev/docs/#link-resources)

Once you’ve added a couple of features, SST can help you link them together. This is great because you **won’t need to hardcode** anything in your app.
Let’s say you are deploying an Express app in a container and you want to upload files to an S3 bucket. You can `link` the bucket to your container.
sst.config.ts

```typescript

const bucket = newsst.aws.Bucket("MyBucket");

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

new sst.aws.Service("MyService", {

cluster,

link: [bucket],

loadBalancer: {

ports: [{ listen: "80/http" }]

}

});

```

You can then use SST’s [SDK](https://sst.dev/docs/reference/sdk/) to access the S3 bucket in your Express app.
index.mjs```

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

```

Learn more about [resource linking](https://sst.dev/docs/linking/).
* * *

## [Project structure](https://sst.dev/docs/#project-structure)

We’ve looked at a couple of different types of files. Let’s take a step back and see what an SST app looks like in practice.
* * *

### [Drop-in mode](https://sst.dev/docs/#drop-in-mode)

The simplest way to run SST is to use it as a part of your app. This is called _drop-in mode_. For example, if you are building a Next.js app, you can add a `sst.config.ts` file to the root.

```

my-nextjs-app

├─ next.config.js

├─ sst.config.ts

├─ package.json

├─ app

├─ lib

└─ public

```

View an
* * *

### [Monorepo](https://sst.dev/docs/#monorepo)

Alternatively, you might use SST in a monorepo. This is useful because most projects have a frontend, a backend, and some functions.
In this case, the `sst.config.ts` is still in the root but you can split it up into parts in the `infra/` directory.

```

my-sst-app

├─ sst.config.ts

├─ package.json

├─ packages

│  ├─ functions

│  ├─ frontend

│  ├─ backend

│  └─ core

└─ infra

```

Learn more about our [monorepo setup](https://sst.dev/docs/set-up-a-monorepo/).
* * *

## [CLI](https://sst.dev/docs/#cli)

To make this all work, SST comes with a [CLI](https://sst.dev/docs/reference/cli/). You can install it as a part of your Node project.
Terminal window```

npminstallsst

```

Or if you are not using Node, you can install it globally.
Terminal window```

curl-fsSLhttps://sst.dev/install|bash

```

Learn more about the [CLI](https://sst.dev/docs/reference/cli/).
* * *

### [Dev](https://sst.dev/docs/#dev)

The CLI includes a `dev` command that starts a local development environment.
Terminal window```

sstdev

```

This brings up a _multiplexer_ that:

  1. Starts a watcher that deploys any infrastructure changes.
  2. Runs your functions [_Live_](https://sst.dev/docs/live/), letting you make and test changes without having to redeploy them.
  3. Creates a [_tunnel_](https://sst.dev/docs/reference/cli#tunnel) to connect your local machine to any resources in a VPC.
  4. Starts your frontend and container services in dev mode and links it to your infrastructure.

The `sst dev` CLI makes it so that you won’t have to start your frontend or container applications separately. Learn more about [`sst dev`](https://sst.dev/docs/reference/cli/#dev).
* * *

### [Deploy](https://sst.dev/docs/#deploy)

When you’re ready to deploy your app, you can use the `deploy` command.
Terminal window```

sstdeploy--stageproduction

```

* * *

#### [Stages](https://sst.dev/docs/#stages)

The stage name is used to namespace different environments of your app. So you can create one for dev.
Terminal window```

sstdeploy--stagedev

```

Or for a pull request.
Terminal window```

sstdeploy--stagepr-123

```

Learn more about [stages](https://sst.dev/docs/reference/cli#stage).
* * *

## [Console](https://sst.dev/docs/#console)

Once you are ready to go to production, you can use the [SST Console](https://sst.dev/docs/console/) to **auto-deploy** your app, create **preview environments** , and **monitor** for any issues.
![SST Console](https://sst.dev/_astro/sst-console-home.-pMOaf_T_hPeMB.webp)
Learn more about the [Console](https://sst.dev/docs/console/).
* * *

## [FAQ](https://sst.dev/docs/#faq)

Here are some questions that we frequently get.
* * *
**Is SST open-source if it’s based on Pulumi and Terraform?**
SST uses Pulumi behind the scenes for the providers and the deployment engine. And Terraform’s providers are _bridged_ through Pulumi.
SST only relies on the open-source parts of Pulumi and Terraform. It does not require a Pulumi account and all the data about your app and its resources stay on your side.
* * *
**How does SST compare to CDK for Terraform or Pulumi?**
Both CDKTF and Pulumi allow you to define your infrastructure using a programming language like TypeScript. SST is also built on top of Pulumi. So you might wonder how SST compares to them and why you would use SST instead of them.
In a nutshell, SST is for developers, while CDKTF and Pulumi are primarily for DevOps engineers. There are 3 big things SST does for developers:

  1. Higher-level components
SST’s built-in components like [`Nextjs`](https://sst.dev/docs/component/aws/nextjs/) or [`Email`](https://sst.dev/docs/component/aws/email/) make it easy for developers to add features to their app. You can use these without having to figure out how to work with the underlying Terraform resources.
  2. Linking resources
SST makes it easy to link your infrastructure to your application and access them at runtime in your code.
  3. Dev mode
Finally, SST features a unified local developer environment that deploys your app through a watcher, runs your functions [_Live_](https://sst.dev/docs/live/), creates a [_tunnel_](https://sst.dev/docs/reference/cli#tunnel) to your VPC, starts your frontend and backend, all together.

* * *
**How does SST make money?**
While SST is open-source and free to use, we also have the [Console](https://sst.dev/docs/console/) that can auto-deploy your apps and monitor for any issues. It’s optional and includes a free tier but it’s a SaaS service. It’s used by a large number of teams in our community, including ours.
* * *

#### [Next steps](https://sst.dev/docs/#next-steps)

  1. [Learn about the SST workflow](https://sst.dev/docs/workflow/)
  2. Create your first SST app
     * [Build a Next.js app in AWS](https://sst.dev/docs/start/aws/nextjs/)
     * [Deploy Bun in a container to AWS](https://sst.dev/docs/start/aws/bun/)
     * [Build a Hono API with Cloudflare Workers](https://sst.dev/docs/start/cloudflare/hono/)

[Skip to content](https://sst.dev/docs#_top)

# What is SST

SST is a framework that makes it easy to build modern full-stack applications on your own infrastructure.
SST supports over 150 providers. Check out the [full list](https://sst.dev/docs/all-providers#directory).
What makes SST different is that your _entire_ app is **defined in code** — in a single `sst.config.ts` file. This includes databases, buckets, queues, Stripe webhooks, or any one of **150+ providers**.
With SST, **everything is automated**.
* * *

## [Components](https://sst.dev/docs#components)

You start by defining parts of your app, _**in code**_.
For example, you can add your frontend and set the domain you want to use.

* [Next.js](https://sst.dev/docs#tab-panel-18)
* [Remix](https://sst.dev/docs#tab-panel-19)
* [Astro](https://sst.dev/docs#tab-panel-20)
* [Svelte](https://sst.dev/docs#tab-panel-21)
* [Solid](https://sst.dev/docs#tab-panel-22)

sst.config.ts
```typescript

new sst.aws.Nextjs("MyWeb", {

domain: "my-app.com"

});

```

sst.config.ts

```typescript


new sst.aws.Remix("MyWeb", {




domain: "my-app.com"



});

```

sst.config.ts

```typescript

new sst.aws.Astro("MyWeb", {

domain: "my-app.com"

});

```

sst.config.ts

```typescript


new sst.aws.SvelteKit("MyWeb", {




domain: "my-app.com"



});

```

sst.config.ts

```typescript

new sst.aws.SolidStart("MyWeb", {

domain: "my-app.com"

});

```

Just like the frontend, you can configure backend features _in code_.
Like your API deployed in a container. Or any Lambda functions, Postgres databases, S3 Buckets, or cron jobs.

* [Containers](https://sst.dev/docs#tab-panel-23)
* [Functions](https://sst.dev/docs#tab-panel-24)
* [Postgres](https://sst.dev/docs#tab-panel-25)
* [Bucket](https://sst.dev/docs#tab-panel-26)
* [Cron](https://sst.dev/docs#tab-panel-27)

sst.config.ts

```typescript


const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


loadBalancer: {



ports: [{ listen: "80/http" }]



}


});

```

sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

handler: "src/lambda.handler"

});

```

sst.config.ts

```typescript


new sst.aws.Postgres("MyDatabase", { vpc });


```

sst.config.ts

```typescript

new sst.aws.Bucket("MyBucket");

```

sst.config.ts

```typescript


new sst.aws.Cron("MyCronJob", {




job: "src/cron.handler",




schedule: "rate(1 minute)"



});

```

You can even set up your Stripe products in code.
sst.config.ts

```typescript

new stripe.Product("MyStripeProduct", {

name: "SST Paid Plan",

description: "This is how SST makes money",

});

```

You can check out the full list of components in the sidebar.
* * *

## [Infrastructure](https://sst.dev/docs#infrastructure)

The above are called **Components**. They are a way of defining the features of your application in code. You can define any feature of your application with them.
In the above examples, they create the necessary infrastructure in your AWS account. All without using the AWS Console.
Learn more about [Components](https://sst.dev/docs/components/).
* * *

### [Configure](https://sst.dev/docs#configure)

SST’s components come with sensible defaults designed to get you started. But they can also be configured completely.
For example, the `sst.aws.Function` can be configured with all the common Lambda function options.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




handler: "src/lambda.handler",




timeout: "3 minutes",




memory: "1024 MB"



});

```

But with SST you can take it a step further and transform how the Function component creates its low level resources. For example, the Function component also creates an IAM Role. You can transform the IAM Role using the `transform` prop.
sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

handler: "src/lambda.handler",

transform: {

role: (args)=> ({

name: `${args.name}-MyRole`

})

}

});

```

Learn more about [transforms](https://sst.dev/docs/components#transforms).
* * *

### [Providers](https://sst.dev/docs#providers)

SST has built-in components for AWS and Cloudflare that make these services easier to use.
However it also supports components from any one of the **150+ Pulumi/Terraform providers**. For example, you can use Vercel for your frontends.
sst.config.ts

```typescript


new vercel.Project("MyFrontend", {




name: "my-nextjs-app"



});

```

Learn more about [Providers](https://sst.dev/docs/providers) and check out the full list in the [Directory](https://sst.dev/docs/all-providers#directory).
* * *

## [Link resources](https://sst.dev/docs#link-resources)

Once you’ve added a couple of features, SST can help you link them together. This is great because you **won’t need to hardcode** anything in your app.
Let’s say you are deploying an Express app in a container and you want to upload files to an S3 bucket. You can `link` the bucket to your container.
sst.config.ts

```typescript

const bucket = newsst.aws.Bucket("MyBucket");

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

new sst.aws.Service("MyService", {

cluster,

link: [bucket],

loadBalancer: {

ports: [{ listen: "80/http" }]

}

});

```

You can then use SST’s [SDK](https://sst.dev/docs/reference/sdk/) to access the S3 bucket in your Express app.
index.mjs```

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

```

Learn more about [resource linking](https://sst.dev/docs/linking/).
* * *

## [Project structure](https://sst.dev/docs#project-structure)

We’ve looked at a couple of different types of files. Let’s take a step back and see what an SST app looks like in practice.
* * *

### [Drop-in mode](https://sst.dev/docs#drop-in-mode)

The simplest way to run SST is to use it as a part of your app. This is called _drop-in mode_. For example, if you are building a Next.js app, you can add a `sst.config.ts` file to the root.

```

my-nextjs-app

├─ next.config.js

├─ sst.config.ts

├─ package.json

├─ app

├─ lib

└─ public

```

View an
* * *

### [Monorepo](https://sst.dev/docs#monorepo)

Alternatively, you might use SST in a monorepo. This is useful because most projects have a frontend, a backend, and some functions.
In this case, the `sst.config.ts` is still in the root but you can split it up into parts in the `infra/` directory.

```

my-sst-app

├─ sst.config.ts

├─ package.json

├─ packages

│  ├─ functions

│  ├─ frontend

│  ├─ backend

│  └─ core

└─ infra

```

Learn more about our [monorepo setup](https://sst.dev/docs/set-up-a-monorepo/).
* * *

## [CLI](https://sst.dev/docs#cli)

To make this all work, SST comes with a [CLI](https://sst.dev/docs/reference/cli/). You can install it as a part of your Node project.
Terminal window```

npminstallsst

```

Or if you are not using Node, you can install it globally.
Terminal window```

curl-fsSLhttps://sst.dev/install|bash

```

Learn more about the [CLI](https://sst.dev/docs/reference/cli/).
* * *

### [Dev](https://sst.dev/docs#dev)

The CLI includes a `dev` command that starts a local development environment.
Terminal window```

sstdev

```

This brings up a _multiplexer_ that:

  1. Starts a watcher that deploys any infrastructure changes.
  2. Runs your functions [_Live_](https://sst.dev/docs/live/), letting you make and test changes without having to redeploy them.
  3. Creates a [_tunnel_](https://sst.dev/docs/reference/cli#tunnel) to connect your local machine to any resources in a VPC.
  4. Starts your frontend and container services in dev mode and links it to your infrastructure.

The `sst dev` CLI makes it so that you won’t have to start your frontend or container applications separately. Learn more about [`sst dev`](https://sst.dev/docs/reference/cli/#dev).
* * *

### [Deploy](https://sst.dev/docs#deploy)

When you’re ready to deploy your app, you can use the `deploy` command.
Terminal window```

sstdeploy--stageproduction

```

* * *

#### [Stages](https://sst.dev/docs#stages)

The stage name is used to namespace different environments of your app. So you can create one for dev.
Terminal window```

sstdeploy--stagedev

```

Or for a pull request.
Terminal window```

sstdeploy--stagepr-123

```

Learn more about [stages](https://sst.dev/docs/reference/cli#stage).
* * *

## [Console](https://sst.dev/docs#console)

Once you are ready to go to production, you can use the [SST Console](https://sst.dev/docs/console/) to **auto-deploy** your app, create **preview environments** , and **monitor** for any issues.
![SST Console](https://sst.dev/_astro/sst-console-home.-pMOaf_T_hPeMB.webp)
Learn more about the [Console](https://sst.dev/docs/console/).
* * *

## [FAQ](https://sst.dev/docs#faq)

Here are some questions that we frequently get.
* * *
**Is SST open-source if it’s based on Pulumi and Terraform?**
SST uses Pulumi behind the scenes for the providers and the deployment engine. And Terraform’s providers are _bridged_ through Pulumi.
SST only relies on the open-source parts of Pulumi and Terraform. It does not require a Pulumi account and all the data about your app and its resources stay on your side.
* * *
**How does SST compare to CDK for Terraform or Pulumi?**
Both CDKTF and Pulumi allow you to define your infrastructure using a programming language like TypeScript. SST is also built on top of Pulumi. So you might wonder how SST compares to them and why you would use SST instead of them.
In a nutshell, SST is for developers, while CDKTF and Pulumi are primarily for DevOps engineers. There are 3 big things SST does for developers:

  1. Higher-level components
SST’s built-in components like [`Nextjs`](https://sst.dev/docs/component/aws/nextjs/) or [`Email`](https://sst.dev/docs/component/aws/email/) make it easy for developers to add features to their app. You can use these without having to figure out how to work with the underlying Terraform resources.
  2. Linking resources
SST makes it easy to link your infrastructure to your application and access them at runtime in your code.
  3. Dev mode
Finally, SST features a unified local developer environment that deploys your app through a watcher, runs your functions [_Live_](https://sst.dev/docs/live/), creates a [_tunnel_](https://sst.dev/docs/reference/cli#tunnel) to your VPC, starts your frontend and backend, all together.

* * *
**How does SST make money?**
While SST is open-source and free to use, we also have the [Console](https://sst.dev/docs/console/) that can auto-deploy your apps and monitor for any issues. It’s optional and includes a free tier but it’s a SaaS service. It’s used by a large number of teams in our community, including ours.
* * *

#### [Next steps](https://sst.dev/docs#next-steps)

  1. [Learn about the SST workflow](https://sst.dev/docs/workflow/)
  2. Create your first SST app
     * [Build a Next.js app in AWS](https://sst.dev/docs/start/aws/nextjs/)
     * [Deploy Bun in a container to AWS](https://sst.dev/docs/start/aws/bun/)
     * [Build a Hono API with Cloudflare Workers](https://sst.dev/docs/start/cloudflare/hono/)

[Skip to content](https://sst.dev/docs/linking#_top)

# Linking

Resource Linking allows you to access your **infrastructure** in your **runtime code** in a typesafe and secure way.

  1. Create a resource that you want to link to. For example, a bucket.
sst.config.ts
```typescript

const bucket = newsst.aws.Bucket("MyBucket");

```

  2. Link it to your function or frontend, using the `link` prop.
     * [Next.js](https://sst.dev/docs/linking#tab-panel-6)
     * [Remix](https://sst.dev/docs/linking#tab-panel-7)
     * [Astro](https://sst.dev/docs/linking#tab-panel-8)
     * [Function](https://sst.dev/docs/linking#tab-panel-9)
sst.config.ts

```typescript


new sst.aws.Nextjs("MyWeb", {



link: [bucket]


});

```

sst.config.ts

```typescript

new sst.aws.Remix("MyWeb", {

link: [bucket]

});

```

sst.config.ts

```typescript


new sst.aws.Astro("MyWeb", {



link: [bucket]


});

```

sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

handler: "src/lambda.handler",

link: [bucket]

});

```

  3. Use the [SDK](https://sst.dev/docs/reference/sdk/) to access the linked resource in your runtime in a typesafe way.
     * [Next.js](https://sst.dev/docs/linking#tab-panel-10)
     * [Remix](https://sst.dev/docs/linking#tab-panel-11)
     * [Astro](https://sst.dev/docs/linking#tab-panel-12)
     * [Function](https://sst.dev/docs/linking#tab-panel-13)
app/page.tsx```

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

```

app/routes/_index.tsx```

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

```

src/pages/index.astro```

---

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

---

```

src/lambda.ts
```typescript

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

```

The SDK currently supports JS/TS, Python, Golang, and Rust.

Learn how to use the SDK in [Python](https://sst.dev/docs/reference/sdk/#python), [Golang](https://sst.dev/docs/reference/sdk/#golang), and [Rust](https://sst.dev/docs/reference/sdk/#rust).
* * *

### [Working locally](https://sst.dev/docs/linking#working-locally)

The above applies to your app deployed through `sst deploy`.
To access linked resources locally you’ll need to be running `sst dev`. By default, the `sst dev` CLI runs a multiplexer that also starts your frontend for you. This loads all your linked resources in the environment. Read more about [`sst dev`](https://sst.dev/docs/reference/cli/#dev).
However if you are not using the multiplexer.

```

sstdev--mode=basic

```

You’ll need to wrap your frontend’s dev command with the `sst dev` command.

* [Next.js](https://sst.dev/docs/linking#tab-panel-14)
* [Remix](https://sst.dev/docs/linking#tab-panel-15)
* [Astro](https://sst.dev/docs/linking#tab-panel-16)
* [Function](https://sst.dev/docs/linking#tab-panel-17)

Terminal window```

sstdevnextdev

```

Terminal window```

sstdevremixdev

```

Terminal window```

sstdevastrodev

```

Terminal window```

sstdev

```

* * *

## [How it works](https://sst.dev/docs/linking#how-it-works)

At high level when you link a resource to a function or frontend, the following happens:

  1. The _links_ that the resource exposes are injected into the function package.
The links a component exposes are listed in its API reference. For example, you can [view a Bucket’s links here](https://sst.dev/docs/component/aws/bucket/#links).
  2. The types to access these links are generated.
  3. The function is given permission to access the linked resource.

* * *

### [Injecting links](https://sst.dev/docs/linking#injecting-links)

Resource links are injected into your function or frontend package when you run `sst dev` or `sst deploy`. But this is done in a slightly different way for both these cases.

#### [Functions](https://sst.dev/docs/linking#functions)

The functions in SST are tree shaken and bundled using

#### [Frontends](https://sst.dev/docs/linking#frontends)

The frontends are not bundled by SST. Instead, when they are built, SST injects the resource links into the `process.env` object using the prefix `SST_RESOURCE_`.
This is why when you are running your frontend locally, it needs to be wrapped in the `sst dev` command.
Links are only available on the server of your frontend.
Resource links are only available on the server-side of your frontend. If you want to access them in your client components, you’ll need to pass them in explicitly.
* * *

### [Generating types](https://sst.dev/docs/linking#generating-types)

When you run `sst dev` or `sst deploy`, it generates the types to access the linked resources. These are generated as:

  1. A `sst-env.d.ts` file in the project root with types for **all** the linked resources in the app.
  2. A `sst-env.d.ts` file in the same directory of the nearest `package.json` of the function or frontend that’s _receiving_ the links. This references the root `sst-env.d.ts` file.

You can check the generated `sst-env.d.ts` types into source control. This will let your teammates see the types without having to run `sst dev` when they pull your changes.
* * *

## [Extending linking](https://sst.dev/docs/linking#extending-linking)

The examples above are built into SST’s components. You might want to modify the permissions that are granted as a part of these links.
Or, you might want to link other resources from the Pulumi/Terraform ecosystem. Or want to link a different set of outputs than what SST exposes.
You can do this using the [`sst.Linkable`](https://sst.dev/docs/component/linkable/) component.
* * *

### [Link any value](https://sst.dev/docs/linking#link-any-value)

The `Linkable` component takes a list of properties that you want to link. These can be outputs from other resources or constants.
sst.config.ts

```typescript


const myLinkable = newsst.Linkable("MyLinkable", {




properties: { foo: "bar" }




});


```

You can optionally include permissions or bindings for the linked resource.
Now you can now link this resource to your frontend or a function.
sst.config.ts

```typescript

new sst.aws.Function("MyApi", {

handler: "src/lambda.handler",

link: [myLinkable]

});

```

Then use the [SDK](https://sst.dev/docs/reference/sdk/) to access that at runtime.
src/lambda.ts

```typescript


import { Resource } from"sst";




console.log(Resource.MyLinkable.foo);


```

Read more about [`sst.Linkable`](https://sst.dev/docs/component/linkable/).
* * *

### [Link any resource](https://sst.dev/docs/linking#link-any-resource)

You can also wrap any resource class to make it linkable with the `Linkable.wrap` static method.
sst.config.ts

```typescript

Linkable.wrap(aws.dynamodb.Table, (table)=> ({

properties: { tableName: table.name }

}));

```

Now you create an instance of `aws.dynamodb.Table` and link it in your app like any other SST component.
sst.config.ts

```typescript


const table = newaws.dynamodb.Table("MyTable", {




attributes: [{ name: "id", type: "S" }],




hashKey: "id"




});




new sst.aws.Nextjs("MyWeb", {



link: [table]


});

```

And use the [SDK](https://sst.dev/docs/reference/sdk/) to access it at runtime.
app/page.tsx```

import { Resource } from"sst";

console.log(Resource.MyTable.tableName);

```

* * *
### [Modify built-in links](https://sst.dev/docs/linking#modify-built-in-links)
You can also modify the links SST creates. For example, you might want to change the permissions of a linkable resource.
sst.config.ts
```typescript


sst.Linkable.wrap(sst.aws.Bucket, (bucket)=> ({




properties: { name: bucket.name },



include: [



sst.aws.permission({




actions: ["s3:GetObject"],




resources: [bucket.arn]



})


]


}));

```

This overrides the existing link and lets you create your own.
Read more about [`sst.Linkable.wrap`](https://sst.dev/docs/component/linkable/#static-wrap).

[Skip to content](https://sst.dev/docs/reference/cli#_top)

# CLI

The CLI helps you manage your SST apps.
If you are using SST as a part of your Node project, we recommend installing it locally.
Terminal window```

npminstallsst

```

* * *
If you are not using Node, you can install the CLI globally.
Terminal window```


curl-fsSLhttps://sst.dev/install|bash


```

The CLI currently supports macOS, Linux, and WSL. Windows support is in beta.
To install a specific version.
Terminal window```

curl-fsSLhttps://sst.dev/install|VERSION=0.0.403bash

```

* * *
#### [With a package manager](https://sst.dev/docs/reference/cli#with-a-package-manager)
You can also use a package manager to install the CLI.
  * **macOS**
The CLI is available via a Homebrew Tap, and as downloadable binary in the 
Terminal window```


brewinstallsst/tap/sst



# Upgrade



brewupgradesst


```

You might have to run `brew upgrade sst`, before the update.

* **Linux**
The CLI is available as downloadable binaries in the `.deb` or `.rpm` and install with `sudo dpkg -i` and `sudo rpm -i`.
For Arch Linux, it’s available in the

* * *

#### [Usage](https://sst.dev/docs/reference/cli#usage)

Once installed you can run the commands using.
Terminal window```

sst [command]

```

The CLI takes a few global flags. For example, the deploy command takes the `--stage` flag
Terminal window```


sstdeploy--stageproduction


```

* * *

#### [Environment variables](https://sst.dev/docs/reference/cli#environment-variables)

You can access any environment variables set in the CLI in your `sst.config.ts` file. For example, running:
Terminal window```

ENV_VAR=123sstdeploy

```

Will let you access `ENV_VAR` through `process.env.ENV_VAR`.
* * *
## [Global Flags](https://sst.dev/docs/reference/cli#global-flags)
### [stage](https://sst.dev/docs/reference/cli#stage)
**Type** `string`
Set the stage the CLI is running on.
```

sst [command] --stage production

```

The stage is a string that is used to prefix the resources in your app. This allows you to have multiple _environments_ of your app running in the same account.
Changing the stage will redeploy your app to a new stage with new resources. The old resources will still be around in the old stage.
You can also use the `SST_STAGE` environment variable.
```

SST_STAGE=devsst [command]

```

This can also be declared in a `.env` file or in the CLI session.
If the stage is not passed in, then the CLI will:
  1. Use the username on the local machine. 
     * If the username is `root`, `admin`, `prod`, `dev`, `production`, then it will prompt for a stage name.
  2. Store this in the `.sst/stage` file and reads from it in the future.


This stored stage is called your **personal stage**.
### [verbose](https://sst.dev/docs/reference/cli#verbose)
**Type** `boolean`
Prints extra information to the log files in the `.sst/` directory.
Terminal window```


sst [command] --verbose


```

To also view this on the screen, use the `--print-logs` flag.

### [print-logs](https://sst.dev/docs/reference/cli#print-logs)

**Type** `boolean`
Print the logs to the screen. These are logs that are written to the `.sst/` directory.
Terminal window```

sst [command] --print-logs

```

It can also be set using the `SST_PRINT_LOGS` environment variable.
Terminal window```


SST_PRINT_LOGS=1sst [command]


```

This is useful when running in a CI environment.

### [config](https://sst.dev/docs/reference/cli#config)

**Type** `string`
Optionally, pass in a path to the SST config file. This default to `sst.config.ts` in the current directory.
Terminal window```

sst--configpath/to/config.ts [command]

```

This is useful when your monorepo has multiple SST apps in it. You can run the SST CLI for a specific app by passing in the path to its config file.
### [help](https://sst.dev/docs/reference/cli#help)
**Type** `boolean`
Prints help for the given command.
```

sst [command] --help

```

Or the global help.
```

sst--help

```

## [Commands](https://sst.dev/docs/reference/cli#commands)
### [init](https://sst.dev/docs/reference/cli#init)
```

sstinit

```

#### [Flags](https://sst.dev/docs/reference/cli#flags)
  * `yes` `boolean`
Skip interactive confirmation for detected framework.


Initialize a new project in the current directory. This will create a `sst.config.ts` and `sst install` your providers.
If this is run in a Next.js, Remix, Astro, or SvelteKit project, it’ll init SST in drop-in mode.
To skip the interactive confirmation after detecting the framework.
```

sstinit--yes

```

### [dev](https://sst.dev/docs/reference/cli#dev)
```

sstdev [command]

```

#### [Args](https://sst.dev/docs/reference/cli#args)
  * `command?`
The command to run


#### [Flags](https://sst.dev/docs/reference/cli#flags-1)
  * `mode` `string`
Defaults to using `multi` mode. Use `mono` to get a single stream of all child process logs or `basic` to not spawn any child processes.


Run your app in dev mode. By default, this starts a multiplexer with processes that deploy your app, run your functions, and start your frontend.
The tabbed terminal UI is only available on Linux/macOS and WSL.
Each process is run in a separate tab that you can click on in the sidebar.
![sst dev multiplexer mode](https://sst.dev/_astro/sst-dev-multiplexer-mode.D8lmOaku_1upbhD.webp)
The multiplexer makes it so that you won’t have to start your frontend or your container applications separately.
Here’s what happens when you run `sst dev`.
  * Deploy most of your resources as-is.
  * Except for components that have a `dev` prop. 
    * `Function` components are run [_Live_](https://sst.dev/docs/live/) in the **Functions** tab.
    * `Task` components have their _stub_ versions deployed that proxy the task and run their `dev.command` in the **Tasks** tab.
    * Frontends like `Nextjs`, `Remix`, `Astro`, `StaticSite`, etc. have their dev servers started in a separate tab and are not deployed.
    * `Service` components are not deployed, and instead their `dev.command` is started in a separate tab.
    * `Postgres`, `Aurora`, and `Redis` link to a local database if the `dev` prop is set.
  * Start an [`sst tunnel`](https://sst.dev/docs/reference/cli#tunnel) session in a new tab if your app has a `Vpc` with `bastion` enabled.
  * Load any [linked resources](https://sst.dev/docs/linking) in the environment.
  * Start a watcher for your `sst.config.ts` and redeploy any changes.


The `Service` component and the frontends like `Nextjs` or `StaticSite` are not deployed by `sst dev`.
Optionally, you can disable the multiplexer and not spawn any child processes by running `sst dev` in basic mode.
```

sstdev--mode=basic

```

This will only deploy your app and run your functions. If you are coming from SST v2, this is how `sst dev` used to work.
However in `basic` mode, you’ll need to start your frontend separately by running `sst dev` in a separate terminal session by passing in the command. For example:
```

sstdevnextdev

```

By wrapping your command, it’ll load your [linked resources](https://sst.dev/docs/linking) in the environment.
To pass in a flag to the command, use `--`.
```

sstdev--nextdev--turbo

```

You can also disable the tabbed terminal UI by running `sst dev` in mono mode.
```

sstdev--mode=mono

```

Unlike `basic` mode, this’ll spawn child processes. But instead of a tabbed UI it’ll show their outputs in a single stream.
This is used by default in Windows.
### [deploy](https://sst.dev/docs/reference/cli#deploy)
```

sstdeploy

```

#### [Flags](https://sst.dev/docs/reference/cli#flags-2)
  * `target`
Only run it for the given component.
  * `continue` `boolean`
Continue on error and try to deploy as many resources as possible.
  * `dev` `boolean`
Deploy resources like `sst dev` would.


Deploy your application. By default, it deploys to your personal stage. You typically want to deploy it to a specific stage.
```

sstdeploy--stageproduction

```

Optionally, deploy a specific component by passing in the name of the component from your `sst.config.ts`.
```

sstdeploy--targetMyComponent

```

All the resources are deployed as concurrently as possible, based on their dependencies. For resources like your container images, sites, and functions; it first builds them and then deploys the generated assets.
Configure the concurrency if your CI builds are running out of memory.
Since the build processes for some of these resources take a lot of memory, their concurrency is limited by default. However, this can be configured.
Resource | Concurrency | Flag  
---|---|---  
Sites | 1 | `SST_BUILD_CONCURRENCY_SITE`  
Functions | 4 | `SST_BUILD_CONCURRENCY_FUNCTION`  
Containers | 1 | `SST_BUILD_CONCURRENCY_CONTAINER`  
So only one site is built at a time, 4 functions are built at a time, and only 1 container is built at a time.
You can set the above environment variables to change this when you run `sst deploy`. This is useful for CI environments where you want to control this based on how much memory your CI machine has.
For example, to build a maximum of 2 sites concurrently.
```

SST_BUILD_CONCURRENCY_SITE=2sstdeploy

```

Or to configure all these together.
```

SST_BUILD_CONCURRENCY_SITE=2SST_BUILD_CONCURRENCY_CONTAINER=2SST_BUILD_CONCURRENCY_FUNCTION=8sstdeploy

```

Typically, this command exits when there’s an error deploying a resource. But sometimes you want to be able to `--continue` deploying as many resources as possible;
```

sstdeploy--continue

```

This is useful when deploying a new stage with a lot of resources. You want to be able to deploy as many resources as possible and then come back and fix the errors.
The `sst dev` command deploys your resources a little differently. It skips deploying resources that are going to be run locally. Sometimes you want to deploy a personal stage without starting `sst dev`.
```

sstdeploy--dev

```

The `--dev` flag will deploy your resources as if you were running `sst dev`.
### [diff](https://sst.dev/docs/reference/cli#diff)
```

sstdiff

```

#### [Flags](https://sst.dev/docs/reference/cli#flags-3)
  * `target`
Only run it for the given component.
  * `dev` `boolean`
Compare to the dev version of this stage.


Builds your app to see what changes will be made when you deploy it.
It displays a list of resources that will be created, updated, or deleted. For each of these resources, it’ll also show the properties that are changing.
Run a `sst diff` to see what changes will be made when you deploy your app.
This is useful for cases when you pull some changes from a teammate and want to see what will be deployed; before doing the actual deploy.
Optionally, you can diff a specific component by passing in the name of the component from your `sst.config.ts`.
```

sstdiff--targetMyComponent

```

By default, this compares to the last deploy of the given stage as it would be deployed using `sst deploy`. But if you are working in dev mode using `sst dev`, you can use the `--dev` flag.
```

sstdiff--dev

```

This is useful because in dev mode, you app is deployed a little differently.
### [add](https://sst.dev/docs/reference/cli#add)
```

sstadd<provider>

```

#### [Args](https://sst.dev/docs/reference/cli#args-1)
  * `provider`
The provider to add.


Adds and installs the given provider. For example,
```

sstaddaws

```

This command will:
  1. Installs the package for the AWS provider.
  2. Add `aws` to the globals in your `sst.config.ts`.
  3. And, add it to your `providers`.


sst.config.ts
```typescript

{


providers: {



aws: "6.27.0"



}


}

```

You can use any provider listed in the [Directory](https://sst.dev/docs/all-providers#directory).
Running `sst add aws` above is the same as manually adding the provider to your config and running `sst install`.
By default, the latest version of the provider is installed. If you want to use a specific version, you can change it in your config.
sst.config.ts

```typescript

{

providers: {

aws: {

version: "6.26.0"

}

}

}

```

You’ll need to run `sst install` if you update the `providers` in your config.
By default, these packages are fetched from the NPM registry. If you want to use a different registry, you can set the `NPM_REGISTRY` environment variable.

```

NPM_REGISTRY=<https://my-registry.comsstaddaws>

```

### [install](https://sst.dev/docs/reference/cli#install)

```

sstinstall

```

Installs the providers in your `sst.config.ts`. You’ll need this command when:

  1. You add a new provider to the `providers` or `home` in your config.
  2. Or, when you want to install new providers after you `git pull` some changes.

The `sst install` command is similar to `npm install`.
Behind the scenes, it installs the packages for your providers and adds the providers to your globals.
If you don’t have a version specified for your providers in your `sst.config.ts`, it’ll install their latest versions.

### [secret](https://sst.dev/docs/reference/cli#secret)

#### [Flags](https://sst.dev/docs/reference/cli#flags-4)

* `fallback` `boolean`
Manage the fallback values of secrets.

#### [Subcommands](https://sst.dev/docs/reference/cli#subcommands)

* [`set`](https://sst.dev/docs/reference/cli#secret-set)
* [`remove`](https://sst.dev/docs/reference/cli#secret-remove)
* [`load`](https://sst.dev/docs/reference/cli#secret-load)
* [`list`](https://sst.dev/docs/reference/cli#secret-list)

Manage the secrets in your app defined with `sst.Secret`.
The `--fallback` flag can be used to manage the fallback values of a secret.
Applies to all the sub-commands in `sst secret`.

#### [secret set](https://sst.dev/docs/reference/cli#secret-set)

```

sstsecretset<name> [value]

```

#### [Args](https://sst.dev/docs/reference/cli#args-2)

* `name`
The name of the secret.
* `value`
The value of the secret.

Set the value of the secret.
The secrets are encrypted and stored in an S3 Bucket in your AWS account. They are also stored in the package of the functions using the secret.
If you are not running `sst dev`, you’ll need to `sst deploy` to apply the secret.
For example, set the `sst.Secret` called `StripeSecret` to `123456789`.

```

sstsecretsetStripeSecretdev_123456789

```

Optionally, set the secret in a specific stage.

```

sstsecretsetStripeSecretprod_123456789--stageproduction

```

You can also set a _fallback_ value for a secret with `--fallback`.

```

sstsecretsetStripeSecretdev_123456789--fallback

```

So if the secret is not set for a specific stage, it’ll use the fallback instead. This only works for stages that are in the same AWS account.
Set fallback values for your PR stages.
This is useful for preview environments that are automatically deployed. You won’t have to set the secret for the stage after it’s deployed.
To set something like an RSA key, you can first save it to a file.

```

cat>tmp.txt<<EOF

-----BEGIN RSA PRIVATE KEY-----

MEgCQQCo9+BpMRYQ/dL3DS2CyJxRF+j6ctbT3/Qp84+KeFhnii7NT7fELilKUSnx

S30WAvQCCo2yU1orfgqr41mM70MBAgMBAAE=

-----END RSA PRIVATE KEY-----

EOF

```

Then set the secret from the file.

```

sstsecretsetKey<tmp.txt

```

And make sure to delete the temp file.

#### [secret remove](https://sst.dev/docs/reference/cli#secret-remove)

```

sstsecretremove<name>

```

#### [Args](https://sst.dev/docs/reference/cli#args-3)

* `name`
The name of the secret.

Remove a secret.
For example, remove the `sst.Secret` called `StripeSecret`.

```

sstsecretremoveStripeSecret

```

Optionally, remove a secret in a specific stage.

```

sstsecretremoveStripeSecret--stageproduction

```

Remove the fallback value of the secret.

```

sstsecretremoveStripeSecret--fallback

```

#### [secret load](https://sst.dev/docs/reference/cli#secret-load)

```

sstsecretload<file>

```

#### [Args](https://sst.dev/docs/reference/cli#args-4)

* `file`
The file to load the secrets from.

Load all the secrets from a file and set them.

```

sstsecretload./secrets.env

```

The file needs to be in the _dotenv_ or bash format of key-value pairs.
secrets.env```

KEY_1=VALUE1

KEY_2=VALUE2

```

Optionally, set the secrets in a specific stage.

```

sstsecretload--stageproduction./prod.env

```

Set these secrets as _fallback_ values.

```

sstsecretload./secrets.env--fallback

```

This command can be paired with the `secret list` command to get all the secrets from one stage and load them into another.

```

sstsecretlist>./secrets.env

sstsecretload--stageproduction./secrets.env

```

This works becase `secret list` outputs the secrets in the right format.

#### [secret list](https://sst.dev/docs/reference/cli#secret-list)

```

sstsecretlist

```

Lists all the secrets.
Optionally, list the secrets in a specific stage.

```

sstsecretlist--stageproduction

```

List only the fallback secrets.

```

sstsecretlist--fallback

```

### [shell](https://sst.dev/docs/reference/cli#shell)

```

sstshell [command]

```

#### [Args](https://sst.dev/docs/reference/cli#args-5)

* `command?`
A command to run.

#### [Flags](https://sst.dev/docs/reference/cli#flags-5)

* `target`
Only run it for the given component.

Run a command with **all the resources linked** to the environment. This is useful for running scripts against your infrastructure.
For example, let’s say you have the following resources in your app.
sst.config.ts
```typescript

newsst.aws.Bucket("MyMainBucket");

newsst.aws.Bucket("MyAdminBucket");

```

We can now write a script that’ll can access both these resources with the [JS SDK](https://sst.dev/docs/reference/sdk/).
my-script.js```

import { Resource } from"sst";

console.log(Resource.MyMainBucket.name, Resource.MyAdminBucket.name);

```

And run the script with `sst shell`.

```

sstshellnodemy-script.js

```

This’ll have access to all the buckets from above.
Run the command with `--` to pass arguments to it.
To pass arguments into the script, you’ll need to prefix it using `--`.

```

sstshell--nodemy-script.js--arg1--arg2

```

If no command is passed in, it opens a shell session with the linked resources.

```

sstshell

```

This is useful if you want to run multiple commands, all while accessing the resources in your app.
Optionally, you can run this for a specific component by passing in the name of the component.

```

sstshell--targetMyComponent

```

Here the linked resources for `MyComponent` and its environment variables are available.

### [remove](https://sst.dev/docs/reference/cli#remove)

```

sstremove

```

#### [Flags](https://sst.dev/docs/reference/cli#flags-6)

* `target` `string`
Only run it for the given component.

Removes your application. By default, it removes your personal stage.
The resources in your app are removed based on the `removal` setting in your `sst.config.ts`.
This does not remove the SST _state_ and _bootstrap_ resources in your account as these might still be in use by other apps. You can remove them manually if you want to reset your account, [learn more](https://sst.dev/docs/state/#reset).
Optionally, remove your app from a specific stage.

```

sstremove--stageproduction

```

You can also remove a specific component by passing in the name of the component from your `sst.config.ts`.

```

sstremove--targetMyComponent

```

### [unlock](https://sst.dev/docs/reference/cli#unlock)

```

sstunlock

```

When you run `sst deploy`, it acquires a lock on your state file to prevent concurrent deploys.
However, if something unexpectedly kills the `sst deploy` process, or if you manage to run `sst deploy` concurrently, the lock might not be released.
This should not usually happen, but it can prevent you from deploying. You can run `sst unlock` to release the lock.

### [version](https://sst.dev/docs/reference/cli#version)

```

sstversion

```

Prints the current version of the CLI.

### [upgrade](https://sst.dev/docs/reference/cli#upgrade)

```

sstupgrade [version]

```

#### [Args](https://sst.dev/docs/reference/cli#args-6)

* `version?`
A version to upgrade to.

Upgrade the CLI to the latest version. Or optionally, pass in a version to upgrade to.

```

sstupgrade0.10

```

### [telemetry](https://sst.dev/docs/reference/cli#telemetry)

#### [Subcommands](https://sst.dev/docs/reference/cli#subcommands-1)

* [`enable`](https://sst.dev/docs/reference/cli#telemetry-enable)
* [`disable`](https://sst.dev/docs/reference/cli#telemetry-disable)

Manage telemetry settings.
SST collects completely anonymous telemetry data about general usage. We track:

* Version of SST in use
* Command invoked, `sst dev`, `sst deploy`, etc.
* General machine information, like the number of CPUs, OS, CI/CD environment, etc.

This is completely optional and can be disabled at any time.
You can also opt-out by setting an environment variable: `SST_TELEMETRY_DISABLED=1` or `DO_NOT_TRACK=1`.

#### [telemetry enable](https://sst.dev/docs/reference/cli#telemetry-enable)

```

ssttelemetryenable

```

Enable telemetry.

#### [telemetry disable](https://sst.dev/docs/reference/cli#telemetry-disable)

```

ssttelemetrydisable

```

Disable telemetry.

### [refresh](https://sst.dev/docs/reference/cli#refresh)

```

sstrefresh

```

#### [Flags](https://sst.dev/docs/reference/cli#flags-7)

* `target` `string`
Only run it for the given component.

Compares your local state with the state of the resources in the cloud provider. Any changes that are found are adopted into your local state. It will:

  1. Go through every single resource in your state.
  2. Make a call to the cloud provider to check the resource.
     * If the configs are different, it’ll **update the state** to reflect the change.
     * If the resource doesn’t exist anymore, it’ll **remove it from the state**.

The `sst refresh` does not make changes to the resources in the cloud provider.
You can also refresh a specific component by passing in the name of the component.

```

sstrefresh--targetMyComponent

```

This is useful for cases where you want to ensure that your local state is in sync with your cloud provider. [Learn more about how state works](https://sst.dev/docs/providers/#how-state-works).

### [state](https://sst.dev/docs/reference/cli#state)

#### [Subcommands](https://sst.dev/docs/reference/cli#subcommands-2)

* [`export`](https://sst.dev/docs/reference/cli#state-export)
* [`remove`](https://sst.dev/docs/reference/cli#state-remove)
* [`repair`](https://sst.dev/docs/reference/cli#state-repair)

Manage state of your app

#### [state export](https://sst.dev/docs/reference/cli#state-export)

```

sststateexport

```

#### [Flags](https://sst.dev/docs/reference/cli#flags-8)

* `decrypt`
Decrypt the state before printing it out.

Prints the state of your app.
This pull the state of your app from the cloud provider and then prints it out. You can write this to a file or view it directly in your terminal.
This can be run for specific stages as well.

```

sststateexport--stageproduction

```

By default, it runs on your personal stage.

#### [state remove](https://sst.dev/docs/reference/cli#state-remove)

```

sststateremove<target>

```

#### [Args](https://sst.dev/docs/reference/cli#args-7)

* `target`
The name of the resource to remove.

Removes the reference for the given resource from the state.
This does not remove the resource itself.
This does not remove the resource itself, it only edits the state of your app.

```

sststateremoveMyBucket

```

Here, `MyBucket` is the name of the resource as defined in your `sst.config.ts`.
sst.config.ts
```typescript

new sst.aws.Bucket("MyBucket");

```

This command will:

  1. Find the resource with the given name in the state.
  2. Remove that from the state. It does not remove the children of this resource.
  3. Runs a `repair` to remove any dependencies to this resource.

You can run this for specific stages as well.

```

sststateremoveMyBucket--stageproduction

```

By default, it runs on your personal stage.

#### [state repair](https://sst.dev/docs/reference/cli#state-repair)

```

sststaterepair

```

Repairs the state of your app if it’s corrupted.
Sometimes, if something goes wrong with your app, or if the state was directly edited, the state can become corrupted. This will cause your `sst deploy` command to fail.
This command looks for the following issues and fixes them.

  1. Since the state is a list of resources, if one resource depends on another, it needs to be listed after the one it depends on. This command finds resources that depend on each other but are not ordered correctly and **reorders them**.
  2. If resource B depends on resource A, but resource A is not listed in the state, it’ll **remove the dependency**.

This command does this by going through all the resources in the state, fixing the issues and updating the state.
You can run this for specific stages as well.

```

sststaterepair--stageproduction

```

By default, it runs on your personal stage.

### [cert](https://sst.dev/docs/reference/cli#cert)

```

sstcert

```

Generate a locally-trusted certificate to connect to the Console.
The Console can show you local logs from `sst dev` by connecting to your CLI. Certain browsers like Safari and Brave require the local connection to be running on HTTPS.
This command uses `localhost` and `127.0.0.1`.
You’ll only need to do this once on your machine.

### [tunnel](https://sst.dev/docs/reference/cli#tunnel)

#### [Subcommands](https://sst.dev/docs/reference/cli#subcommands-3)

* [`install`](https://sst.dev/docs/reference/cli#tunnel-install)

Start a tunnel.

```

ssttunnel

```

If your app has a VPC with `bastion` enabled, you can use this to connect to it. This will forward traffic from the following ranges over SSH:

* `10.0.4.0/22`
* `10.0.12.0/22`
* `10.0.0.0/22`
* `10.0.8.0/22`

The tunnel allows your local machine to access resources that are in the VPC.
The tunnel is only available for apps that have a VPC with `bastion` enabled.
If you are running `sst dev`, this tunnel will be started automatically under the _Tunnel_ tab in the sidebar.
This is automatically started when you run `sst dev`.
You can start this manually if you want to connect to a different stage.

```

ssttunnel--stageproduction

```

This needs a network interface on your local machine. You can create this with the `sst tunnel install` command.

#### [tunnel install](https://sst.dev/docs/reference/cli#tunnel-install)

```

ssttunnelinstall

```

Install the tunnel.
To be able to create a tunnel, SST needs to create a network interface on your local
Terminal window```

sudossttunnelinstall

```

You only need to run this once on your machine.

### [diagnostic](https://sst.dev/docs/reference/cli#diagnostic)

```

sstdiagnostic

```

Generates a diagnostic report based on the last command that was run.
This takes the state of your app, its log files, and generates a zip file in the `.sst/` directory. This is for debugging purposes.

[Skip to content](https://sst.dev/docs/component/aws/email#_top)

# Email

The `Email` component lets you send emails in your app. It uses
You can configure it to send emails from a specific email address or from any email addresses in a domain.
New AWS SES accounts are in _sandbox mode_ and need to
By default, new AWS SES accounts are in the _sandbox mode_ and can only send email to verified email addresses and domains. It also limits your account to a sending quota. To remove these restrictions, you need to

#### [Sending from an email address](https://sst.dev/docs/component/aws/email#sending-from-an-email-address)

For using an email address as the sender, you need to verify the email address.
sst.config.ts
```typescript

const email = newsst.aws.Email("MyEmail", {

sender: "<spongebob@example.com>",

});

```

#### [Sending from a domain](https://sst.dev/docs/component/aws/email#sending-from-a-domain)

When you use a domain as the sender, you’ll need to verify that you own the domain.
sst.config.ts

```typescript


new sst.aws.Email("MyEmail", {




sender: "example.com"



});

```

#### [Configuring DMARC](https://sst.dev/docs/component/aws/email#configuring-dmarc)

sst.config.ts

```typescript

new sst.aws.Email("MyEmail", {

sender: "example.com",

dmarc: "v=DMARC1; p=quarantine; adkim=s; aspf=s;"

});

```

#### [Link to a resource](https://sst.dev/docs/component/aws/email#link-to-a-resource)

You can link it to a function or your Next.js app to send emails.
sst.config.ts

```typescript


new sst.aws.Function("MyApi", {




handler: "sender.handler",



link: [email]


});

```

Now in your function you can use the AWS SES SDK to send emails.
sender.ts

```typescript

import { Resource } from"sst";

import { SESv2Client, SendEmailCommand } from"@aws-sdk/client-sesv2";

const client = newSESv2Client();

await client.send(

newSendEmailCommand({

FromEmailAddress: Resource.MyEmail.sender,

Destination: {

ToAddresses: ["patrick@example.com"]

},

Content: {

Simple: {

Subject: { Data: "Hello World!" },

Body: { Text: { Data: "Sent from my SST app." } }

}

}

})

);

```

* * *

## [Constructor](https://sst.dev/docs/component/aws/email#constructor)

```

newEmail(name, args, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/email#parameters)

* `name` `string`
* `args` [`EmailArgs`](https://sst.dev/docs/component/aws/email#emailargs)
* `opts?`

## [EmailArgs](https://sst.dev/docs/component/aws/email#emailargs)

### [dmarc?](https://sst.dev/docs/component/aws/email#dmarc)

**Type** `Input``<``string``>`
**Default** `“v=DMARC1; p=none;”`
The DMARC policy for the domain. This’ll create a DNS record with the given DMARC policy. Only specify this if you are using a domain name as the `sender`.

```

{

dmarc: "v=DMARC1; p=quarantine; adkim=s; aspf=s;"

}

```

### [dns?](https://sst.dev/docs/component/aws/email#dns)

**Type** `Input``<``false`` |`[`sst.aws.dns`](https://sst.dev/docs/component/aws/dns/)` | `[`sst.cloudflare.dns`](https://sst.dev/docs/component/cloudflare/dns/)` | `[`sst.vercel.dns`](https://sst.dev/docs/component/vercel/dns/)`>`
**Default** `sst.aws.dns`
The DNS adapter you want to use for managing DNS records. Only specify this if you are using a domain name as the `sender`.
If `dns` is set to `false`, you have to add the DNS records manually to verify the domain.
Specify the hosted zone ID for the domain.

```

{

dns: sst.aws.dns({

zone: "Z2FDTNDATAQYW2"

})

}

```

Domain is hosted on Cloudflare.

```

{

dns: sst.cloudflare.dns()

}

```

### [events?](https://sst.dev/docs/component/aws/email#events)

**Type** `Input``<``Object``[]``>`

* [`bus?`](https://sst.dev/docs/component/aws/email#events-bus)
* [`name`](https://sst.dev/docs/component/aws/email#events-name)
* [`topic?`](https://sst.dev/docs/component/aws/email#events-topic)
* [`types`](https://sst.dev/docs/component/aws/email#events-types)

**Default** No event notifications
Configure event notifications for this Email component.

```

{

events: {

name: "OnBounce",

types: ["bounce"],

topic: "arn:aws:sns:us-east-1:123456789012:MyTopic"

}

}

```

#### [events[].bus?](https://sst.dev/docs/component/aws/email#events-bus)

**Type** `Input``<``string``>`
The ARN of the EventBridge bus to send events to.

#### [events[].name](https://sst.dev/docs/component/aws/email#events-name)

**Type** `Input``<``string``>`
The name of the event.

#### [events[].topic?](https://sst.dev/docs/component/aws/email#events-topic)

**Type** `Input``<``string``>`
The ARN of the SNS topic to send events to.

#### [events[].types](https://sst.dev/docs/component/aws/email#events-types)

**Type** `Input``<``Input``<``“``send``”`` | ``“``reject``”`` | ``“``bounce``”`` | ``“``complaint``”`` | ``“``delivery``”`` | ``“``delivery-delay``”`` | ``“``rendering-failure``”`` | ``“``subscription``”`` | ``“``open``”`` | ``“``click``”``>``[]``>`
The types of events to send.

### [sender](https://sst.dev/docs/component/aws/email#sender)

**Type** `Input``<``string``>`
The email address or domain name that you want to send emails from.
You’ll need to verify the email address or domain you are using.
Using an email address as the sender. You’ll need to verify the email address. When you deploy your app, you will receive an email from AWS SES with a link to verify the email address.

```

{

sender: "<john.smith@gmail.com>"

}

```

Using a domain name as the sender. You’ll need to verify that you own the domain. Once you verified, you can send emails from any email addresses in the domain.
SST can automatically verify the domain for the `dns` adapter that’s specified.
To verify the domain, you need to add the verification records to your domain’s DNS. This can be done automatically for the supported `dns` adapters.

```

{

sender: "example.com"

}

```

If the domain is hosted on Cloudflare.

```

{

sender: "example.com",

dns: sst.cloudflare.dns()

}

```

### [transform?](https://sst.dev/docs/component/aws/email#transform)

**Type** `Object`

* [`configurationSet?`](https://sst.dev/docs/component/aws/email#transform-configurationset)
* [`identity?`](https://sst.dev/docs/component/aws/email#transform-identity)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.configurationSet?](https://sst.dev/docs/component/aws/email#transform-configurationset)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the SES configuration set resource.

#### [transform.identity?](https://sst.dev/docs/component/aws/email#transform-identity)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the SES identity resource.

## [Properties](https://sst.dev/docs/component/aws/email#properties)

### [configSet](https://sst.dev/docs/component/aws/email#configset)

**Type** `Output``<``string``>`
The name of the configuration set.

### [nodes](https://sst.dev/docs/component/aws/email#nodes)

**Type** `Object`

* [`configurationSet`](https://sst.dev/docs/component/aws/email#nodes-configurationset)
* [`identity`](https://sst.dev/docs/component/aws/email#nodes-identity)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.configurationSet](https://sst.dev/docs/component/aws/email#nodes-configurationset)

**Type**
The Amazon SES configuration set.

#### [nodes.identity](https://sst.dev/docs/component/aws/email#nodes-identity)

**Type**
The Amazon SES identity.

### [sender](https://sst.dev/docs/component/aws/email#sender-1)

**Type** `Output``<``string``>`
The sender email address or domain name.

## [SDK](https://sst.dev/docs/component/aws/email#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/email#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `configSet` `string`
The name of the configuration set.
* `sender` `string`
The sender email address or domain name.

## [Methods](https://sst.dev/docs/component/aws/email#methods)

### [static get](https://sst.dev/docs/component/aws/email#static-get)

```

Email.get(name, sender, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/email#parameters-1)

* `name` `string`
The name of the component.
* `sender` `Input``<``string``>`
The email address or domain name of the existing SES identity.
* `opts?`

**Returns** [`Email`](https://sst.dev/docs/component/aws/)
Reference an existing Email component with the given Amazon SES identity. This is useful when you create an SES identity in one stage and want to share it in another stage. It avoids having to create a new Email component in the other stage.
Imagine you create an Email component in the `dev` stage. And in your personal stage `frank`, instead of creating a new component, you want to share the one from `dev`.
sst.config.ts

```typescript


const email = $app.stage === "frank"




? sst.aws.Email.get("MyEmail", "spongebob@example.com")




:new sst.aws.Email("MyEmail", {




sender: "spongebob@example.com",



});

```

[Skip to content](https://sst.dev/docs/live#_top)

# Live

Live is a feature of SST that lets you test changes made to your AWS Lambda functions in milliseconds. Your changes work without having to redeploy. And they can be invoked remotely.
By default, `sst dev` will run all the functions in your app _“live”_.
It works by proxying requests from AWS to your local machine, executing it locally, and proxying the response back.
* * *

## [Advantages](https://sst.dev/docs/live#advantages)

This setup of running your functions locally and proxying the results back allows you to do a couple of things:

* Your changes are **reloaded in under 10ms**.
* You can set **breakpoints to debug** your function in your favorite IDE.
* Functions can be invoked remotely. For example, say `https://my-api.com/hello` is your API endpoint. Hitting that will run the local version of that function.
  * This applies to more than just APIs. Any cron job or async event that gets invoked remotely will also run your local function.
  * It allows you to very easily debug and **test webhooks** , since you can just give the webhook your API endpoint.
  * Supports all function triggers, there’s no need to mock an event.
* Uses the **right IAM permissions** , so if a Lambda fails on AWS due to the lack of IAM permissions, it would fail locally as well.

* * *

## [How it works](https://sst.dev/docs/live#how-it-works)

Live uses
When you run `sst dev`, it [bootstraps](https://sst.dev/docs/state#bootstrap) a new AppSync Events API for the region you are using.
This is roughly what the flow looks like:

  1. When you run `sst dev`, it deploys your app and replaces the Lambda functions with a _stub_ version.
  2. It also starts up a local WebSocket client and connects to the AppSync API endpoint.
  3. When a Lambda function in your app is invoked, it publishes an event, where the payload is the Lambda function request.
  4. Your local WebSocket client receives this event. It publishes an event acknowledging that it received the request.
  5. Next, it runs the local version of the function and publishes an event with the function response as the payload. The local version is run as a Node.js Worker.
  6. Finally, the stub Lambda function receives the event and responds with the payload.

* * *

### [Quirks](https://sst.dev/docs/live#quirks)

There are a couple of quirks with this setup that are worth noting.

  1. **Runtime change**
The stub function that’s deployed uses a **different runtime** than your Lambda function. You might run into this when you change the runtime in your config but the runtime of the Lambda function in the AWS Console doesn’t change.
The _stub_ function that’s deployed uses a different runtime than the actual function.
We use a different runtime because we want the function to be as fast as possible at proxying requests.
  2. **Live mode persists**
If you kill the `sst dev` CLI, your functions are not run locally anymore but the stub function in AWS are still there. This means that it’ll attempt to proxy requests to your machine and timeout.
Only use `sst dev` in your personal stage.
You can fix this by running `sst deploy` and it’ll deploy the real version of your app. But the next time you run `sst dev` it’ll need to deploy the stub back. This’ll take a couple of minutes. So we recommend only using your personal stages for `sst dev`. And avoid flipping back and forth between `dev` and `deploy`.

* * *

### [Live mode](https://sst.dev/docs/live#live-mode)

When a function is running live it sets the `SST_DEV` environment variable to `true`. So in your Node.js functions you can access it using `process.env.SST_DEV`.
src/lambda.js```

exportasyncfunctionmain(event) {

const body = process.env.SST_DEV ? "Hello, Live!" : "Hello, World!";

return {

body,

statusCode: 200,

};

}

```

This is useful if you want to access some resources locally.
* * *
#### [Connect to a local DB](https://sst.dev/docs/live#connect-to-a-local-db)
For example, when running locally you might want to connect to a local database. You can do that with the `SST_DEV` environment variable.
```

const dbHost = process.env.SST_DEV

?"localhost"

:"amazon-string.rds.amazonaws.com";

```

* * *
## [Cost](https://sst.dev/docs/live#cost)
AWS AppSync Events that powers Live is **completely serverless**. So you don’t get charged when it’s not in use.
It’s also pretty cheap. It’s roughly $1.00 per million messages and $0.08 per million connection minutes. You can 
This approach has been economical even for large teams with dozens of developers.
* * *
## [Privacy](https://sst.dev/docs/live#privacy)
All the data stays between your local machine and your AWS account. There are **no 3rd party services** that are used.
Live also supports connecting to AWS resources inside a VPC.
* * *
### [Using a VPC](https://sst.dev/docs/live#using-a-vpc)
By default your local functions cannot connect to resources in a VPC. You can fix this by either setting up a VPN connection or creating a tunnel.
* * *
#### [Creating a tunnel](https://sst.dev/docs/live#creating-a-tunnel)
To create a tunnel, you’ll need to:
  1. Enable the `bastion` host in your VPC.
sst.config.ts
```typescript


new sst.aws.Vpc("MyVpc", { bastion: true });


```

  2. Install the tunnel.
Terminal window```

sudossttunnelinstall

```

This needs _sudo_ to create the network interface on your machine. You only need to do this once.
  3. Run `sst dev`.
Terminal window```


sstdev


```

This starts the tunnel automatically; notice the **Tunnel** tab on the left. Now your local environment can connect to resources in your VPC.
* * *

#### [Setting up a VPN connection](https://sst.dev/docs/live#setting-up-a-vpn-connection)

To set up a VPN connection, you’ll need to:

  1. Setup a VPN connection from your local machine to your VPC network. You can use the AWS Client VPN service to set it up.
  2. Then
  3. And, finally install

Note that, the AWS Client VPC service is billed on an hourly basis but it’s fairly inexpensive.
* * *

## [Breakpoints](https://sst.dev/docs/live#breakpoints)

Since Live runs your functions locally, you can set breakpoints and debug your functions in your favorite IDE.
![VS Code Enable Auto Attach](https://sst.dev/_astro/vs-code-enable-auto-attach.DU9F_N05_B9h6i.webp)
For VS Code, you’ll need to enable Auto Attach from the Command Palette. Hit `Ctrl+Shift+P` or `Cmd+Shift+P`, type in **Debug: Toggle Auto Attach** and select **Always**.
You need to start a new terminal **in VS Code** after enabling Auto Attach.
Now open a new terminal in VS Code, run `sst dev`, set a breakpoint in a function, and invoke the function.
* * *

## [Changelog](https://sst.dev/docs/live#changelog)

Live is a feature that was created by SST when it first launched back in 2021. It’s gone through a few different iterations since then.

SST Version | Change  
---|---  
**v0.5.0** | Then called _Live Lambda_ , used a API Gateway WebSocket API and a DynamoDB table.  
**v2.0.0** | Switched to using AWS IoT, this was roughly 2-3x faster.  
**v3.3.1** | Switched to using AWS AppSync Events, which is even faster and handles larger payloads better.

[Skip to content](https://sst.dev/docs/all-providers#_top)

# All Providers

Aside from the [built-in](https://sst.dev/docs/components#built-in) components, SST supports any of the **150+** Pulumi and Terraform providers.
Check out the full list in the [Directory](https://sst.dev/docs/all-providers#directory).
* * *

## [Add a provider](https://sst.dev/docs/all-providers#add-a-provider)

To add a provider to your app run.
Terminal window```

sstadd<provider>

```

This command adds the provider to your config, installs the packages, and adds the namespace of the provider to your globals.
You don’t need to `import` the provider packages in your `sst.config.ts`.
SST manages these packages internally and you do not need to import the package in your `sst.config.ts`.
For example, to add the Stripe provider.
Terminal window```


sstaddstripe


```

Read more about [providers](https://sst.dev/docs/providers).
* * *

### [Preloaded](https://sst.dev/docs/all-providers#preloaded)

SST comes preloaded with the following providers, so you **don’t need to add them**.
These are used internally to power the [built-in](https://sst.dev/docs/components#built-in) components.
* * *

## [Use a resource](https://sst.dev/docs/all-providers#use-a-resource)

Once added, you can use a resource from the provider in your `sst.config.ts`.
For example, use a Stripe resource in your config’s `run` function.
sst.config.ts

```typescript

exportdefault$config({

// ...

asyncrun() {

new stripe.Product("MyStripeProduct", {

name: "SST Paid Plan",

description: "This is how SST makes money",

});

},

});

```

As mentioned above, since the AWS provider comes preloaded, you can use any AWS resource directly as well.
sst.config.ts

```typescript


new aws.apprunner.Service("MyService", {




serviceName: "example",



sourceConfiguration: {


imageRepository: {


imageConfiguration: {



port: "8000"



},



imageIdentifier: "public.ecr.aws/aws-containers/hello-app-runner:latest",




imageRepositoryType: "ECR_PUBLIC"



}


}


});

```

* * *

## [Directory](https://sst.dev/docs/all-providers#directory)

Below is the full list of providers that SST supports.
Terminal window```

sstadd<provider>

```

Install any of the following using the package name as the `provider`. For example, `sst add auth0`.
If you want SST to support a Terraform provider or update a version, you can **submit a PR** to the 
* * *
Provider | Package  
---|---  
| `@netascode/aci`  
| `@pulumiverse/acme`  
| `aiven`  
| `akamai`  
| `alicloud`  
| `eks`  
| `@pulumiverse/aquasec`  
| `artifactory`  
| `@pulumiverse/astra`  
| `auth0`  
| `auto-deploy`  
| `aws-apigateway`  
| `aws`  
| `@lbrlabs/pulumi-awscontroltower`  
| `aws-iam`  
| `aws-native`  
| `aws-quickstart-aurora-postgres`  
| `aws-quickstart-redshift`  
| `aws-quickstart-vpc`  
| `aws-s3-replicated-bucket`  
| `aws-static-website`  
| `awsx`  
| `@ediri/azapi`  
| `azuread`  
| `azure`  
| `pulumi-azure-justrun`  
| `azure-native`  
| `azure-quickstart-acr-geo-replication`  
| `azure-quickstart-acr-geo-replication`  
| `azure-static-website`  
| `azuredevops`  
| `@pulumiverse/buildkite`  
| `@checkly/pulumi`  
| `sdwan`  
| `ise`  
| `civo`  
| `cloudinit`  
| `cloudamqp`  
| `cloudflare`  
| `@pulumiverse/cockroach`  
| `command`  
| `confluentcloud`  
| `consul`  
| `@pulumiverse/cpln`  
| `databricks`  
| `datadog`  
| `dbtcloud`  
| `digitalocean`  
| `dnsimple`  
| `docker`  
| `docker-build`  
| `@pulumiverse/doppler`  
| `@pulumiverse/dynatrace`  
| `ec`  
| `@equinix-labs/pulumi-equinix`  
| `@pulumiverse/esxi-native`  
| `@eventstore/pulumi-eventstorecloud`  
| `@pulumiverse/exoscale`  
| `f5bigip`  
| `fastly`  
| `@worawat/flux`  
| `@pulumiverse/fortios`  
| `pulumi-fusionauth`  
| `@pulumiverse/gandi`  
| `gcp-global-cloudrun`  
| `@genesiscloud/pulumi-genesiscloud`  
| `github`  
| `gitlab`  
| `gcp`  
| `google-native`  
| `google-cloud-static-website`  
| `@pulumiverse/grafana`  
| `@pulumiverse/harbor`  
| `harness`  
| `vault`  
| `@grapl/pulumi-hcp`  
| `hcloud`  
| `@impart-security/pulumi-impart`  
| `@komminarlabs/influxdb`  
| `kafka`  
| `keycloak`  
| `kong`  
| `@koyeb/pulumi-koyeb`  
| `kubernetes`  
| `kubernetes-cert-manager`  
| `kubernetes-coredns`  
| `@lbrlabs/pulumi-lauchdarkly`  
| `@lbrlabs/pulumi-eks`  
| `libvirt`  
| `linode`  
| `mailgun`  
| `@pulumiverse/matchbox`  
| `aws-miniflux`  
| `minio`  
| `mongodbatlas`  
| `@pulumiverse/mssql`  
| `mysql`  
| `neon`  
| `newrelic`  
| `kubernetes-ingress-nginx`  
| `@pierskarsenbarg/ngrok`  
| `nomad`  
| `ns1`  
| `nuage`  
| `@pierskarsenbarg/nutanix`  
| `okta`  
| `onelogin`  
| `openstack`  
| `opsgenie`  
| `oci`  
| `@ovh-devrelteam/pulumi-ovh`  
| `pagerduty`  
| `@pinecone-database/pulumi`  
| `planetscale`  
| `@port-labs/port`  
| `postgresql`  
| `@prodvana/pulumi-prodvana`  
| `@muhlba91/pulumi-proxmoxve`  
| `pulumiservice`  
| `@pulumiverse/purrl`  
| `@ediri/qovery`  
| `rabbitmq`  
| `rancher2`  
| `railway`  
| `random`  
| `@rediscloud/pulumi-rediscloud`  
| `@rootly/pulumi`  
| `@runpod-infra/pulumi`  
| `@pulumiverse/scaleway`  
| `@pulumiverse/sentry`  
| `signalfx`  
| `slack`  
| `snowflake`  
| `@splightplatform/pulumi-splight`  
| `splunk`  
| `spotinst`  
| `@pulumiverse/statuscake`  
| `scm`  
| `stripe`  
| `@pierskarsenbarg/sdm`  
| `sumologic`  
| `supabase`  
| `@symbiosis-cloud/symbiosis-pulumi`  
| `synced-folder`  
| `tailscale`  
| `@pulumiverse/talos`  
| `@pulumiverse/time`  
| `tls`  
| `@twingate/pulumi-twingate`  
| `@pulumiverse/unifi`  
| `@upstash/pulumi`  
| `venafi`  
| `@pulumiverse/vercel`  
| `vsphere`  
| `@volcengine/pulumi`  
| `vsphere`  
| `@ediri/vultr`  
| `wavefront`  
| `yandex`  
| `@pulumiverse/zitadel`  
| `@bdzscaler/pulumi-zia`  
| `@bdzscaler/pulumi-zpa`  
Any missing providers or typos? Feel free to _Edit this page_ and submit a PR.


[Skip to content](https://sst.dev/docs/providers#_top)
# Providers
A provider is what allows SST to interact with the APIs of various cloud services. These are packages that can be installed through your `sst.config.ts`.
SST is built on Pulumi/Terraform and **supports 150+ providers**. This includes the major clouds like AWS, Azure, and GCP; but also services like Cloudflare, Stripe, Vercel, Auth0, etc.
Check out the full list in the [Directory](https://sst.dev/docs/all-providers#directory).
* * *
## [Install](https://sst.dev/docs/providers#install)
To add a provider to your app run.
Terminal window```


sstadd<provider>


```

This command adds the provider to your config, installs the packages, and adds the namespace of the provider to your globals.
Do not `import` the provider packages in your `sst.config.ts`.
SST manages these packages internally and you do not need to import the package in your `sst.config.ts`.
Your app can have multiple providers.
The name of a provider comes from the **name of the package** in the [Directory](https://sst.dev/docs/all-providers#directory). For example, `sst add planetscale`, will add the following to your `sst.config.ts`.
sst.config.ts

```typescript

{

providers: {

planetscale: "0.0.7"

}

}

```

You can add multiple providers to your app.
sst.config.ts

```typescript

{


providers: {



aws: "6.27.0",




cloudflare: "5.37.1"



}


}

```

Read more about the [`sst add`](https://sst.dev/docs/reference/cli/#add) command.
* * *

## [Configure](https://sst.dev/docs/providers#configure)

You can configure a provider in your `sst.config.ts`. For example, to change the region for AWS.
sst.config.ts

```typescript

{

providers: {

aws: {

region: "us-west-2"

}

}

}

```

You can check out the available list of options that you can configure for a provider over on the provider’s docs. For example, here are the ones for
* * *

### [Versions](https://sst.dev/docs/providers#versions)

By default, SST installs the latest version. If you want to use a specific version, you can change it in your config.
sst.config.ts

```typescript

{


providers: {


aws: {



version: "6.27.0"



}


}


}

```

If you make any changes to the `providers` in your config, you’ll need to run `sst install`.
You’ll need to run `sst install` if you update the `providers` in your config.
The version of the provider is always pinned to what’s in the `sst.config.ts` and does not auto-update. This is the case, even if there is no version set. This is to make sure that the providers don’t update in the middle of your dev workflow.
Providers don’t auto-update. They stick to the version that was installed initially.
So if you want to update it, you’ll need to change it manually and run `sst install`.
* * *

### [Credentials](https://sst.dev/docs/providers#credentials)

Most providers will read your credentials from the environment. For example, for Cloudflare you might set your token like so.
Terminal window```

exportCLOUDFLARE_API_TOKEN=aaaaaaaa_aaaaaaaaaaaa_aaaaaaaa

```

However, some providers also allow you to pass in the credentials through the config.
sst.config.ts
```typescript

{


providers: {


cloudflare: {



apiToken: "aaaaaaaa_aaaaaaaaaaaa_aaaaaaaa"



}


}


}

```

Read more about [configuring providers](https://sst.dev/docs/reference/config/#providers).
* * *

## [Components](https://sst.dev/docs/providers#components)

The provider packages come with components that you can use in your app.
For example, running `sst add aws` will allow you to use all the components under the `aws` namespace.
sst.config.ts

```typescript

new aws.s3.BucketV2("b", {

bucket: "mybucket",

tags: {

Name: "My bucket"

}

});

```

Aside from components in the providers, SST also has a list of built-in components. These are typically higher level components that make it easy to add features to your app.
You can check these out in the sidebar. Read more about [Components](https://sst.dev/docs/components/).
* * *

## [Functions](https://sst.dev/docs/providers#functions)

Aside from the components, there are a collection of functions that are exposed by a provider. These are listed in the Pulumi docs as `getXXXXXX` on the sidebar.
For example, to get the AWS account being used in your app.
sst.config.ts

```typescript


const current = await aws.getCallerIdentity({});




const accountId = current.accountId;




const callerArn = current.arn;




const callerUser = current.userId;


```

Or to get the current region.
sst.config.ts

```typescript

const current = await aws.getRegion({});

const region = current.name;

```

* * *

#### [Output versions](https://sst.dev/docs/providers#output-versions)

The above are _async_ methods that return promises. That means that if you call these in your app, they’ll block the deployment of any resources that are defined after it.
Outputs don’t block your deployments.
So we instead recommend using the _Output_ version of these functions. For example, if we wanted to set the above as environment variables in a function, we would do something like this
sst.config.ts

```typescript


new sst.aws.Function("MyFunction, {




handler: "src/lambda.handler",



environment: {



ACCOUNT: aws.getCallerIdentityOutput({}).accountId,




REGION: aws.getRegionOutput().name



}


}

```

The `aws.getXXXXOutput` functions typically return an object of type _`Output<primitive>`_. Read more about[Outputs](https://sst.dev/docs/components/#outputs).
* * *

## [Instances](https://sst.dev/docs/providers#instances)

You can create multiple instances of a provider that’s in your config. By default SST creates one instance of each provider in your `sst.config.ts` with the defaults. By you can create multiple instances in your app.
sst.config.ts

```typescript

const useast1 = newaws.Provider("AnotherAWS");

```

This is useful for multi-region or multi-account deployments.
* * *

### [Multi-region](https://sst.dev/docs/providers#multi-region)

You might want to create multiple providers in cases where some resources in your app need to go to one region, while others need to go to a separate region.
Let’s look at an example. Assume your app is normally deployed to `us-west-1`. But you need to create an ACM certificate that needs to be deployed to `us-east-1`.
sst.config.ts

```typescript


const useast1 = newaws.Provider("useast1", { region: "us-east-1" });




new sst.aws.Function("MyFunction, "src/lambda.handler");




new aws.acm.Certificate("cert", {




domainName: "foo.com",




validationMethod: "EMAIL",




}, { provider: useast1 });


```

Here the function is created in your default region, `us-west-1`. While the certificate is created in `us-east-1`.

[Skip to content](https://sst.dev/docs/components#_top)

# Components

Every SST app is made up of components. These are logical units that represent features in your app; like your frontends, APIs, databases, or queues.
There are two types of components in SST:

  1. Built-in components — High level components built by the SST team
  2. Provider components — Low level components from the providers

Let’s look at them below.
* * *

## [Background](https://sst.dev/docs/components#background)

Most [providers](https://sst.dev/docs/providers/) like AWS are made up of low level resources. And it takes quite a number of these to put together something like a frontend or an API. For example, it takes around 70 low level AWS resources to create a Next.js app on AWS.
As a result, Infrastructure as Code has been traditionally only been used by DevOps or Platform engineers.
To fix this, SST has components that can help you with the most common features in your app.
* * *

## [Built-in](https://sst.dev/docs/components#built-in)

The built-in components in SST, the ones you see in the sidebar, are designed to make it really easy to create the various parts of your app.
For example, you don’t need to know a lot of AWS details to deploy your Next.js frontend:
sst.config.ts

```typescript

new sst.aws.Nextjs("MyWeb");

```

And because this is all in code, it’s straightforward to configure this further.
sst.config.ts

```typescript


new sst.aws.Nextjs("MyWeb", {




domain: "my-app.com",




path: "packages/web",



imageOptimization: {



memory: "512 MB"



},



buildCommand: "npm run build"



});

```

You can even take this a step further and completely transform how the low level resources are created. We’ll look at this below.
Aside from the built-in SST components, all the [Pulumi/Terraform providers](https://sst.dev/docs/all-providers#directory) are supported as well.
Currently SST has built-in components for two cloud providers.
* * *

### [AWS](https://sst.dev/docs/components#aws)

The AWS built-in components are designed to make it easy to work with AWS.
SST’s built-in components make it easy to build apps with AWS.
These components are namespaced under **`sst.aws.*`**and listed under AWS in the sidebar. Internally they use Pulumi’s
* * *

### [Cloudflare](https://sst.dev/docs/components#cloudflare)

These components are namespaced under **`sst.cloudflare.*`**and listed under Cloudflare in the sidebar. Internally they use Pulumi’s
* * *

## [Constructor](https://sst.dev/docs/components#constructor)

To add a component to your app, you create an instance of it by passing in a couple of args. For example, here’s the signature of the [Function](https://sst.dev/docs/component/aws/function) component.

```


new sst.aws.Function(name: string, args: FunctionArgs, opts?: pulumi.ComponentResourceOptions)


```

Each component takes the following:

* `name`: The name of the component. This needs to be unique across your entire app.
* `args`: An object of properties that allows you to configure the component.
* `opts?`: An optional object of properties that allows you to configure this component in Pulumi.

Here’s an example of creating a `Function` component:
sst.config.ts

```typescript

const function = newsst.aws.Function("MyFunction", {

handler: "src/lambda.handler"

});

```

* * *

### [Name](https://sst.dev/docs/components#name)

There are two guidelines to follow when naming your components:

  1. The names of SST’s built-in components and components extended with [`Linkable.wrap`](https://sst.dev/docs/component/linkable/#static-wrap) need to be global across your entire app.
This allows [Resource Linking](https://sst.dev/docs/linking) to look these resources up at runtime.
  2. Optionally, use PascalCase for the component name.
For example, you might name your bucket, `MyBucket` and use Resource Linking to look it up with `Resource.MyBucket`.
However this is purely cosmetic. You can use kebab case. So `my-bucket`, and look it up using `Resource['my-bucket']`.

* * *

### [Args](https://sst.dev/docs/components#args)

Each component takes a set of args that allow you to configure it. These args are specific to each component. For example, the Function component takes [`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs).
Most of these args are optional, meaning that most components need very little configuration to get started. Typically, the most common configuration options are lifted to the top-level. To further configure the component, you’ll need to use the `transform` prop.
Args usually take primitive types. However, they also take a special version of a primitive type. It’ll look something like _`Input<string>`_. We’ll look at this in detail below.
* * *

## [Transform](https://sst.dev/docs/components#transform)

Most components take a `transform` prop as a part of their constructor or methods. It’s an object that takes callbacks that allow you to transform how that component’s infrastructure is created.
You can completely configure a component using the `transform` prop.
For example, here’s what the `transform` prop looks like for the [Function](https://sst.dev/docs/component/aws/function#transform) component:

* `function`: A callback to transform the underlying Lambda function
* `logGroup`: A callback to transform the Lambda’s LogGroup resource
* `role`: A callback to transform the role that the Lambda function assumes

The type for these callbacks is similar. Here’s what the `role` callback looks like:

```

RoleArgs |(args:RoleArgs, opts: pulumi.ComponentResourceOptions, name:string)=>void

```

This takes either:

* A `RoleArgs` object. For example:

```

{

transform: {

role: {

name: "MyRole"

}

}

}

```

This is **merged** with the original `RoleArgs` that were going to be passed to the component.

* A function that takes `RoleArgs`. Here’s the function signature:

```

(args:RoleArgs, opts: pulumi.ComponentResourceOptions, name:string)=>void

```

Where
So you can pass in a callback that takes the current `RoleArgs` and mutates it.

```

{

transform: {

role: (args, opts)=> {

args.name=`${args.name}-MyRole`;

opts.retainOnDelete=true;

}

}

}

```

* * *

### [`$transform`](https://sst.dev/docs/components#transform-1)

Similar to the component transform, we have the global `$transform`. This allows you to transform how a component of a given type is created.
Set default props across all your components with `$transform`.
For example, set a default `runtime` for your functions.
sst.config.ts

```typescript


$transform(sst.aws.Function, (args, opts)=> {



// Set the default if it's not set by the component



args.runtime??="nodejs18.x";



});

```

This sets the runtime for any `Function` component that’ll be **created after this call**.
The reason we do the check for `args.runtime` is to allow components to override the default. We do this by only setting the default if the component isn’t specifying its own `runtime`.
sst.config.ts

```typescript

new sst.aws.Function("MyFunctionA", {

handler: "src/lambdaA.handler"

});

new sst.aws.Function("MyFunctionB", {

handler: "src/lambdaB.handler",

runtime: "nodejs20.x"

});

```

So given the above transform, `MyFunctionA` will have a runtime of `nodejs18.x` and `MyFunctionB` will have a runtime of `nodejs20.x`.
The `$transform` is only applied to components that are defined after it.
The `args` and `opts` in the `$transform` callback are what you’d pass to the `Function` component. Recall the signature of the `Function` component:
sst.config.ts

```typescript


new sst.aws.Function(name: string, args: FunctionArgs, opts?: pulumi.ComponentResourceOptions)


```

Read more about the global [`$transform`](https://sst.dev/docs/reference/global/#transform).
* * *

## [Properties](https://sst.dev/docs/components#properties)

An instance of a component exposes a set of properties. For example, the `Function` component exposes the following [properties](https://sst.dev/docs/component/aws/function#properties) — `arn`, `name`, `url`, and `nodes`.

```


const functionArn = function.arn;


```

These can be used to output info about your app or can be used as args for other components.
These are typically primitive types. However, they can also be a special version of a primitive type. It’ll look something like _`Output<string>`_. We’ll look at this in detail below.
* * *

### [Links](https://sst.dev/docs/components#links)

Some of these properties are also made available via [resource linking](https://sst.dev/docs/linking/). This allows you to access them in your functions and frontends in a typesafe way.
For example, a Function exposes its `name` through its [links](https://sst.dev/docs/component/aws/bucket/#links).
* * *

### [Nodes](https://sst.dev/docs/components#nodes)

The `nodes` property that a component exposes gives you access to the underlying infrastructure. This is an object that contains references to the underlying Pulumi components that are created.
The nodes that are made available reflect the ones that can be configured using the `transform` prop.
For example, the `Function` component exposes the following [nodes](https://sst.dev/docs/component/aws/function#nodes) — `function`, `logGroup`, and `role`.
* * *

## [Outputs](https://sst.dev/docs/components#outputs)

The properties of a component are typically of a special type that looks something like, _`Output<primitive>`_.
These are values that are not available yet and will be resolved as the deploy progresses. However, these outputs can be used as args in other components.
This makes it so that parts of your app are not blocked and all your resources are deployed as concurrently as possible.
For example, let’s create a function with an url.
sst.config.ts

```typescript

const myFunction = newsst.aws.Function("MyFunction", {

url: true,

handler: "src/lambda.handler"

});

```

Here, `myFunction.url` is of type `Output<string>`. We want to use this function url as a route in our router.
sst.config.ts

```typescript


new sst.aws.Router("MyRouter", {



routes: {



"/api": myFunction.url



}


});

```

The route arg takes `Input<string>`, which means it can take a string or an output. This creates a dependency internally. So the router will be deployed after the function has been. However, other components that are not dependent on this function can be deployed concurrently.
You can read more about
* * *

### [Apply](https://sst.dev/docs/components#apply)

Since outputs are values that are yet to be resolved, you cannot use them in regular operations. You’ll need to resolve them first.
For example, let’s take the function url from above. We cannot do the following.
sst.config.ts

```typescript

const newUrl = myFunction.url + "/foo";

```

This is because the value of the output is not known at the time of this operation. We’ll need to resolve it.
The easiest way to work with an output is using `.apply`. It’ll allow you to apply an operation on the output and return a new output.
sst.config.ts

```typescript


const newUrl = myFunction.url.apply((value) => value + "/foo");


```

In this case, `newUrl` is also an `Output<string>`.
* * *

### [Helpers](https://sst.dev/docs/components#helpers)

To make it a little easier to work with outputs, we have the following global helper functions.
* * *

#### [`$concat`](https://sst.dev/docs/components#concat)

This lets you do.
sst.config.ts

```typescript

const newUrl = $concat(myFunction.url, "/foo");

```

Instead of the apply.
sst.config.ts

```typescript


const newUrl = myFunction.url.apply((value) => value + "/foo");


```

Read more about [`$concat`](https://sst.dev/docs/reference/global/#concat).
* * *

#### [`$interpolate`](https://sst.dev/docs/components#interpolate)

This lets you do.
sst.config.ts

```typescript

const newUrl = $interpolate`${myFunction.url}/foo`;

```

Instead of the apply.
sst.config.ts

```typescript


const newUrl = myFunction.url.apply((value) => value + "/foo");


```

Read more about [`$interpolate`](https://sst.dev/docs/reference/global/#interpolate).
* * *

#### [`$jsonParse`](https://sst.dev/docs/components#jsonparse)

This is for outputs that are JSON strings. So instead of doing this.
sst.config.ts

```typescript

const policy = policyStr.apply((policy) =>

JSON.parse(policy)

);

```

You can.
sst.config.ts

```typescript


const policy = $jsonParse(policyStr);


```

Read more about [`$jsonParse`](https://sst.dev/docs/reference/global/#jsonParse).
* * *

#### [`$jsonStringify`](https://sst.dev/docs/components#jsonstringify)

Similarly, for outputs that are JSON objects. Instead of doing a stringify after an apply.
sst.config.ts

```typescript

const policy = policyObj.apply((policy) =>

JSON.stringify(policy)

);

```

You can.
sst.config.ts

```typescript


const policy = $jsonStringify(policyObj);


```

Read more about [`$jsonStringify`](https://sst.dev/docs/reference/global/#jsonStringify).
* * *

#### [`$resolve`](https://sst.dev/docs/components#resolve)

And finally when you are working with a list of outputs and you want to resolve them all together.
sst.config.ts

```typescript

$resolve([bucket.name, worker.url]).apply(([bucketName, workerUrl])=> {

console.log(`Bucket: ${bucketName}`);

console.log(`Worker: ${workerUrl}`);

})

```

Read more about [`$resolve`](https://sst.dev/docs/reference/global/#resolve).
* * *

## [Versioning](https://sst.dev/docs/components#versioning)

SST components evolve over time, sometimes introducing breaking changes. To maintain backwards compatibility, we implement a component versioning scheme.
For example, we released a new version the [`Vpc`](https://sst.dev/docs/component/aws/vpc) that does not create a NAT Gateway by default. To roll this out the previous version of the `Vpc` component was renamed to [`Vpc.v1`](https://sst.dev/docs/component/aws/vpc-v1).
Now if you were using the original `Vpc` component, update SST, and deploy; you’ll get an error during the deploy saying that there’s a new version of this component.
This allows you to decide what you want to do with this component.
* * *

#### [Continue with the old version](https://sst.dev/docs/components#continue-with-the-old-version)

If you prefer to continue using the older version of a component, you can rename it.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc");




const vpc = newsst.aws.Vpc.v1("MyVpc");


```

Now if you deploy again, SST knows that you want to stick with the old version and it won’t error.
* * *

#### [Update to the latest version](https://sst.dev/docs/components#update-to-the-latest-version)

Instead, if you wanted to update to the latest version, you’ll have to rename the component.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc");

const vpc = newsst.aws.Vpc("MyNewVpc");

```

Now if you redeploy, it’ll remove the previously created component and recreate it with the new name and the latest version.
This is because from SST’s perspective it looks like the `MyVpc` component was removed and a new component called `MyNewVpc` was added.
Removing and recreating components may cause temporary downtime in your app.
Since these are being recreated you’ve to be aware that there might be a period of time when that resource is not around. This might cause some downtime, depending on the resource.

[Skip to content](https://sst.dev/docs/component/aws/nextjs#_top)

# Nextjs

The `Nextjs` component lets you deploy

#### [Minimal example](https://sst.dev/docs/component/aws/nextjs#minimal-example)

Deploy the Next.js app that’s in the project root.
sst.config.ts

```typescript


newsst.aws.Nextjs("MyWeb");


```

#### [Change the path](https://sst.dev/docs/component/aws/nextjs#change-the-path)

Deploys a Next.js app in the `my-next-app/` directory.
sst.config.ts

```typescript

newsst.aws.Nextjs("MyWeb", {

path: "my-next-app/"

});

```

#### [Add a custom domain](https://sst.dev/docs/component/aws/nextjs#add-a-custom-domain)

Set a custom domain for your Next.js app.
sst.config.ts

```typescript


newsst.aws.Nextjs("MyWeb", {




domain: "my-app.com"



});

```

#### [Redirect www to apex domain](https://sst.dev/docs/component/aws/nextjs#redirect-www-to-apex-domain)

Redirect `www.my-app.com` to `my-app.com`.
sst.config.ts

```typescript

newsst.aws.Nextjs("MyWeb", {

domain: {

name: "my-app.com",

redirects: ["www.my-app.com"]

}

});

```

#### [Link resources](https://sst.dev/docs/component/aws/nextjs#link-resources)

[Link resources](https://sst.dev/docs/linking/) to your Next.js app. This will grant permissions to the resources and allow you to access it in your app.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket");




new sst.aws.Nextjs("MyWeb", {



link: [bucket]


});

```

You can use the [SDK](https://sst.dev/docs/reference/sdk/) to access the linked resources in your Next.js app.
app/page.tsx```

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

```

* * *
## [Constructor](https://sst.dev/docs/component/aws/nextjs#constructor)
```

newNextjs(name, args?, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/nextjs#parameters)
  * `name` `string`
  * `args?` [`NextjsArgs`](https://sst.dev/docs/component/aws/nextjs#nextjsargs)
  * `opts?`


## [NextjsArgs](https://sst.dev/docs/component/aws/nextjs#nextjsargs)
### [assets?](https://sst.dev/docs/component/aws/nextjs#assets)
**Type** `Input``<``Object``>`
  * [`fileOptions?`](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions) `Input``<``Object``[]``>`
    * [`cacheControl?`](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions-cachecontrol)
    * [`contentType?`](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions-contenttype)
    * [`files`](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions-files)
    * [`ignore?`](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions-ignore)
  * [`nonVersionedFilesCacheHeader?`](https://sst.dev/docs/component/aws/nextjs#assets-nonversionedfilescacheheader)
  * [`purge?`](https://sst.dev/docs/component/aws/nextjs#assets-purge)
  * [`textEncoding?`](https://sst.dev/docs/component/aws/nextjs#assets-textencoding)
  * [`versionedFilesCacheHeader?`](https://sst.dev/docs/component/aws/nextjs#assets-versionedfilescacheheader)


**Default** `Object`
Configure how the Next.js app assets are uploaded to S3.
By default, this is set to the following. Read more about these options below.
```

{

assets: {

textEncoding: "utf-8",

versionedFilesCacheHeader: "public,max-age=31536000,immutable",

nonVersionedFilesCacheHeader: "public,max-age=0,s-maxage=86400,stale-while-revalidate=8640"

}

}

```

Read more about these options below.
####  [assets.fileOptions?](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions)
**Type** `Input``<``Object``[]``>`
Specify the `Content-Type` and `Cache-Control` headers for specific files. This allows you to override the default behavior for specific files using glob patterns.
Apply `Cache-Control` and `Content-Type` to all zip files.
```

{

assets: {

fileOptions: [

{

files: "**/*.zip",

contentType: "application/zip",

cacheControl: "private,no-cache,no-store,must-revalidate"

}

]

}

}

```

Apply `Cache-Control` to all CSS and JS files except for CSS files with `index-` prefix in the `main/` directory.
```

{

assets: {

fileOptions: [

{

files: ["**/*.css", "**/*.js"],

ignore: "main/index-*.css",

cacheControl: "private,no-cache,no-store,must-revalidate"

}

]

}

}

```

#####  [assets.fileOptions[].cacheControl?](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions-cachecontrol)
**Type** `string`
The `Cache-Control` header to apply to the matched files.
#####  [assets.fileOptions[].contentType?](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions-contenttype)
**Type** `string`
The `Content-Type` header to apply to the matched files.
#####  [assets.fileOptions[].files](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions-files)
**Type** `string`` | ``string``[]`
A glob pattern or array of glob patterns of files to apply these options to.
#####  [assets.fileOptions[].ignore?](https://sst.dev/docs/component/aws/nextjs#assets-fileoptions-ignore)
**Type** `string`` | ``string``[]`
A glob pattern or array of glob patterns of files to exclude from the ones matched by the `files` glob pattern.
####  [assets.nonVersionedFilesCacheHeader?](https://sst.dev/docs/component/aws/nextjs#assets-nonversionedfilescacheheader)
**Type** `Input``<``string``>`
**Default** `“public,max-age=0,s-maxage=86400,stale-while-revalidate=8640”`
The `Cache-Control` header used for non-versioned files, like `index.html`. This is used by both CloudFront and the browser cache.
The default is set to not cache on browsers, and cache for 1 day on CloudFront.
```

{

assets: {

nonVersionedFilesCacheHeader: "public,max-age=0,no-cache"

}

}

```

####  [assets.purge?](https://sst.dev/docs/component/aws/nextjs#assets-purge)
**Type** `Input``<``boolean``>`
**Default** `true`
Configure if files from previous deployments should be purged from the bucket.
```

{

assets: {

purge: false

}

}

```

####  [assets.textEncoding?](https://sst.dev/docs/component/aws/nextjs#assets-textencoding)
**Type** `Input``<``“``utf-8``”`` | ``“``iso-8859-1``”`` | ``“``windows-1252``”`` | ``“``ascii``”`` | ``“``none``”``>`
**Default** `“utf-8”`
Character encoding for text based assets, like HTML, CSS, JS. This is used to set the `Content-Type` header when these files are served out.
If set to `"none"`, then no charset will be returned in header.
```

{

assets: {

textEncoding: "iso-8859-1"

}

}

```

####  [assets.versionedFilesCacheHeader?](https://sst.dev/docs/component/aws/nextjs#assets-versionedfilescacheheader)
**Type** `Input``<``string``>`
**Default** `“public,max-age=31536000,immutable”`
The `Cache-Control` header used for versioned files, like `main-1234.css`. This is used by both CloudFront and the browser cache.
The default `max-age` is set to 1 year.
```

{

assets: {

versionedFilesCacheHeader: "public,max-age=31536000,immutable"

}

}

```

### [buildCommand?](https://sst.dev/docs/component/aws/nextjs#buildcommand)
**Type** `Input``<``string``>`
**Default** `“npx —yes open-next@OPEN_NEXT_VERSION build”`
The command used internally to build your Next.js app. It uses OpenNext with the `openNextVersion`.
If you want to use a custom `build` script from your `package.json`. This is useful if you have a custom build process or want to use a different version of OpenNext. OpenNext by default uses the `build` script for building next-js app in your `package.json`. You can customize the build command in OpenNext configuration.
```

{

buildCommand: "npm run build:open-next"

}

```

### [cachePolicy?](https://sst.dev/docs/component/aws/nextjs#cachepolicy)
**Type** `Input``<``string``>`
**Default** A new cache policy is created
Configure the Next.js app to use an existing CloudFront cache policy.
CloudFront has a limit of 20 cache policies per account, though you can request a limit increase.
By default, a new cache policy is created for it. This allows you to reuse an existing policy instead of creating a new one.
```

{

cachePolicy: "658327ea-f89d-4fab-a63d-7e88639e58f6"

}

```

### [dev?](https://sst.dev/docs/component/aws/nextjs#dev)
**Type** `false`` | ``Object`
  * [`autostart?`](https://sst.dev/docs/component/aws/nextjs#dev-autostart)
  * [`command?`](https://sst.dev/docs/component/aws/nextjs#dev-command)
  * [`directory?`](https://sst.dev/docs/component/aws/nextjs#dev-directory)
  * [`title?`](https://sst.dev/docs/component/aws/nextjs#dev-title)
  * [`url?`](https://sst.dev/docs/component/aws/nextjs#dev-url)


Configure how this component works in `sst dev`.
In `sst dev` your Next.js app is run in dev mode; it’s not deployed.
Instead of deploying your Next.js app, this starts it in dev mode. It’s run as a separate process in the `sst dev` multiplexer. Read more about [`sst dev`](https://sst.dev/docs/reference/cli/#dev).
To disable dev mode, pass in `false`.
####  [dev.autostart?](https://sst.dev/docs/component/aws/nextjs#dev-autostart)
**Type** `Input``<``boolean``>`
**Default** `true`
Configure if you want to automatically start this when `sst dev` starts. You can still start it manually later.
####  [dev.command?](https://sst.dev/docs/component/aws/nextjs#dev-command)
**Type** `Input``<``string``>`
**Default** `“npm run dev”`
The command that `sst dev` runs to start this in dev mode.
####  [dev.directory?](https://sst.dev/docs/component/aws/nextjs#dev-directory)
**Type** `Input``<``string``>`
**Default** Uses the `path`
Change the directory from where the `command` is run.
####  [dev.title?](https://sst.dev/docs/component/aws/nextjs#dev-title)
**Type** `Input``<``string``>`
The title of the tab in the multiplexer.
####  [dev.url?](https://sst.dev/docs/component/aws/nextjs#dev-url)
**Type** `Input``<``string``>`
**Default** `“`
The `url` when this is running in dev mode.
Since this component is not deployed in `sst dev`, there is no real URL. But if you are using this component’s `url` or linking to this component’s `url`, it can be useful to have a placeholder URL. It avoids having to handle it being `undefined`.
### [domain?](https://sst.dev/docs/component/aws/nextjs#domain)
**Type** `Input``<``string`` | ``Object``>`
  * [`aliases?`](https://sst.dev/docs/component/aws/nextjs#domain-aliases)
  * [`cert?`](https://sst.dev/docs/component/aws/nextjs#domain-cert)
  * [`dns?`](https://sst.dev/docs/component/aws/nextjs#domain-dns)
  * [`name`](https://sst.dev/docs/component/aws/nextjs#domain-name)
  * [`redirects?`](https://sst.dev/docs/component/aws/nextjs#domain-redirects)


Set a custom domain for your Next.js app.
Automatically manages domains hosted on AWS Route 53, Cloudflare, and Vercel. For other providers, you’ll need to pass in a `cert` that validates domain ownership and add the DNS records.
Built-in support for AWS Route 53, Cloudflare, and Vercel. And manual setup for other providers.
By default this assumes the domain is hosted on Route 53.
```

{

domain: "example.com"

}

```

For domains hosted on Cloudflare.
```

{

domain: {

name: "example.com",

dns: sst.cloudflare.dns()

}

}

```

Specify a `www.` version of the custom domain.
```

{

domain: {

name: "domain.com",

redirects: ["www.domain.com"]

}

}

```

####  [domain.aliases?](https://sst.dev/docs/component/aws/nextjs#domain-aliases)
**Type** `Input``<``string``[]``>`
Alias domains that should be used. Unlike the `redirect` option, this keeps your visitors on this alias domain.
So if your users visit `app2.domain.com`, they will stay on `app2.domain.com` in their browser.
```

{

domain: {

name: "app1.domain.com",

aliases: ["app2.domain.com"]

}

}

```

####  [domain.cert?](https://sst.dev/docs/component/aws/nextjs#domain-cert)
**Type** `Input``<``string``>`
The ARN of an ACM (AWS Certificate Manager) certificate that proves ownership of the domain. By default, a certificate is created and validated automatically.
The certificate will be created in the `us-east-1` region as required by AWS CloudFront. If you are creating your own certificate, you must also create it in `us-east-1`.
You need to pass in a `cert` for domains that are not hosted on supported `dns` providers.
To manually set up a domain on an unsupported provider, you’ll need to:
  1. Once validated, set the certificate ARN as the `cert` and set `dns` to `false`.
  2. Add the DNS records in your provider to point to the CloudFront distribution URL.


```

{

domain: {

name: "domain.com",

dns: false,

cert: "arn:aws:acm:us-east-1:112233445566:certificate/3a958790-8878-4cdc-a396-06d95064cf63"

}

}

```

####  [domain.dns?](https://sst.dev/docs/component/aws/nextjs#domain-dns)
**Type** `Input``<``false`` | `[`sst.aws.dns`](https://sst.dev/docs/component/aws/dns/)` | `[`sst.cloudflare.dns`](https://sst.dev/docs/component/cloudflare/dns/)` | `[`sst.vercel.dns`](https://sst.dev/docs/component/vercel/dns/)`>`
**Default** `sst.aws.dns`
The DNS provider to use for the domain. Defaults to the AWS.
Takes an adapter that can create the DNS records on the provider. This can automate validating the domain and setting up the DNS routing.
Supports Route 53, Cloudflare, and Vercel adapters. For other providers, you’ll need to set `dns` to `false` and pass in a certificate validating ownership via `cert`.
Specify the hosted zone ID for the Route 53 domain.
```

{

domain: {

name: "example.com",

dns: sst.aws.dns({

zone: "Z2FDTNDATAQYW2"

})

}

}

```

Use a domain hosted on Cloudflare, needs the Cloudflare provider.
```

{

domain: {

name: "example.com",

dns: sst.cloudflare.dns()

}

}

```

Use a domain hosted on Vercel, needs the Vercel provider.
```

{

domain: {

name: "example.com",

dns: sst.vercel.dns()

}

}

```

####  [domain.name](https://sst.dev/docs/component/aws/nextjs#domain-name)
**Type** `Input``<``string``>`
The custom domain you want to use.
```

{

domain: {

name: "example.com"

}

}

```

Can also include subdomains based on the current stage.
```

{

domain: {

name: `${$app.stage}.example.com`

}

}

```

####  [domain.redirects?](https://sst.dev/docs/component/aws/nextjs#domain-redirects)
**Type** `Input``<``string``[]``>`
Alternate domains to be used. Visitors to the alternate domains will be redirected to the main `name`.
Unlike the `aliases` option, this will redirect visitors back to the main `name`.
Use this to create a `www.` version of your domain and redirect visitors to the apex domain.
```

{

domain: {

name: "domain.com",

redirects: ["www.domain.com"]

}

}

```

### [edge?](https://sst.dev/docs/component/aws/nextjs#edge)
**Type** `Input``<``Object``>`
  * [`viewerRequest?`](https://sst.dev/docs/component/aws/nextjs#edge-viewerrequest) `Input``<``Object``>`
    * [`injection`](https://sst.dev/docs/component/aws/nextjs#edge-viewerrequest-injection)
    * [`kvStore?`](https://sst.dev/docs/component/aws/nextjs#edge-viewerrequest-kvstore)
  * [`viewerResponse?`](https://sst.dev/docs/component/aws/nextjs#edge-viewerresponse) `Input``<``Object``>`
    * [`injection`](https://sst.dev/docs/component/aws/nextjs#edge-viewerresponse-injection)
    * [`kvStore?`](https://sst.dev/docs/component/aws/nextjs#edge-viewerresponse-kvstore)


Configure CloudFront Functions to customize the behavior of HTTP requests and responses at the edge.
####  [edge.viewerRequest?](https://sst.dev/docs/component/aws/nextjs#edge-viewerrequest)
**Type** `Input``<``Object``>`
Configure the viewer request function.
The viewer request function can be used to modify incoming requests before they reach your origin server. For example, you can redirect users, rewrite URLs, or add headers.
#####  [edge.viewerRequest.injection](https://sst.dev/docs/component/aws/nextjs#edge-viewerrequest-injection)
**Type** `Input``<``string``>`
The code to inject into the viewer request function.
By default, a viewer request function is created to:
  * Disable CloudFront default URL if custom domain is set
  * Add the `x-forwarded-host` header
  * Route assets requests to S3 (static files stored in the bucket)
  * Route server requests to server functions (dynamic rendering)


The function manages routing by:
  1. First checking if the requested path exists in S3 (with variations like adding index.html)
  2. Serving a custom 404 page from S3 if configured and the path isn’t found
  3. Routing image optimization requests to the image optimizer function
  4. Routing all other requests to the nearest server function


The given code will be injected at the beginning of this function.
```

asyncfunctionhandler(event) {

// User injected code

// Default behavior code

returnevent.request;

}

```

To add a custom header to all requests.
```

{

edge: {

viewerRequest: {

injection: `event.request.headers["x-foo"] = { value: "bar" };`

}

}

}

```

You can use this to add basic auth, [check out an example](https://sst.dev/docs/examples/#aws-nextjs-basic-auth).
#####  [edge.viewerRequest.kvStore?](https://sst.dev/docs/component/aws/nextjs#edge-viewerrequest-kvstore)
**Type** `Input``<``string``>`
The KV store to associate with the viewer request function.
```

{

edge: {

viewerRequest: {

kvStore: "arn:aws:cloudfront::123456789012:key-value-store/my-store"

}

}

}

```

####  [edge.viewerResponse?](https://sst.dev/docs/component/aws/nextjs#edge-viewerresponse)
**Type** `Input``<``Object``>`
Configure the viewer response function.
The viewer response function can be used to modify outgoing responses before they are sent to the client. For example, you can add security headers or change the response status code.
By default, no viewer response function is set. A new function will be created with the provided code.
#####  [edge.viewerResponse.injection](https://sst.dev/docs/component/aws/nextjs#edge-viewerresponse-injection)
**Type** `Input``<``string``>`
The code to inject into the viewer response function.
```

asyncfunctionhandler(event) {

// User injected code

returnevent.response;

}

```

To add a custom header to all responses.
```

{

edge: {

viewerResponse: {

injection: `event.response.headers["x-foo"] = { value: "bar" };`

}

}

}

```

#####  [edge.viewerResponse.kvStore?](https://sst.dev/docs/component/aws/nextjs#edge-viewerresponse-kvstore)
**Type** `Input``<``string``>`
The KV store to associate with the viewer response function.
```

{

edge: {

viewerResponse: {

kvStore: "arn:aws:cloudfront::123456789012:key-value-store/my-store"

}

}

}

```

### [environment?](https://sst.dev/docs/component/aws/nextjs#environment)
**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Set 
  1. In `next build`, they are loaded into `process.env`.
  2. Locally while running through `sst dev`.


You can also `link` resources to your Next.js app and access them in a type-safe way with the [SDK](https://sst.dev/docs/reference/sdk/). We recommend linking since it’s more secure.
Recall that in Next.js, you need to prefix your environment variables with `NEXT_PUBLIC_` to access these in the browser. 
```

{

environment: {

API_URL: api.url,

// Accessible in the browser

NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY: "pk_test_123"

}

}

```

### [imageOptimization?](https://sst.dev/docs/component/aws/nextjs#imageoptimization)
**Type** `Object`
  * [`memory?`](https://sst.dev/docs/component/aws/nextjs#imageoptimization-memory)
  * [`staticEtag?`](https://sst.dev/docs/component/aws/nextjs#imageoptimization-staticetag)


**Default** `{memory: “1024 MB”}`
Configure the Lambda function used for image optimization.
####  [imageOptimization.memory?](https://sst.dev/docs/component/aws/nextjs#imageoptimization-memory)
**Type** `“``${number} MB``”`` | ``“``${number} GB``”`
**Default** `“1536 MB”`
The amount of memory allocated to the image optimization function. Takes values between 128 MB and 10240 MB in 1 MB increments.
```

{

imageOptimization: {

memory: "512 MB"

}

}

```

####  [imageOptimization.staticEtag?](https://sst.dev/docs/component/aws/nextjs#imageoptimization-staticetag)
**Type** `boolean`
**Default** `false`
If set to true, a previously computed image will return _304 Not Modified_. This means that image needs to be **immutable**.
The etag will be computed based on the image href, format and width and the next BUILD_ID.
```

{

imageOptimization: {

staticEtag: true,

}

}

```

### [invalidation?](https://sst.dev/docs/component/aws/nextjs#invalidation)
**Type** `Input``<``false`` | ``Object``>`
  * [`paths?`](https://sst.dev/docs/component/aws/nextjs#invalidation-paths)
  * [`wait?`](https://sst.dev/docs/component/aws/nextjs#invalidation-wait)


**Default** `{paths: “all”, wait: false}`
Configure how the CloudFront cache invalidations are handled. This is run after your Next.js app has been deployed.
You get 1000 free invalidations per month. After that you pay $0.005 per invalidation path. 
Turn off invalidations.
```

{

invalidation: false

}

```

Wait for all paths to be invalidated.
```

{

invalidation: {

paths: "all",

wait: true

}

}

```

####  [invalidation.paths?](https://sst.dev/docs/component/aws/nextjs#invalidation-paths)
**Type** `Input``<``string``[]`` | ``“``all``”`` | ``“``versioned``”``>`
**Default** `“all”`
The paths to invalidate.
You can either pass in an array of glob patterns to invalidate specific files. Or you can use one of these built-in options:
  * `all`: All files will be invalidated when any file changes
  * `versioned`: Only versioned files will be invalidated when versioned files change


Each glob pattern counts as a single invalidation. Whereas, invalidating `/*` counts as a single invalidation.
Invalidate the `index.html` and all files under the `products/` route.
```

{

invalidation: {

paths: ["/index.html", "/products/*"]

}

}

```

This counts as two invalidations.
####  [invalidation.wait?](https://sst.dev/docs/component/aws/nextjs#invalidation-wait)
**Type** `Input``<``boolean``>`
**Default** `false`
Configure if `sst deploy` should wait for the CloudFront cache invalidation to finish.
For non-prod environments it might make sense to pass in `false`.
Waiting for this process to finish ensures that new content will be available after the deploy finishes. However, this process can sometimes take more than 5 mins.
```

{

invalidation: {

wait: true

}

}

```

### [link?](https://sst.dev/docs/component/aws/nextjs#link)
**Type** `Input``<``any``[]``>`
[Link resources](https://sst.dev/docs/linking/) to your Next.js app. This will:
  1. Grant the permissions needed to access the resources.
  2. Allow you to access it in your site using the [SDK](https://sst.dev/docs/reference/sdk/).


Takes a list of resources to link to the function.
```

{

link: [bucket, stripeKey]

}

```

### [openNextVersion?](https://sst.dev/docs/component/aws/nextjs#opennextversion)
**Type** `Input``<``string``>`
**Default** The latest version of OpenNext pinned to the version of SST you are using.
Configure the 
This does not automatically update to the latest OpenNext version. It remains pinned to the version of SST you have.
By default, this is pinned to the version of OpenNext that was released with the SST version you are using. You can `DEFAULT_OPEN_NEXT_VERSION`. OpenNext changed its package name from `open-next` to `@opennextjs/aws` in version `3.1.4`. SST will choose the correct one based on the version you provide.
```

{

openNextVersion: "3.4.1"

}

```

### [path?](https://sst.dev/docs/component/aws/nextjs#path)
**Type** `Input``<``string``>`
**Default** `”.”`
Path to the directory where your Next.js app is located. This path is relative to your `sst.config.ts`.
By default this assumes your Next.js app is in the root of your SST app.
If your Next.js app is in a package in your monorepo.
```

{

path: "packages/web"

}

```

### [permissions?](https://sst.dev/docs/component/aws/nextjs#permissions)
**Type** `Input``<``Object``[]``>`
  * [`actions`](https://sst.dev/docs/component/aws/nextjs#permissions-actions)
  * [`effect?`](https://sst.dev/docs/component/aws/nextjs#permissions-effect)
  * [`resources`](https://sst.dev/docs/component/aws/nextjs#permissions-resources)


Permissions and the resources that the [server function](https://sst.dev/docs/component/aws/nextjs#nodes-server) in your Next.js app needs to access. These permissions are used to create the function’s IAM role.
If you `link` the function to a resource, the permissions to access it are automatically added.
Allow reading and writing to an S3 bucket called `my-bucket`.
```

{

permissions: [

{

actions: ["s3:GetObject", "s3:PutObject"],

resources: ["arn:aws:s3:::my-bucket/*"]

},

]

}

```

Perform all actions on an S3 bucket called `my-bucket`.
```

{

permissions: [

{

actions: ["s3:*"],

resources: ["arn:aws:s3:::my-bucket/*"]

},

]

}

```

Grant permissions to access all resources.
```

{

permissions: [

{

actions: ["*"],

resources: ["*"]

},

]

}

```

####  [permissions[].actions](https://sst.dev/docs/component/aws/nextjs#permissions-actions)
**Type** `string``[]`
The 
```

{

actions: ["s3:*"]

}

```

####  [permissions[].effect?](https://sst.dev/docs/component/aws/nextjs#permissions-effect)
**Type** `“``allow``”`` | ``“``deny``”`
**Default** `“allow”`
Configures whether the permission is allowed or denied.
```

{

effect: "deny"

}

```

####  [permissions[].resources](https://sst.dev/docs/component/aws/nextjs#permissions-resources)
**Type** `Input``<``Input``<``string``>``[]``>`
The resourcess specified using the 
```

{

resources: ["arn:aws:s3:::my-bucket/*"]

}

```

### [regions?](https://sst.dev/docs/component/aws/nextjs#regions)
**Type** `Input``<``string``[]``>`
**Default** The default region of the SST app
Regions that the server function will be deployed to.
By default, the server function is deployed to a single region, this is the default region of your SST app.
This does not use Lambda@Edge, it deploys multiple Lambda functions instead.
To deploy it to multiple regions, you can pass in a list of regions. And any requests made will be routed to the nearest region based on the user’s location.
```

{

regions: ["us-east-1", "eu-west-1"]

}

```

### [router?](https://sst.dev/docs/component/aws/nextjs#router)
**Type** `Object`
  * [`domain?`](https://sst.dev/docs/component/aws/nextjs#router-domain)
  * [`instance`](https://sst.dev/docs/component/aws/nextjs#router-instance)
  * [`path?`](https://sst.dev/docs/component/aws/nextjs#router-path)


Serve your Next.js app through a `Router` instead of a standalone CloudFront distribution.
By default, this component creates a new CloudFront distribution. But you might want to serve it through the distribution of your `Router` as a:
  * A path like `/docs`
  * A subdomain like `docs.example.com`
  * Or a combined pattern like `dev.example.com/docs`


To serve your Next.js app **from a path** , you’ll need to configure the root domain in your `Router` component.
sst.config.ts
```typescript


const router = newsst.aws.Router("Router", {




"example.com"




});


```

Now set the `router` and the `path`.

```

{


router: {


instance: router,



path: "/docs"



}


}

```

You also need to set the `next.config.js`.
If routing to a path, you need to set that as the base path in your Next.js app as well.
next.config.js```

exportdefaultdefineConfig({

basePath: "/docs"

});

```

To serve your Next.js app **from a subdomain** , you’ll need to configure the domain in your `Router` component to match both the root and the subdomain.
sst.config.ts
```typescript


const router = newsst.aws.Router("Router", {



domain: {



"example.com",




 ["*.example.com"]



}



});


```

Now set the `domain` in the `router` prop.

```

{


router: {


instance: router,



domain: "docs.example.com"



}


}

```

Finally, to serve your Next.js app **from a combined pattern** like `dev.example.com/docs`, you’ll need to configure the domain in your `Router` to match the subdomain.
sst.config.ts

```typescript

const router = newsst.aws.Router("Router", {

domain: {

"example.com",

 ["*.example.com"]

}

});

```

And set the `domain` and the `path`.

```

{

router: {

instance: router,

domain: "dev.example.com",

path: "/docs"

}

}

```

Also, make sure to set this as the `basePath` in your `next.config.js`, like above.

#### [router.domain?](https://sst.dev/docs/component/aws/nextjs#router-domain)

**Type** `Input``<``string``>`
Route requests matching a specific domain pattern.
You can serve your resource from a subdomain. For example, if you want to make it available at `https://dev.example.com`, set the `Router` to match the domain or a wildcard.
sst.config.ts

```typescript


const router = newsst.aws.Router("MyRouter", {




"*.example.com"




});


```

Then set the domain pattern.

```

router: {


instance: router,



domain: "dev.example.com"



}

```

While `dev.example.com` matches `*.example.com`. Something like `docs.dev.example.com` will not match `*.example.com`.
Nested wildcards domain patterns are not supported.
You’ll need to add `*.dev.example.com` as an alias.

#### [router.instance](https://sst.dev/docs/component/aws/nextjs#router-instance)

**Type** `Input``<`[`Router`](https://sst.dev/docs/component/aws/router)`>`
The `Router` component to use for routing requests.
Let’s say you have a Router component.
sst.config.ts

```typescript

const router = newsst.aws.Router("MyRouter", {

domain: "example.com"

});

```

You can attach it to the Router, instead of creating a standalone CloudFront distribution.

```

router: {

instance: router

}

```

#### [router.path?](https://sst.dev/docs/component/aws/nextjs#router-path)

**Type** `Input``<``string``>`
**Default** `”/”`
Route requests matching a specific path prefix.

```

router: {

instance: router,

path: "/docs"

}

```

### [server?](https://sst.dev/docs/component/aws/nextjs#server)

**Type** `Object`

* [`architecture?`](https://sst.dev/docs/component/aws/nextjs#server-architecture)
* [`install?`](https://sst.dev/docs/component/aws/nextjs#server-install)
* [`layers?`](https://sst.dev/docs/component/aws/nextjs#server-layers)
* [`loader?`](https://sst.dev/docs/component/aws/nextjs#server-loader)
* [`memory?`](https://sst.dev/docs/component/aws/nextjs#server-memory)
* [`runtime?`](https://sst.dev/docs/component/aws/nextjs#server-runtime)
* [`timeout?`](https://sst.dev/docs/component/aws/nextjs#server-timeout)

**Default** `{architecture: “x86_64”, memory: “1024 MB”}`
Configure the Lambda function used for server.

#### [server.architecture?](https://sst.dev/docs/component/aws/nextjs#server-architecture)

**Type** `Input``<``“``x86_64``”`` | ``“``arm64``”``>`
**Default** `“x86_64”`
The

```

{

server: {

architecture: "arm64"

}

}

```

#### [server.install?](https://sst.dev/docs/component/aws/nextjs#server-install)

**Type** `Input``<``string``[]``>`
Dependencies that need to be excluded from the server function package.
Certain npm packages cannot be bundled using esbuild. This allows you to exclude them from the bundle. Instead they’ll be moved into a `node_modules/` directory in the function package.
If esbuild is giving you an error about a package, try adding it to the `install` list.
This will allow your functions to be able to use these dependencies when deployed. They just won’t be tree shaken. You however still need to have them in your `package.json`.
Packages listed here still need to be in your `package.json`.
Esbuild will ignore them while traversing the imports in your code. So these are the **package names as seen in the imports**. It also works on packages that are not directly imported by your code.

```

{

server: {

install: ["sharp"]

}

}

```

#### [server.layers?](https://sst.dev/docs/component/aws/nextjs#server-layers)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of Lambda layer ARNs to add to the server function.

```

{

server: {

layers: ["arn:aws:lambda:us-east-1:123456789012:layer:my-layer:1"]

}

}

```

#### [server.loader?](https://sst.dev/docs/component/aws/nextjs#server-loader)

**Type** `Input``<``Record``<``string`, `>``>`
Configure additional esbuild loaders for other file extensions. This is useful when your code is importing non-JS files like `.png`, `.css`, etc.

```

{

server: {

loader: {

".png": "file"

}

}

}

```

#### [server.memory?](https://sst.dev/docs/component/aws/nextjs#server-memory)

**Type** `Input``<``“``${number} MB``”`` | ``“``${number} GB``”``>`
**Default** `“1024 MB”`
The amount of memory allocated to the server function. Takes values between 128 MB and 10240 MB in 1 MB increments.

```

{

server: {

memory: "2048 MB"

}

}

```

#### [server.runtime?](https://sst.dev/docs/component/aws/nextjs#server-runtime)

**Type** `Input``<``“``nodejs18.x``”`` | ``“``nodejs20.x``”`` | ``“``nodejs22.x``”``>`
**Default** `“nodejs20.x”`
The runtime environment for the server function.

```

{

server: {

runtime: "nodejs22.x"

}

}

```

#### [server.timeout?](https://sst.dev/docs/component/aws/nextjs#server-timeout)

**Type** `Input``<``“``${number} minute``”`` | ``“``${number} minutes``”`` | ``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“20 seconds”`
The maximum amount of time the server function can run.
While Lambda supports timeouts up to 900 seconds, your requests are served through AWS CloudFront. And it has a default limit of 60 seconds.
If you set a timeout that’s longer than 60 seconds, this component will check if your account can allow for that timeout. If not, it’ll throw an error.
If you need a timeout longer than 60 seconds, you’ll need to request a limit increase.
You can increase this to 180 seconds for your account by contacting AWS Support and

```

{

server: {

timeout: "50 seconds"

}

}

```

If you need a timeout longer than what CloudFront supports, we recommend using a separate Lambda `Function` with the `url` enabled instead.

### [transform?](https://sst.dev/docs/component/aws/nextjs#transform)

**Type** `Object`

* [`assets?`](https://sst.dev/docs/component/aws/nextjs#transform-assets)
* [`cdn?`](https://sst.dev/docs/component/aws/nextjs#transform-cdn)
* [`server?`](https://sst.dev/docs/component/aws/nextjs#transform-server)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.assets?](https://sst.dev/docs/component/aws/nextjs#transform-assets)

**Type** [`BucketArgs`](https://sst.dev/docs/component/aws/bucket#bucketargs)` | ``(``args``: `[`BucketArgs`](https://sst.dev/docs/component/aws/bucket#bucketargs)`, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Bucket resource used for uploading the assets.

#### [transform.cdn?](https://sst.dev/docs/component/aws/nextjs#transform-cdn)

**Type** [`CdnArgs`](https://sst.dev/docs/component/aws/cdn#cdnargs)` | ``(``args``: `[`CdnArgs`](https://sst.dev/docs/component/aws/cdn#cdnargs)`, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the CloudFront CDN resource.

#### [transform.server?](https://sst.dev/docs/component/aws/nextjs#transform-server)

**Type** [`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)` | ``(``args``: `[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the server Function resource.

### [vpc?](https://sst.dev/docs/component/aws/nextjs#vpc)

**Type** [`Vpc`](https://sst.dev/docs/component/aws/vpc)`| ``Input``<``Object``>`

* [`privateSubnets`](https://sst.dev/docs/component/aws/nextjs#vpc-privatesubnets)
* [`securityGroups`](https://sst.dev/docs/component/aws/nextjs#vpc-securitygroups)

Configure the server function to connect to private subnets in a virtual private cloud or VPC. This allows it to access private resources.
Create a `Vpc` component.
sst.config.ts

```typescript


const myVpc = newsst.aws.Vpc("MyVpc");


```

Or reference an existing VPC.
sst.config.ts

```typescript

const myVpc = sst.aws.Vpc.get("MyVpc", {

id: "vpc-12345678901234567"

});

```

And pass it in.

```

{

vpc: myVpc

}

```

#### [vpc.privateSubnets](https://sst.dev/docs/component/aws/nextjs#vpc-privatesubnets)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of VPC subnet IDs.

#### [vpc.securityGroups](https://sst.dev/docs/component/aws/nextjs#vpc-securitygroups)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of VPC security group IDs.

### [warm?](https://sst.dev/docs/component/aws/nextjs#warm)

**Type** `Input``<``number``>`
**Default** `0`
The number of instances of the [server function](https://sst.dev/docs/component/aws/nextjs#nodes-server) to keep warm. This is useful for cases where you are experiencing long cold starts. The default is to not keep any instances warm.
This works by starting a serverless cron job to make _n_ concurrent requests to the server function every few minutes. Where _n_ is the number of instances to keep warm.

## [Properties](https://sst.dev/docs/component/aws/nextjs#properties)

### [nodes](https://sst.dev/docs/component/aws/nextjs#nodes)

**Type** `Object`

* [`assets`](https://sst.dev/docs/component/aws/nextjs#nodes-assets)
* [`cdn`](https://sst.dev/docs/component/aws/nextjs#nodes-cdn)
* [`revalidationFunction`](https://sst.dev/docs/component/aws/nextjs#nodes-revalidationfunction)
* [`revalidationQueue`](https://sst.dev/docs/component/aws/nextjs#nodes-revalidationqueue)
* [`revalidationTable`](https://sst.dev/docs/component/aws/nextjs#nodes-revalidationtable)
* [`server`](https://sst.dev/docs/component/aws/nextjs#nodes-server)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.assets](https://sst.dev/docs/component/aws/nextjs#nodes-assets)

**Type** `undefined`` |`[`Bucket`](https://sst.dev/docs/component/aws/bucket)
The Amazon S3 Bucket that stores the assets.

#### [nodes.cdn](https://sst.dev/docs/component/aws/nextjs#nodes-cdn)

**Type** `undefined`` |`[`Cdn`](https://sst.dev/docs/component/aws/cdn)
The Amazon CloudFront CDN that serves the site.

#### [nodes.revalidationFunction](https://sst.dev/docs/component/aws/nextjs#nodes-revalidationfunction)

**Type** `undefined`` | ``Output``<``undefined`` |`[`Function`](https://sst.dev/docs/component/aws/function)`>`
The Lambda function that processes the ISR revalidation.

#### [nodes.revalidationQueue](https://sst.dev/docs/component/aws/nextjs#nodes-revalidationqueue)

**Type** `undefined`` | ``Output``<``undefined`` |`[`Queue`](https://sst.dev/docs/component/aws/queue)`>`
The Amazon SQS queue that triggers the ISR revalidator.

#### [nodes.revalidationTable](https://sst.dev/docs/component/aws/nextjs#nodes-revalidationtable)

**Type** `undefined`` | ``Output``<``undefined`` | ``>`
The Amazon DynamoDB table that stores the ISR revalidation data.

#### [nodes.server](https://sst.dev/docs/component/aws/nextjs#nodes-server)

**Type** `undefined`` | ``Output``<`[`Function`](https://sst.dev/docs/component/aws/function)`>`
The AWS Lambda server function that renders the site.

### [url](https://sst.dev/docs/component/aws/nextjs#url)

**Type** `Output``<``string``>`
The URL of the Next.js app.
If the `domain` is set, this is the URL with the custom domain. Otherwise, it’s the auto-generated CloudFront URL.

## [SDK](https://sst.dev/docs/component/aws/nextjs#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/nextjs#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `url` `string`
The URL of the Next.js app.
If the `domain` is set, this is the URL with the custom domain. Otherwise, it’s the auto-generated CloudFront URL.

[Skip to content](https://sst.dev/docs/start/aws/bun#_top)

# Bun on AWS with SST

We are going to build an app with Bun, add an S3 Bucket for file uploads, and deploy it to AWS in a container with SST.
You can
Before you get started, make sure to [configure your AWS credentials](https://sst.dev/docs/iam-credentials#credentials).
* * *

#### [Examples](https://sst.dev/docs/start/aws/bun#examples)

We also have a few other Bun examples that you can refer to.

* [Deploy Bun with Elysia in a container](https://sst.dev/docs/examples/#aws-bun-elysia-container)
* [Build a hit counter with Bun and Redis](https://sst.dev/docs/examples/#aws-bun-redis)

* * *

## [1. Create a project](https://sst.dev/docs/start/aws/bun#1-create-a-project)

Let’s start by creating our Bun app.
Terminal window```

mkdiraws-bun && cdaws-bun

buninit-y

```

* * *

#### [Init Bun Serve](https://sst.dev/docs/start/aws/bun#init-bun-serve)

Replace your `index.ts` with the following.
index.ts
```typescript

const server = Bun.serve({

async fetch(req) {

consturl = newURL(req.url);

if (url.pathname === "/" && req.method === "GET") {

return newResponse("Hello World!");

}

return newResponse("404!");

},

});

console.log(`Listening on ${server.url}`);

```

This starts up an HTTP server by default on port `3000`.
* * *

#### [Add scripts](https://sst.dev/docs/start/aws/bun#add-scripts)

Add the following to your `package.json`.
package.json```

"scripts": {

"dev": "bun run --watch index.ts"

},

```

This adds a `dev` script with a watcher.
* * *

#### [Init SST](https://sst.dev/docs/start/aws/bun#init-sst)

Now let’s initialize SST in our app.
Terminal window```

bunxsstinit

buninstall

```

This’ll create an `sst.config.ts` file in your project root and install SST.
* * *

## [2. Add a Service](https://sst.dev/docs/start/aws/bun#2-add-a-service)

To deploy our Bun app, let’s add an `sst.config.ts`.
sst.config.ts

```typescript


asyncrun() {




const vpc = newsst.aws.Vpc("MyVpc");




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




newsst.aws.Service("MyService", {




cluster,



loadBalancer: {



ports: [{ listen: "80/http", forward: "3000/http" }],



},


dev: {



command: "bun dev",



},


});


}

```

This creates a VPC with an ECS Cluster, and adds a Fargate service to it.
By default, your service in not deployed when running in _dev_.
The `dev.command` tells SST to instead run our Bun app locally in dev mode.
* * *

#### [Start dev mode](https://sst.dev/docs/start/aws/bun#start-dev-mode)

Run the following to start dev mode. This’ll start SST and your Bun app.
Terminal window```

bunsstdev

```

Once complete, click on **MyService** in the sidebar and open your Bun app in your browser.
* * *
## [3. Add an S3 Bucket](https://sst.dev/docs/start/aws/bun#3-add-an-s3-bucket)
Let’s add an S3 Bucket for file uploads. Add this to your `sst.config.ts` below the `Vpc` component.
sst.config.ts
```typescript


const bucket = newsst.aws.Bucket("MyBucket");


```

* * *

#### [Link the bucket](https://sst.dev/docs/start/aws/bun#link-the-bucket)

Now, link the bucket to the container.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

// ...

link: [bucket],

});

```

This will allow us to reference the bucket in our Bun app.
* * *

## [4. Upload a file](https://sst.dev/docs/start/aws/bun#4-upload-a-file)

We want a `POST` request made to the `/` route to upload a file to our S3 bucket. Let’s add this below our _Hello World_ route in our `index.ts`.
index.ts

```typescript


if (url.pathname==="/"&& req.method==="POST") {




const formData = await req.formData();




const file = formData.get("file")! as File;




const params = {




Resource.MyBucket.name,




ContentType: file.type,




Key: file.name,




Body: file,




};




const upload = newUpload({




params,




client: s3,




});




await upload.done();




returnnewResponse("File uploaded successfully.");



}

```

We are directly accessing our S3 bucket with `Resource.MyBucket.name`.
Add the imports. We’ll use the extra ones below.
index.ts

```typescript

import { Resource } from"sst";

import {

S3Client,

GetObjectCommand,

ListObjectsV2Command,

} from"@aws-sdk/client-s3";

import { Upload } from"@aws-sdk/lib-storage";

import { getSignedUrl } from"@aws-sdk/s3-request-presigner";

const s3 = newS3Client();

```

And install the npm packages.
Terminal window```

buninstall@aws-sdk/client-s3@aws-sdk/lib-storage@aws-sdk/s3-request-presigner

```

* * *

## [5. Download the file](https://sst.dev/docs/start/aws/bun#5-download-the-file)

We’ll add a `/latest` route that’ll download the latest file in our S3 bucket. Let’s add this below our upload route in `index.ts`.
index.ts
```typescript

if (url.pathname==="/latest"&& req.method==="GET") {

const objects = await s3.send(

newListObjectsV2Command({

Bucket: Resource.MyBucket.name,

}),

);

const latestFile = objects.Contents!.sort(

(a, b) =>

(b.LastModified?.getTime() ?? 0) - (a.LastModified?.getTime() ?? 0),

)[0];

const command = newGetObjectCommand({

Key: latestFile.Key,

Bucket: Resource.MyBucket.name,

});

return Response.redirect(awaitgetSignedUrl(s3, command));

}

```

* * *

#### [Test your app](https://sst.dev/docs/start/aws/bun#test-your-app)

To upload a file run the following from your project root.
Terminal window```

curl-Ffile=@package.jsonhttp://localhost:3000/

```

This should upload the `package.json`. Now head over to `http://localhost:3000/latest` in your browser and it’ll show you what you just uploaded.
![SST Bun app file upload](https://sst.dev/_astro/start-bun-app-file-upload.3Vs-WnhI_1VfJ84.webp)
* * *

## [6. Deploy your app](https://sst.dev/docs/start/aws/bun#6-deploy-your-app)

To deploy our app we’ll first add a `Dockerfile`.
Dockerfile```

FROM oven/bun

COPY bun.lock .

COPY package.json .

RUN bun install --frozen-lockfile

COPY . .

EXPOSE 3000

CMD ["bun", "index.ts"]

```

This is a pretty basic setup. You can refer to the
You need to be running
Let’s also add a `.dockerignore` file in the root.
.dockerignore```

node_modules

.git

.gitignore

README.md

Dockerfile*

```

Now to build our Docker image and deploy we run:
Terminal window```

bunsstdeploy--stageproduction

```

You can use any stage name here but it’s good to create a new stage for production. This’ll give the URL of your Bun app deployed as a Fargate service.
Terminal window```

✓Complete

MyService:<http://prod-MyServiceLoadBalanc-491430065.us-east-1.elb.amazonaws.com>

```

Congrats! Your app should now be live!
* * *

## [Connect the console](https://sst.dev/docs/start/aws/bun#connect-the-console)

As a next step, you can setup the [SST Console](https://sst.dev/docs/console/) to _**git push to deploy**_ your app and view logs from it.
![SST Console Autodeploy](https://sst.dev/_astro/sst-console-autodeploy.DTgdy-D4_Z107cYw.webp)
You can [create a free account](https://console.sst.dev) and connect it to your AWS account.

[Skip to content](https://sst.dev/docs/start/aws/nextjs#_top)

# Next.js on AWS with SST

There are two ways to deploy a Next.js app to AWS with SST.

  1. [Serverless with OpenNext](https://sst.dev/docs/start/aws/nextjs#serverless)
  2. [Containers with Docker](https://sst.dev/docs/start/aws/nextjs#containers)

We’ll use both to build a couple of simple apps below.
* * *

#### [Examples](https://sst.dev/docs/start/aws/nextjs#examples)

We also have a few other Next.js examples that you can refer to.

* [Adding basic auth to your Next.js app](https://sst.dev/docs/examples/#aws-nextjs-basic-auth)
* [Enabling streaming in your Next.js app](https://sst.dev/docs/examples/#aws-nextjs-streaming)
* [Add additional routes to the Next.js CDN](https://sst.dev/docs/examples/#aws-nextjs-add-behavior)
* [Hit counter with Redis and Next.js in a container](https://sst.dev/docs/examples/#aws-nextjs-container-with-redis)

* * *

## [Serverless](https://sst.dev/docs/start/aws/nextjs#serverless)

We are going to create a Next.js app, add an S3 Bucket for file uploads, and deploy it using `Nextjs` component.
You can
Before you get started, make sure to [configure your AWS credentials](https://sst.dev/docs/iam-credentials#credentials).
* * *

### [1. Create a project](https://sst.dev/docs/start/aws/nextjs#1-create-a-project)

Let’s start by creating our app.
Terminal window```

npxcreate-next-app@latestaws-nextjs

cdaws-nextjs

```

We are picking **TypeScript** and not selecting **ESLint**.
* * *

##### [Init SST](https://sst.dev/docs/start/aws/nextjs#init-sst)

Now let’s initialize SST in our app.
Terminal window```

npxsst@latestinit

```

Select the defaults and pick **AWS**. This’ll create a `sst.config.ts` file in your project root.
* * *

##### [Start dev mode](https://sst.dev/docs/start/aws/nextjs#start-dev-mode)

Run the following to start dev mode. This’ll start SST and your Next.js app.
Terminal window```

npxsstdev

```

Once complete, click on **MyWeb** in the sidebar and open your Next.js app in your browser.
* * *

### [2. Add an S3 Bucket](https://sst.dev/docs/start/aws/nextjs#2-add-an-s3-bucket)

Let’s allow public `access` to our S3 Bucket for file uploads. Update your `sst.config.ts`.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket", {




access: "public"




});


```

Add this above the `Nextjs` component.

##### [Link the bucket](https://sst.dev/docs/start/aws/nextjs#link-the-bucket)

Now, link the bucket to our Next.js app.
sst.config.ts

```typescript

newsst.aws.Nextjs("MyWeb", {

link: [bucket]

});

```

* * *

### [3. Create an upload form](https://sst.dev/docs/start/aws/nextjs#3-create-an-upload-form)

Add a form client component in `components/form.tsx`.
components/form.tsx```

"use client";

import styles from"./form.module.css";

exportdefaultfunctionForm({ url }: { url:string }) {

return (

<form

className={styles.form}

onSubmit={async(e)=> {

e.preventDefault();

const file = (e.target as HTMLFormElement).file.files?.[0] ?? null;

const image = await fetch(url, {

body: file,

method: "PUT",

headers: {

"Content-Type": file.type,

"Content-Disposition": `attachment; filename="${file.name}"`,

},

});

window.location.href=image.url.split["?"](0);

}}

>

<inputname="file"type="file"accept="image/png, image/jpeg" />

<buttontype="submit">Upload</button>

</form>

);

}

```

Add some styles.
components/form.module.css```

.form {

padding: 2rem;

border-radius: 0.5rem;

background-color: var(--gray-alpha-100);

}

.forminput {

margin-right: 1rem;

}

.formbutton {

appearance: none;

padding: 0.5rem0.75rem;

font-weight: 500;

font-size: 0.875rem;

border-radius: 0.375rem;

background-color: transparent;

font-family: var(--font-geist-sans);

border: 1pxsolidvar(--gray-alpha-200);

}

.formbutton:active:enabled {

background-color: var(--gray-alpha-200);

}

```

* * *

### [4. Generate a pre-signed URL](https://sst.dev/docs/start/aws/nextjs#4-generate-a-pre-signed-url)

When our app loads, we’ll generate a pre-signed URL for the file upload and render the form with it. Replace your `Home` component in `app/page.tsx`.
app/page.tsx```

export const dynamic = "force-dynamic";

exportdefaultasyncfunctionHome() {

const command = newPutObjectCommand({

Key: crypto.randomUUID(),

Resource.MyBucket.name,

});

const url = await getSignedUrl(newS3Client({}),command);

return (

<div className={styles.page}>

<main className={styles.main}>

<Form url={url} />

</main>

</div>

);

}

```

We need the `force-dynamic` because we don’t want Next.js to cache the pre-signed URL.
We are directly accessing our S3 bucket with `Resource.MyBucket.name`.
Add the relevant imports.
app/page.tsx```

import { Resource } from"sst";

import Form from"@/components/form";

import { getSignedUrl } from"@aws-sdk/s3-request-presigner";

import { S3Client, PutObjectCommand } from"@aws-sdk/client-s3";

```

And install the npm packages.
Terminal window```

npminstall@aws-sdk/client-s3@aws-sdk/s3-request-presigner

```

* * *

#### [Test your app](https://sst.dev/docs/start/aws/nextjs#test-your-app)

Head over to the local Next.js app in your browser, `http://localhost:3000` and try **uploading an image**. You should see it upload and then download the image.
![SST Next.js app local](https://sst.dev/_astro/start-nextjs-local.jNuBVnOP_PRG6H.webp)
* * *

### [5. Deploy your app](https://sst.dev/docs/start/aws/nextjs#5-deploy-your-app)

Now let’s deploy your app to AWS.
Terminal window```

npxsstdeploy--stageproduction

```

You can use any stage name here but it’s good to create a new stage for production.
Congrats! Your app should now be live!
* * *

## [Containers](https://sst.dev/docs/start/aws/nextjs#containers)

We are going to create a Next.js app, add an S3 Bucket for file uploads, and deploy it in a container with the `Cluster` component.
You can
Before you get started, make sure to [configure your AWS credentials](https://sst.dev/docs/iam-credentials#credentials).
* * *

### [1. Create a project](https://sst.dev/docs/start/aws/nextjs#1-create-a-project-1)

Let’s start by creating our app.
Terminal window```

npxcreate-next-app@latestaws-nextjs-container

cdaws-nextjs-container

```

We are picking **TypeScript** and not selecting **ESLint**.
* * *

##### [Init SST](https://sst.dev/docs/start/aws/nextjs#init-sst-1)

Now let’s initialize SST in our app.
Terminal window```

npxsst@latestinit

```

Select the defaults and pick **AWS**. This’ll create a `sst.config.ts` file in your project root.
* * *

### [2. Add a Service](https://sst.dev/docs/start/aws/nextjs#2-add-a-service)

To deploy our Next.js app in a container, we’ll use `run` function in your `sst.config.ts`.
sst.config.ts

```typescript


asyncrun() {




const vpc = newsst.aws.Vpc("MyVpc");




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




newsst.aws.Service("MyService", {




cluster,



loadBalancer: {



ports: [{ listen: "80/http", forward: "3000/http" }],



},


dev: {



command: "npm run dev",



},


});


}

```

This creates a VPC, and an ECS Cluster with a Fargate service in it.
By default, your service is not deployed when running in _dev_.
The `dev.command` tells SST to instead run our Next.js app locally in dev mode.
* * *

#### [Start dev mode](https://sst.dev/docs/start/aws/nextjs#start-dev-mode-1)

Run the following to start dev mode. This’ll start SST and your Next.js app.
Terminal window```

npxsstdev

```

Once complete, click on **MyService** in the sidebar and open your Next.js app in your browser.
* * *
### [3. Add an S3 Bucket](https://sst.dev/docs/start/aws/nextjs#3-add-an-s3-bucket)
Let’s allow public `access` to our S3 Bucket for file uploads. Update your `sst.config.ts`.
sst.config.ts
```typescript


const bucket = newsst.aws.Bucket("MyBucket", {




access: "public"




});


```

Add this below the `Vpc` component.
* * *

##### [Link the bucket](https://sst.dev/docs/start/aws/nextjs#link-the-bucket-1)

Now, link the bucket to the container.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

// ...

link: [bucket],

});

```

This will allow us to reference the bucket in our Next.js app.
* * *

### [4. Create an upload form](https://sst.dev/docs/start/aws/nextjs#4-create-an-upload-form)

Add a form client component in `components/form.tsx`.
components/form.tsx```

"use client";

import styles from"./form.module.css";

exportdefaultfunctionForm({ url }: { url:string }) {

return (

<form

className={styles.form}

onSubmit={async(e)=> {

e.preventDefault();

const file = (e.target as HTMLFormElement).file.files?.[0] ?? null;

const image = await fetch(url, {

body: file,

method: "PUT",

headers: {

"Content-Type": file.type,

"Content-Disposition": `attachment; filename="${file.name}"`,

},

});

window.location.href=image.url.split["?"](0);

}}

>

<inputname="file"type="file"accept="image/png, image/jpeg" />

<buttontype="submit">Upload</button>

</form>

);

}

```

Add some styles.
components/form.module.css```

.form {

padding: 2rem;

border-radius: 0.5rem;

background-color: var(--gray-alpha-100);

}

.forminput {

margin-right: 1rem;

}

.formbutton {

appearance: none;

padding: 0.5rem0.75rem;

font-weight: 500;

font-size: 0.875rem;

border-radius: 0.375rem;

background-color: transparent;

font-family: var(--font-geist-sans);

border: 1pxsolidvar(--gray-alpha-200);

}

.formbutton:active:enabled {

background-color: var(--gray-alpha-200);

}

```

* * *

### [5. Generate a pre-signed URL](https://sst.dev/docs/start/aws/nextjs#5-generate-a-pre-signed-url)

When our app loads, we’ll generate a pre-signed URL for the file upload and render the form with it. Replace your `Home` component in `app/page.tsx`.
app/page.tsx```

export const dynamic = "force-dynamic";

exportdefaultasyncfunctionHome() {

const command = newPutObjectCommand({

Key: crypto.randomUUID(),

Resource.MyBucket.name,

});

const url = await getSignedUrl(newS3Client({}),command);

return (

<div className={styles.page}>

<main className={styles.main}>

<Form url={url} />

</main>

</div>

);

}

```

We need the `force-dynamic` because we don’t want Next.js to cache the pre-signed URL.
We are directly accessing our S3 bucket with `Resource.MyBucket.name`.
Add the relevant imports.
app/page.tsx```

import { Resource } from"sst";

import Form from"@/components/form";

import { getSignedUrl } from"@aws-sdk/s3-request-presigner";

import { S3Client, PutObjectCommand } from"@aws-sdk/client-s3";

```

And install the npm packages.
Terminal window```

npminstall@aws-sdk/client-s3@aws-sdk/s3-request-presigner

```

* * *

#### [Test your app](https://sst.dev/docs/start/aws/nextjs#test-your-app-1)

Head over to the local Next.js app in your browser, `http://localhost:3000` and try **uploading an image**. You should see it upload and then download the image.
![SST Next.js app local](https://sst.dev/_astro/start-nextjs-local.jNuBVnOP_PRG6H.webp)
* * *

### [6. Deploy your app](https://sst.dev/docs/start/aws/nextjs#6-deploy-your-app)

To build our app for production, we’ll enable Next.js’s `next.config.mjs`.
next.config.ts
```typescript

const nextConfig:NextConfig = {

/_config options here_/

"standalone"

};

```

Now to deploy our app we’ll add a `Dockerfile`.
Dockerfile```

FROM node:lts-alpine AS base

# Stage 1: Install dependencies

FROM base AS deps

WORKDIR /app

COPY package.json package-lock.json* ./

COPY sst-env.d.ts* ./

RUN npm ci

# Stage 2: Build the application

FROM base AS builder

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules

COPY . .

# If static pages do not need linked resources

RUN npm run build

# If static pages need linked resources

# RUN --mount=type=secret,id=SST_RESOURCE_MyResource,env=SST_RESOURCE_MyResource \

# npm run build

# Stage 3: Production server

FROM base AS runner

WORKDIR /app

ENV NODE_ENV=production

COPY --from=builder /app/.next/standalone ./

COPY --from=builder /app/.next/static ./.next/static

EXPOSE 3000

CMD ["node", "server.js"]

```

This builds our Next.js app in a Docker image.
You need to be running
If your Next.js app is building static pages that need linked resources, you can need to declare them in your `Dockerfile`. For example, if we need the linked `MyBucket` component from above.

```

RUN --mount=type=secret,id=SST_RESOURCE_MyBucket,env=SST_RESOURCE_MyBucket npm run build

```

You’ll need to do this for each linked resource.
Let’s also add a `.dockerignore` file in the root.
.dockerignore```

.git

.next

node_modules

```

Now to build our Docker image and deploy we run:
Terminal window```

npxsstdeploy--stageproduction

```

You can use any stage name here but it’s good to create a new stage for production.
Congrats! Your app should now be live!
* * *

## [Connect the console](https://sst.dev/docs/start/aws/nextjs#connect-the-console)

As a next step, you can setup the [SST Console](https://sst.dev/docs/console/) to _**git push to deploy**_ your app and view logs from it.
![SST Console Autodeploy](https://sst.dev/_astro/sst-console-autodeploy.DTgdy-D4_Z107cYw.webp)
You can [create a free account](https://console.sst.dev) and connect it to your AWS account.

[Skip to content](https://sst.dev/docs/workflow#_top)

# Workflow

The main difference between working on SST versus any other framework is that everything related to your app is all **defined in code**.

  1. SST **automatically manages** the resources in AWS (or any provider) defined in your app.
  2. You don’t need to **make any manual changes** to them in your cloud provider’s console.

This idea of _automating everything_ can feel unfamiliar at first. So let’s go through the workflow and look at some basic concepts.
* * *

## [Setup](https://sst.dev/docs/workflow#setup)

Before you start working on your app, there are a couple of things we recommend setting up.
Starting with your code editor.
* * *

### [Editor](https://sst.dev/docs/workflow#editor)

SST apps are configured through a file called `sst.config.ts`. It’s a TypeScript file and it can work with your editor to type check and autocomplete your code. It can also show you inline help.

* [Type check](https://sst.dev/docs/workflow#tab-panel-94)
* [Autocomplete](https://sst.dev/docs/workflow#tab-panel-95)
* [Inline help](https://sst.dev/docs/workflow#tab-panel-96)

![Editor typecheck](https://sst.dev/_astro/editor-typecheck.DFIqjKFy_ZGmPhs.webp)
![Editor autocomplete](https://sst.dev/_astro/editor-autocomplete.C_qMtcF7_1yQCxU.webp)
![Editor help](https://sst.dev/_astro/editor-help.CyNAvvXo_ZjgtIt.webp)
Most modern editors; VS Code and Neovim included, should do the above automatically. But you should start by making sure that your editor has been set up.
* * *

### [Credentials](https://sst.dev/docs/workflow#credentials)

SST apps are deployed to your infrastructure. So whether you are deploying to AWS, or Cloudflare, or any other cloud provider, make sure you have their credentials configured locally.
Learn more about how to [configure your AWS credentials](https://sst.dev/docs/iam-credentials/).
* * *

### [Console](https://sst.dev/docs/workflow#console)

SST also comes with a [Console](https://sst.dev/docs/console/). It shows you all your apps, the resources in them, lets you configure _git push to deploy_ , and also send you alerts for when there are any issues.
While it is optional, we recommend creating a free account and linking it to your AWS account. Learn more about the [SST Console](https://sst.dev/docs/console/).
* * *

## [sst.config.ts](https://sst.dev/docs/workflow#sstconfigts)

Now that you are ready to work on your app and your `sst.config.ts`, let’s take a look at what it means to _configure everything in code_.
* * *

### [IaC](https://sst.dev/docs/workflow#iac)

Infrastructure as Code or _IaC_ is a process of automating the management of infrastructure through code. Rather than doing it manually through a console or user interface.
You won’t need to use the AWS Console to configure your SST app.
Say your app has a Function and an S3 bucket, you would define that in your `sst.config.ts`.
sst.config.ts
```typescript

const bucket = newsst.aws.Bucket("MyBucket");

new sst.aws.Function("MyFunction", {

handler: "index.handler"

});

```

You won’t need to go to the Lambda and S3 parts of the AWS Console. SST will do the work for you.
In the above snippets, `sst.aws.Function` and `sst.aws.Bucket` are called Components. Learn more about [Components](https://sst.dev/docs/components/).
* * *

### [Resources](https://sst.dev/docs/workflow#resources)

The reason this works is because when SST deploys the above app, it’ll convert it into a set of commands. These then call AWS with your credentials to create the underlying resources. So the above components get transformed into a list of low level resources in AWS.
You are not directly responsible for the low level resources that SST creates.
If you log in to your AWS Console you can see what gets created internally. While these might look a little intimidating, they are all managed by SST and you are not directly responsible for them.
SST will create, track, and remove all the low level resources defined in your app.
* * *

#### [Exceptions](https://sst.dev/docs/workflow#exceptions)

There are some exceptions to this. You might have resources that are not defined in your SST config. These could include the following resources:

  1. **Previously created**
You might’ve previously created some resources by hand that you would like to use in your new SST app. You can import these resources into your app. Moving forward, SST will manage them for you. Learn more about [importing resources](https://sst.dev/docs/import-resources/).
  2. **Externally managed**
You might have resources that are managed by a different team. In this case, you don’t want SST to manage them. You simply want to reference them in your app. Learn more about [referencing resources](https://sst.dev/docs/reference-resources/).
  3. **Shared across stages**
If you are creating preview environments, you might not want to make copies of certain resources, like your database. You might want to share these across stages. Learn more about [sharing across stages](https://sst.dev/docs/share-across-stages/).

* * *

### [Linking](https://sst.dev/docs/workflow#linking)

Let’s say you wanted your function from the above example to upload a file to the S3 bucket, you’d need to hardcode the name of the bucket in your API.
SST avoids this by allowing you to **link resources** together.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




handler: "index.handler",



link: [bucket]


});

```

Now in your function you can access the bucket using SST’s [SDK](https://sst.dev/docs/reference/sdk/).
index.ts

```typescript

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

```

There’s a difference between the two snippets above. One is your **infrastructure code** and the other is your **runtime code**. One is run while creating your app, while the other runs when your users use your app.
You can access your infrastructure in your runtime using the SST SDK.
The _link_ allows you to access your **infrastructure** in your **runtime code**. Learn more about [resource linking](https://sst.dev/docs/linking/).
* * *

### [State](https://sst.dev/docs/workflow#state)

When you make a change to your `sst.config.ts`, like we did above. SST only deploys the changes.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




handler: "index.handler",



link: [bucket]


});

```

It does this by maintaining a _state_ of your app. The state is a tree of all the resources in your app and all their properties.
The state is stored in a file locally and backed up to a bucket in your AWS (or Cloudflare) account.
You can view the state of your app and its history in the SST Console.
A word of caution, if for some reason you delete your state locally and in your provider, SST won’t be able to manage the resources anymore. To SST this app won’t exist anymore.
Do not delete the bucket that stores your app’s state.
To fix this, you’ll have to manually re-import all those resources back into your app. Learn more about [how state works](https://sst.dev/docs/state/).
* * *

#### [Out of sync](https://sst.dev/docs/workflow#out-of-sync)

We mentioned above that you are not responsible for the low level resources that SST creates. But this isn’t just a point of convenience; it’s something you should not do.
Do not manually make changes to the low level resources that SST creates.
The reason for this is that, SST only applies the diffs when your `sst.config.ts` changes. So if you manually change the resources, it’ll be out of sync with your state.
You can fix some of this by running [`sst refresh`](https://sst.dev/docs/reference/cli/#refresh) but in general you should avoid doing this.
* * *

## [App](https://sst.dev/docs/workflow#app)

So now that we know how IaC works, a lot of the workflow and concepts will begin to make sense. Starting with the key parts of an app.
* * *

### [Name](https://sst.dev/docs/workflow#name)

Every app has a name. The name is used as a namespace. It allows SST to deploy multiple apps to the same cloud provider account, while isolating the resources in an app.
If you change the name of your app in your `sst.config.ts`, SST will create a completely new set of resources for it. It **does not** rename the resources.
To rename an app, you’ll need to remove the resources from the old one and deploy to the new one.
So if you:

  1. Create an app with the name `my-sst-app` in your `sst.config.ts` and deploy it.
  2. Rename the app in your `sst.config.ts` to `my-new-sst-app` and deploy again.

You will now have two apps in your AWS account called `my-sst-app` and `my-new-sst-app`.
If you want to rename your app, you’ll need to [remove](https://sst.dev/docs/workflow/#remove) the old app first and then deploy a new one with the new name.
* * *

### [Stage](https://sst.dev/docs/workflow#stage)

An app can have multiple stages. A stage is like an _environment_ , it’s a separate version of your app. For example, you might have a dev stage, a production stage, or a personal stage.
It’s useful to have multiple versions of your app because it lets you make changes and test in one version while your users continue to use the other.
You create a new stage by deploying to it with the `--stage <name>` CLI option. The stage name is used as a namespace to create a new version of your app. It’s similar to how the app name is used as a namespace.
To rename a stage, you’ll need to [remove](https://sst.dev/docs/workflow/#remove) the resources from the old one and deploy to the new one.
Similar to app names, stages cannot be renamed. So if you wanted to rename a `development` stage to `dev`; you’ll need to first remove `development` and then deploy `dev`.
* * *

#### [Personal stages](https://sst.dev/docs/workflow#personal-stages)

By default, if no stage is passed in, SST creates a stage using the username in your computer. This is called a **personal stage**. Personal stages are typically used in _dev_ mode and every developer on your team should use their own personal stage.
We’ll look at this in detail below.
* * *

### [Region](https://sst.dev/docs/workflow#region)

Most resources that are created in AWS (and many other providers) belong to a specific region. So when you deploy your app, it’s deployed to a specific region.
To switch regions, you’ll need to [remove](https://sst.dev/docs/workflow/#remove) the resources from one region and deploy to the new one.
For AWS, the region comes from your AWS credentials but it can be specified in the `sst.config.ts`.
sst.config.ts

```typescript

exportdefault$config({

app(input) {

return {

name: "my-sst-app",

providers: {

aws: { region: "us-west-2" }

}

};

}

});

```

Similar to the app and stage, if you want to switch regions; you’ll need to remove your app in the old region and deploy it to the new one.
* * *

## [Commands](https://sst.dev/docs/workflow#commands)

Now with the above background let’s look at the workflow of building an SST app.
Let’s say you’ve created an app by running.
Terminal window```

sstinit

```

* * *

### [Dev](https://sst.dev/docs/workflow#dev)

To start with, you’ll run your app in dev.
Terminal window```

sstdev

```

This deploys your app to your _personal_ stage in _dev mode_. It brings up a multiplexer that deploys your app, runs your functions, creates a tunnel, and starts your frontend and container services.
It deploys your app a little differently and is optimized for local development.

  1. It runs the functions in your app [_Live_](https://sst.dev/docs/live/) by deploying a **_stub_ version**. These proxy any requests to your local machine.
  2. It **does not deploy** your frontends or container services. Instead, it starts them locally.
  3. It also creates a [_tunnel_](https://sst.dev/docs/reference/cli#tunnel) that allows them to connect to any resources that are deployed in a VPC.

Only use `sst dev` in your personal stage.
For this reason we recommend only using your personal stage for local development. And instead deploying to a separate stage when you want to share your app with your users.
Learn more about [`sst dev`](https://sst.dev/docs/reference/cli/#dev).
* * *

### [Deploy](https://sst.dev/docs/workflow#deploy)

Once you are ready to go to production you can run.
Terminal window```

sstdeploy--stageproduction

```

You can use any stage name for production here.
* * *

### [Remove](https://sst.dev/docs/workflow#remove)

If you want to remove your app and all the resources in it, you can run.
Terminal window```

sstremove--stage<name>

```

You want to be careful while running this command because it permanently removes all the resources from your AWS (or cloud provider) account.
Be careful while running `sst remove` since it permanently removes all your resources.
To prevent accidental removal, our template `sst.config.ts` comes with the following.
sst.config.ts

```typescript


removal: input?.stage==="production"?"retain":"remove",


```

This is telling SST that if the stage is called `production` then on remove, retain critical resources like buckets and databases. This should avoid any accidental data loss.
Learn more about [removal policies](https://sst.dev/docs/reference/config/#removal).
* * *

## [With a team](https://sst.dev/docs/workflow#with-a-team)

This workflow really shines when working with a team. Let’s look at what it looks like with a basic git workflow.

  1. Every developer on the team uses `sst dev` to work in their own isolated personal stage.
  2. You commit your changes to a branch called `dev`.
  3. Any changes to the `dev` branch are auto-deployed using `sst deploy --stage dev`.
  4. Your team tests changes made to the `dev` stage of your app.
  5. If they look good, `dev` is merged into a branch called `production`.
  6. And any changes to the `production` branch are auto-deployed to the `production` stage with `sst deploy --stage production`.

In this setup, you have a separate stage per developer, a _dev_ stage for testing, and a _production_ stage.
* * *

### [Autodeploy](https://sst.dev/docs/workflow#autodeploy)

To have a branch automatically deploy to a stage when commits are pushed to it, you need to configure GitHub Actions.
![SST Console Autodeploy](https://sst.dev/_astro/sst-console-autodeploy.DTgdy-D4_Z107cYw.webp)
Or you can connect your repo to the SST Console and it’ll auto-deploy your app for you. Learn more about [Autodeploy](https://sst.dev/docs/console/#autodeploy).
* * *

### [PR environments](https://sst.dev/docs/workflow#pr-environments)

You can also set it up to create preview environments.
So when a pull request (say PR#12) is created, you auto-deploy a new stage using `sst deploy --stage pr-12`. And once the PR is merged, the preview environment or stage gets removed using `sst remove --stage pr-12`.
Just like above, you can configure this using GitHub Actions or let the SST Console do it for you.
* * *
And there you have it. You are now ready to build apps the _SST way_.

[Skip to content](https://sst.dev/docs/console#_top)

# Console

The Console is a web based dashboard to manage your SST apps — [**console.sst.dev**](https://console.sst.dev)
With it, you and your team can see all your apps, their **resources** and **updates** , **view logs** , **get alerts** on any issues, and **_git push to deploy_** them.
[![SST Console](https://sst.dev/_astro/sst-console-home-light.-MHGdy-Y_Z2fVPM.webp)](https://console.sst.dev)
The Console is completely optional and comes with a free tier.
* * *

## [Get started](https://sst.dev/docs/console#get-started)

Start by creating an account and connecting your AWS account.
Currently the Console only supports apps **deployed to AWS**.

  1. **Create an account with your email**
It’s better to use your work email so that you can invite your team to your workspace later — [**console.sst.dev**](https://console.sst.dev)
  2. **Create a workspace**
You can add your apps and invite your team to a workspace. A workspace can be for a personal project or for your team at work. You can create as many workspaces as you want.
Create a workspace for your organization. You can use it to invite your team and connect all your AWS accounts.
  3. **Connect your AWS account**
This will ask you to create a CloudFormation stack in your AWS account. Make sure that this stack is being added to **us-east-1**. Scroll down and click **Create stack**.
The CloudFormation stack needs to be created in **us-east-1**. If you create it in the wrong region by mistake, remove it and create it again.
This stack will scan all the regions in your account for SST apps and subscribe to them. Once created, you’ll see all your apps, stages, and the functions in the apps.
If you are connecting a newly created AWS account, you might run into the following error while creating the stack.

> Resource handler returned message: “Specified ReservedConcurrentExecutions for function decreases account’s UnreservedConcurrentExecution below its minimum value
This happens because AWS has been limiting the concurrency of Lambda functions for new accounts. It’s a good idea to increase this limit before you go to production anyway.
To do so, you can
Expedite the request If you want to expedite the request:
    1. Submit the request.
    2. Click the **Quota request history** link in the sidebar.
    3. Click on **AWS Support Center Case** to open your request case details.
    4. Hit the **Reply** button and select **Chat** to chat with an AWS representative to expedite it.

  4. **Invite your team**
Use the email address of your teammates to invite them. They just need to login with the email you’ve used and they’ll be able to join your workspace.

* * *

## [How it works](https://sst.dev/docs/console#how-it-works)

At a high level, here’s how the Console works.

* It’s hosted on our side
It stores some metadata about what resources you have deployed. We’ll have a version that can be self-hosted in the future.
* You can view all your apps and stages
Once you’ve connected your AWS accounts, it’ll deploy a separate CloudFormation stack and connect to any SST apps in it. And all your apps and stages will show up automatically.
* It’s open-source and built with SST
The Console is an SST app. You can view the

* * *

## [Security](https://sst.dev/docs/console#security)

The CloudFormation stack that the Console uses, creates an IAM Role in your account to manage your resources. If this is a concern for your production environments, we have a couple of options.
By default, this role is granted `AdministratorAccess`, but you can customize it to restrict access. We’ll look at this below. Additionally, if you’d like us to sign a BAA, feel free to
There maybe cases where you don’t want any data leaving your AWS account. For this, we’ll be supporting self-hosting the Console in the future.
* * *

#### [IAM permissions](https://sst.dev/docs/console#iam-permissions)

Permissions for the Console fall into two categories: read and write:

* **Read Permissions** : The Console needs specific permissions to display information about resources within your SST apps.
Purpose | AWS IAM Action  
---|---  
Fetch stack outputs | `cloudformation:DescribeStacks`  
Retrieve function runtime and size | `lambda:GetFunction`  
Access stack metadata |  `ec2:DescribeRegions`  
`s3:GetObject`  
`s3:ListBucket`  
Display function logs |  `logs:DescribeLogStreams`  
`logs:FilterLogEvents`  
`logs:GetLogEvents`  
`logs:StartQuery`  
Monitor invocation usage | `cloudwatch:GetMetricData`  
Attach the `arn:aws:iam::aws:policy/ReadOnlyAccess` AWS managed policy to the IAM Role for comprehensive read access.
* **Write Permissions** : The Console requires the following write permissions.
Purpose | AWS IAM Action  
---|---  
Forward bootstrap bucket events to event bus | `s3:PutBucketNotification`  
Send events to Console |  `events:PutRule`  
`events:PutTargets`  
Grant event bus access for Console |  `iam:CreateRole`  
`iam:DeleteRole`  
`iam:DeleteRolePolicy`  
`iam:PassRole`  
`iam:PutRolePolicy`  
Enable Issues to subscribe logs |  `logs:CreateLogGroup`  
`logs:PutSubscriptionFilter`  
Invoke Lambda functions and replay invocations | `lambda:InvokeFunction`  

It’s good practice to periodically review and update these policies.
* * *

#### [Customize policy](https://sst.dev/docs/console#customize-policy)

To customize IAM permissions for the CloudFormation stack:

  1. On the CloudFormation create stack page, download the default `template.json`.
  2. Edit the template file with necessary changes.
_View the template changes_
template.json```

"SSTRole": {

"Type": "AWS::IAM::Role",

"Properties": {

...

"ManagedPolicyArns": [

"arn:aws:iam::aws:policy/AdministratorAccess"

"arn:aws:iam::aws:policy/ReadOnlyAccess"

],

"Policies": [

{

"PolicyName": "SSTPolicy",

"PolicyDocument": {

"Version": "2012-10-17",

"Statement": [

{

"Effect": "Allow",

"Action": [

"s3:PutBucketNotification"

],

"Resource": [

"arn:aws:s3:::sstbootstrap-*"

]

},

{

"Effect": "Allow",

"Action": [

"events:PutRule",

"events:PutTargets"

],

"Resource": {

"Fn::Sub": "arn:aws:events:_:${AWS::AccountId}:rule/SSTConsole_"

}

},

{

"Effect": "Allow",

"Action": [

"iam:CreateRole",

"iam:DeleteRole",

"iam:DeleteRolePolicy",

"iam:PassRole",

"iam:PutRolePolicy"

],

"Resource": {

"Fn::Sub": "arn:aws:iam::${AWS::AccountId}:role/SSTConsolePublisher*"

}

},

{

"Effect": "Allow",

"Action": [

"logs:CreateLogGroup",

"logs:PutSubscriptionFilter"

],

"Resource": {

"Fn::Sub": "arn:aws:logs:_:${AWS::AccountId}:log-group:_"

}

},

{

"Effect": "Allow",

"Action": [

"lambda:InvokeFunction"

],

"Resource": {

"Fn::Sub": "arn:aws:lambda:_:${AWS::AccountId}:function:_"

}

}

]

}

}

]

}

}

```

  3. Upload your edited `template.json` file to an S3 bucket.
  4. Return to the CloudFormation create stack page and replace the template URL in the page URL.


* * *
## [Pricing](https://sst.dev/docs/console#pricing)
[Starting Feb 1, 2025](https://sst.dev/blog/console-pricing-update), the Console will be priced based on the number of active resources in your SST apps.
Resources | Rate per resource  
---|---  
First 2000 | $0.086  
2000+ | $0.032  
**Free Tier** : Workspaces with 350 active resources or fewer.
So for example, if you go over the free tier and have 351 active resources in a month, your bill will be 351 x $0.086 = $30.2.
A couple of things to note.
  * These are calculated for a given workspace every month.
  * A resource is what SST creates in your cloud provider. [Learn more below](https://sst.dev/docs/console#faq).
  * You can always access personal stages, even if you’re above the free tier.
  * A resource is considered active if it comes from a stage: 
    * That has been around for at least 2 weeks.
    * And, was updated during the month.
  * For volume pricing, feel free to 


[Learn more in the FAQ](https://sst.dev/docs/console#faq).
* * *
##### [Active resources](https://sst.dev/docs/console#active-resources)
A resource is considered active if it comes from a stage that has been around for at least 2 weeks. And, was updated during the month.
Let’s look at a few different scenarios to see how this works.
  * A stage that was created 5 months ago and was deployed this month, is active.
  * A stage that was created 5 months ago but was not deployed this month, is not active.
  * A stage that was created 12 days ago, is not active.
  * A stage that was created 20 days ago and was removed 10 days ago, is not active.
  * A stage that was created 5 months ago, deployed this month, then removed this month, is active.
  * A stage created 5 months ago, was not deployed this month, and removed this month, is not active.


* * *
#### [Old pricing](https://sst.dev/docs/console#old-pricing)
Previously, the Console pricing was based on the number of times the Lambda functions in your SST apps are invoked per month and it used the following tiers.
Invocations | Rate (per invocation)  
---|---  
First 1M | Free  
1M - 10M | $0.00002  
10M+ | $0.000002  
  * These are calculated for a given workspace on a monthly basis.
  * This does not apply to personal stages, they’ll be free forever.
  * There’s also a soft limit for Issues on all accounts.
  * For volume pricing, feel free to 


* * *
## [Features](https://sst.dev/docs/console#features)
Here are a few of the things the Console does for you.
  1. [**Logs**](https://sst.dev/docs/console#logs): View logs from any log group in your app
  2. [**Issues**](https://sst.dev/docs/console#issues): Get real-time alerts for any errors in your app
  3. [**Local logs**](https://sst.dev/docs/console#local-logs): View logs from your local `sst dev` session
  4. [**Updates**](https://sst.dev/docs/console#updates): View the details of every update made to your app
  5. [**Resources**](https://sst.dev/docs/console#resources): View all the resources in your app and their props
  6. [**Autodeploy**](https://sst.dev/docs/console#autodeploy): Auto-deploy your app when you _git push_ to your repo


* * *
### [Logs](https://sst.dev/docs/console#logs)
With the Console, you don’t need to go to CloudWatch to look at the logs for your functions, containers and other log groups. You can view:
  * View recent logs
  * Jump to a specific time
  * Search for logs with a given string

![SST Console Logs](https://sst.dev/_astro/sst-console-logs-light.D8Q_xhSx_JoPMA.webp)
* * *
### [Issues](https://sst.dev/docs/console#issues)
The Console will automatically show you any errors in your Node.js Lambda functions and containers in real-time. And notify you through Slack or email.
![SST Console Issues](https://sst.dev/_astro/sst-console-issues-light.jAixSwec_Z2lIrJb.webp)
With Issues, there is:
  * **Nothing to setup** , no code to instrument
  * **Source maps** are supported **automatically**
  * **No impact on performance** , since your code isn’t modified


Issues works out of the box and has no impact on performance.
Issues currently only supports Node.js functions and containers. Other languages and runtimes are on the roadmap.
* * *
#### [Error detection](https://sst.dev/docs/console#error-detection)
For the Console to automatically report your errors, you need to `console.error` an error object.
src/index.ts
```typescript


console.error(newError("my-error"));


```

This works a little differently for containers and functions.

* **Containers**
In a container applications, your code needs to also import the [SST JS SDK](https://sst.dev/docs/reference/sdk/).
src/index.ts

```typescript

import"sst";

console.error(newError("my-error"));

```

This applies a polyfill to the `console` object to prepend the log lines with a marker that allows Issues to detect errors. [More on this below](https://sst.dev/docs/console#how-it-works-1).
If you are already importing the SDK, you won’t need to add an additional import.

* **Functions**
In addition, to errors logged using `console.error(new Error("my-error"))`, Issues also reports Lambda function failures.
src/lambda.ts

```typescript


console.error(newError("my-error"));


```

In Lambda you don’t need to import the SDK to polyfill the `console` object. Since the Lambda runtime does this automatically for you.

* * *

#### [How it works](https://sst.dev/docs/console#how-it-works-1)

Here’s how Issues works behind the scenes.

  1. When an app is deployed or when an account is first synced, we add a log subscriber to the CloudWatch Log groups in your SST apps.
     * This is added to your AWS account and includes a Lambda function. More on this below.
  2. If the subscriber filter matches anything that looks like an error it invokes the Lambda function.
     * In case of errors from a Lambda function, the Lambda runtime automatically adds a marker to the logs that the filter matches for.
     * For containers, the SST SDK polyfills the `console` object to add the marker.
  3. The Lambda function tries to parse the error. If the error comes from a Lambda function, it fetches the source maps from the state bucket in your account.
  4. It then hits an endpoint in the SST Console and passes in that error.
  5. Finally, the Console groups similar looking errors together and displays them.

* * *

#### [Log subscriber](https://sst.dev/docs/console#log-subscriber)

The log subscriber also includes the following:

  1. **Lambda function** that’ll be invoked when a log with an error is matched.
     * This function has a max concurrency set to 10.
     * If it falls behind on processing by over 10 minutes, it’ll discard the logs.
     * This prevents it from scaling indefinitely when there’s a burst of errors.
     * This also means that if there are a lot of errors, the alerts might be delayed by up to 10 minutes.
  2. **IAM role** that gives it access to query the logs and the state bucket for the source maps.
  3. **Log group** with a 1 day retention.

These are added to **every region** in your AWS account that has a CloudWatch log group from your SST apps. It’s deployed using a CloudFormation stack.
This process of adding a log subscriber might fail if we:

* Don’t have enough permissions. In this case, update the permissions that you’ve granted to the Console.
* Hit the limit for the number of subscribers, there’s a maximum of 2 subscribers. To fix this, you can remove one of the existing subscribers.

You can see these errors in the Issues tab. Once you’ve fixed these issues, you can hit **Retry** and it’ll try attaching the subscriber again.
* * *

#### [Costs](https://sst.dev/docs/console#costs)

AWS will bill you for the Lambda function log subscriber that’s in your account. This is usually fairly minimal.
Even if your apps are generating an infinite number of errors, the Lambda function is limited to a concurrency of 10. So the **maximum** you’ll be charged $43 x 10 = **$430 per month x # of regions** that are being monitored.
You can also disable Issues from your workspace settings, if you are using a separate service for monitoring.
* * *

### [Updates](https://sst.dev/docs/console#updates)

Each update in your app also gets a unique URL, a **_permalink_**. This is printed out by the SST CLI.
sst deploy```

↗Permalinkhttps://sst.dev/u/318d3879

```

You can view these updates in the Console. Each update shows:
  1. Full list of **all the resources** that were modified
  2. Changes in their **inputs and outputs**
  3. Any Docker or site **builds logs**
  4. **CLI command** that triggered the update
  5. **Git commit** , if it was an auto-deploy


The permalink is useful for sharing with your team and debugging any issues with your deploys.
![SST Console Updates](https://sst.dev/_astro/sst-console-updates-light.CKwwk6K8_rSgyL.webp)
The CLI updates your [state](https://sst.dev/docs/state/) with the event log from each update and generated a globally unique id. If your AWS account is connected to the Console, it’ll pull the state and event log to generate the details for the update permalink.
When you visit the permalink, the Console looks up the id of the update and redirects you to the right app in your workspace.
* * *
### [Resources](https://sst.dev/docs/console#resources)
The Console shows you the complete [state of the resources](https://sst.dev/docs/state/) in your app. You can view:
  1. Each resource in your app
  2. The relation between resources
  3. The outputs of a given resource

![SST Console Resources](https://sst.dev/_astro/sst-console-resources-light.Cbhg_SwD_TOiix.webp)
* * *
### [Autodeploy](https://sst.dev/docs/console#autodeploy)
The Console can auto-deploy your apps when you _git push_ to your GitHub repo. Autodeploy uses 
![SST Console Autodeploy](https://sst.dev/_astro/sst-console-autodeploy-light.DsTLW4CE_Z2fRvcv.webp)
We designed Autodeploy to be a better fit for SST apps when compared to alternatives like GitHub Actions or CircleCI.
  1. **Easy to get started**
     * Autodeploy supports the standard branch and PR workflow out of the box. You don’t need a config file to get started.
     * There are no complicated steps in configuring your AWS credentials; since your AWS account is already connected to the Console.
  2. **Configurable**
     * You can configure how Autodeploy works directly through your `sst.config.ts`.
     * It’s typesafe and the callbacks let you customize how to respond to incoming git events.
  3. **Runs in your AWS account**
     * The builds are run in your AWS account.
     * It can also be configured to run in your VPC. This is useful if your builds need to access private resources.
  4. **Integrates with the Console**
     * You can see which resources were updated in a deploy.
     * Your resource updates will also show you the related git commit.


* * *
#### [Setup](https://sst.dev/docs/console#setup)
To get started with Autodeploy:
  1. **Enable the GitHub integration**
Head over to your **Workspace settings** > **Integrations** and enable GitHub. This will ask you to login to GitHub and you’ll be asked to pick the GitHub organization or user you want to link to.
You can only associate your workspace with a single GitHub org.
If you have multiple GitHub orgs, you can create multiple workspaces in the Console.
  2. **Connect a repo**
To auto-deploy an app, head over to the **App’s Settings** > **Autodeploy** and select the repo for the app.
  3. **Configure an environment**
Next you can configure a branch or PR environment by selecting the **stage** you want deployed to an **AWS account**. You can optionally configure **environment variables** as well.
Stage names by default are generated based on the branch or PR.
By default, stages are based on the branch name or PR. We’ll look at this in detail below.
  4. **Git push**
Finally, _git push_ to the environment you configured and head over to your app’s **Autodeploy** tab to see it in action.
PR stages are removed when the PR is closed while branch stages are not.
For example, if you configure a branch environment for the stage `production`, any git pushes to the `production` branch will be auto-deployed. Similarly, if you create a new PR, say PR#12, the Console will auto-deploy a stage called `pr-12`.
You can also manually trigger a deployment through the Console by passing in a Git ref and the stage you want to deploy to.
  5. **Setup alerts**
Once your deploys are working, you can set the Console to send alerts for your deploys. Head over to your **Workspace Settings** > **Alerts** and add a new alert to be notified on any Autodeploys, or only on Autodeploy errors.


You can configure how Autodeploy works through your `sst.config.ts`.
While Autodeploy supports the standard branch and PR workflow out of the box, it can be configured in depth through your `sst.config.ts`.
* * *
#### [Configure](https://sst.dev/docs/console#configure)
The above can be configured through the [`console.autodeploy`](https://sst.dev/docs/reference/config/#console-autodeploy) option in the `sst.config.ts`.
sst.config.ts
```typescript


exportdefault$config({



// Your app's config



app(input) { },



// Your app's resources



asyncrun() { },



// Your app's Console config


console: {


autodeploy: {



target(event) {




if (event.type==="branch"&& event.branch==="main"&& event.action==="pushed") {




return { stage: "production" };



}


}


}


}


});

```

In the above example we are using the `console.autodeploy.target` option to change the stage that’s tied to a git event. Only git pushes to the `main` branch to auto-deploy to the `production` stage.
This works because if `target` returns `undefined`, the deploy is skipped. And if you provide your own `target` callback, it overrides the default behavior.
You can use the git events to configure how your app is auto-deployed.
Through the `console.autodeploy.runner` option, you can configure the runner that’s used. For example, if you wanted to increase the timeouts to 2 hours, you can.
sst.config.ts

```typescript

console: {

autodeploy: {

runner: { timeout: "2 hours" }

}

}

```

This also takes the stage name, so you can set the runner config for a specific stage.
sst.config.ts

```typescript

console: {


autodeploy: {



runner(stage) {




if (stage ==="production") return { timeout: "3 hours" };



}


}


}

```

You can also have your builds run inside your VPC.
sst.config.ts

```typescript

console: {

autodeploy: {

runner: {

vpc: {

id: "vpc-0be8fa4de860618bb",

securityGroups: ["sg-0399348378a4c256c"],

subnets: ["subnet-0b6a2b73896dc8c4c", "subnet-021389ebee680c2f0"]

}

}

}

}

```

Or specify files and directories to be cached.
sst.config.ts

```typescript

console: {


autodeploy: {


runner: {


cache: {



paths: ["node_modules", "/path/to/cache"]



}


}


}


}

```

Read more about the [`console.autodeploy`](https://sst.dev/docs/reference/config/#console-autodeploy) config.
* * *

#### [Environments](https://sst.dev/docs/console#environments)

The Console needs to know which account it needs to autodeploy into. You configure this under the **App’s Settings** > **Autodeploy**. Each environment takes:

  1. **Stage**
The stage that is being deployed. By default, the stage name comes from the name of the branch. Branch names are sanitized to only letters/numbers and hyphens. So for example:
     * A push to a branch called `production` will deploy a stage called `production`.
     * A push to PR#12 will deploy to a stage called `pr-12`.
As mentioned, above you can customize this through your `sst.config.ts`.
You can specify a pattern to match the stage name in your environments.
If multiple stages share the same environment, you can use a glob pattern. For example, `pr-*` matches all stages that start with `pr-`.
  2. **AWS Account**
The AWS account that you are deploying to.
  3. **Environment Variables**
Any environment variables you need for the build process. These are made available under `process.env.*` in your `sst.config.ts`.

* * *

#### [How it works](https://sst.dev/docs/console#how-it-works-2)

When you _git push_ to a branch, pull request, or tag, the following happens:

  1. The stage name is generated based on the `console.autodeploy.target` callback.
    1. If there is no callback, the stage name is a sanitized version of the branch or tag.
    2. If there is a callback but no stage is returned, the deploy is skipped.
  2. The stage is matched against the environments in the Console to get the AWS account and any environment variables for the deploy.
  3. The runner config is generated based on the `console.autodeploy.runner`. Or the defaults are used.
  4. The deploy is run based on the above config.

This only applies only to git events. If you trigger a deploy through the Console, you are asked to specify the stage you want to deploy to. So in this case, it skips step 1 from above and does not call `console.autodeploy.target`.
Both `target` and `runner` are optional and come with defaults, but they can be customized.
* * *

#### [Costs](https://sst.dev/docs/console#costs-1)

AWS will bill you for the **CodeBuild build minutes** that are used to run your builds.
* * *

### [Local logs](https://sst.dev/docs/console#local-logs)

When the Console starts up, it checks if you are running `sst dev` locally. If so, then it’ll show you real-time logs from your local terminal. This works by connecting to a local server that’s run as a part of the SST CLI.
![SST Console Local logs](https://sst.dev/_astro/sst-console-local-light.DvQ6HXHr_HAe0R.webp)
The local server only allows access from `localhost` and `console.sst.dev`.
The local logs works in all browsers and environments. But for certain browsers like Safari or Brave, and Gitpod, it needs some additional configuration.
* * *

#### [Safari & Brave](https://sst.dev/docs/console#safari--brave)

Certain browsers like Safari and Brave require the local connection between the browser and the `sst dev` CLI to be running on HTTPS.
SST can automatically generate a locally-trusted certificate using the [`sst cert`](https://sst.dev/docs/reference/cli#cert) command.
Terminal window```

sstcert

```

You’ll only need to **run this once** on your machine.
* * *
#### [Gitpod](https://sst.dev/docs/console#gitpod)
If you are using `sst dev` process running inside your Gitpod workspace.
To get started:
  1. Navigate to Console in the browser


The companion app runs locally and creates a tunnelled connection to your Gitpod workspace.
* * *
## [FAQ](https://sst.dev/docs/console#faq)
Here are some frequently asked questions about the Console.
  * Do I need to use the Console to use SST?
You **don’t need the Console** to use SST. It compliments the CLI and has some features that help with managing your apps in production.
That said, it is completely free to get started. You can create an account and invite your team, **without** having to add a **credit card**.
  * Is there a free tier?
If your workspace has 350 active resources or fewer for the month, it’s considered to be in the free tier. This count also resets every month.
  * What happens if I go over the free tier?
You won’t be able to access the _production_ or deployed stages till you add your billing details in the workspace settings.
Note that, you can continue to **access your personal stages**. Just make sure you have `sst dev` running locally. Otherwise the Console won’t be able to detect that it’s a personal stage.
  * What counts as a resource?
Resources are what SST creates in your cloud provider. This includes the resources created by both SST’s built-in components, like `Function`, `Nextjs`, `Bucket`, and the ones created by any other Terraform/Pulumi provider.
Some components, like `Nextjs` and `StaticSite`, create multiple resources. In general, the more complex the component, the more resources it’ll create.
You can see a [full list of resources](https://sst.dev/docs/console#resources) if you go to an app in your Console and navigate to a stage in it.
For some context, the Console is itself a pretty large 
  * Do PR stages also count?
A stage has to be around for at least 2 weeks before the resources in it are counted as active. So if a PR stage is created and removed within 2 weeks, they don’t count.
However, if you remove a stage and create a new one with the same name, it does not reset the 2 week initial period.


* * *
#### [Old pricing FAQ](https://sst.dev/docs/console#old-pricing-faq)
Here were some frequently asked questions about the old pricing plan for the Console.
  * Do I need to switch to the new pricing?
If you are currently on the old plan, you don’t have to switch and you won’t be automatically switched over either.
You can go to the workspace settings and check out how much you’ll be billed based on both the plans. To switch over, you can cancel your current plan and then subscribe to the new plan.
At some point in the future, we’ll remove the old plan. But there’s no specific timeline for it yet.
  * Which Lambda functions are included in the number of invocations?
The number of invocations are only counted for the **Lambda functions in your SST apps**. Other Lambda functions in your AWS accounts are not included.
  * Do the functions in my personal stages count as a part of the invocations?
Lambda functions that are invoked **locally are not included**.
  * My invocation volume is far higher than the listed tiers. Are there any other options?
Feel free to 


If you have any further questions, feel free to 


[Skip to content](https://sst.dev/docs/set-up-a-monorepo#_top)
# Set up a Monorepo
While, [drop-in mode](https://sst.dev/docs/#drop-in-mode) is great for simple projects, we recommend using a monorepo for projects that are going to have multiple packages.
We created a 
However, setting up a monorepo with everything you need can be surprisingly tricky. To fix this we created a template for a TypeScript monorepo that uses npm workspaces.
* * *
## [How to use](https://sst.dev/docs/set-up-a-monorepo#how-to-use)
To use this template.
  1. Head over to 
  2. Click on **Use this template** and create a new repo.
  3. Clone the repo.
  4. From the project root, run the following to rename it to your app.
Terminal window```


npxreplace-in-file/monorepo-template/gMY_APP**/*.*--verbose


```

  5. Install the dependencies.
Terminal window```

npminstall

```



Now just run `npx sst dev` from the project root.
* * *
## [Project structure](https://sst.dev/docs/set-up-a-monorepo#project-structure)
The app is split into the separate `packages/` and an `infra/` directory.
```

my-sst-app

├─ sst.config.ts

├─ package.json

├─ packages

│  ├─ functions

│  ├─ scripts

│  └─ core

└─ infra

```

The `packages/` directory has your workspaces and this is in the root `package.json`.
"package.json```


"workspaces": [




"packages/*"



]

```

Let’s look at it in detail.
* * *

### [Packages](https://sst.dev/docs/set-up-a-monorepo#packages)

The `packages/` directory includes the following:

* `core/`
This directory includes shared code that can be used by other packages. These are defined as modules. For example, we have an `Example` module.
packages/core/src/example/index.ts

```typescript

exportmodule Example {

exportfunctionhello() {

return"Hello, world!";

}

}

```

We export this using the following in the `package.json`:
packages/core/package.json```

"exports": {

"./*": [

"./src/*\/index.ts",

"./src/*.ts"

]

}

```

This will allow us to import the `Example` module by doing:

```

import { Example } from"@monorepo-template/core/example";

Example.hello();

```

We recommend creating new modules for the various _domains_ in your project. This roughly follows Domain Driven Design.
We also have `sst shell` CLI.
Terminal window```

npmtest

```

* `functions/`
This directory includes our Lambda functions. It imports from the `core/` package by using it as a local dependency.
* `scripts/`
This directory includes scripts that you can run on your SST app using the `sst shell` CLI and `scripts/src/example.ts`, run the following from `packages/scripts/`.
Terminal window```

npmrunshellsrc/example.ts

```

You can add additional packages to the `packages/` directory. For example, you might add a `frontend/` and a `backend/` package.
* * *

### [Infrastructure](https://sst.dev/docs/set-up-a-monorepo#infrastructure)

The `infra/` directory allows you to logically split the infrastructure of your app into separate files. This can be helpful as your app grows.
In the template, we have an `api.ts`, and `storage.ts`. These export resources that can be used in the other infrastructure files.
infra/storage.ts
```typescript

export const bucket = newsst.aws.Bucket("MyBucket");

```

We then dynamically import them in the `sst.config.ts`.
sst.config.ts

```typescript


async run() {




const storage = await import("./infra/storage");




awaitimport("./infra/api");




return {




MyBucket: storage.bucket.name



};


}

```

Finally, some of the outputs of our components are set as outputs for our app.

[Skip to content](https://sst.dev/docs/start/cloudflare/hono#_top)

# Hono on Cloudflare with SST

We are going to build an API with Hono, add an R2 bucket for file uploads, and deploy it using Cloudflare with SST.
You can
Before you get started, make sure to
* * *

## [1. Create a project](https://sst.dev/docs/start/cloudflare/hono#1-create-a-project)

Let’s start by creating our app.
Terminal window```

mkdirmy-hono-api && cdmy-hono-api

npminit-y

```

* * *
#### [Init SST](https://sst.dev/docs/start/cloudflare/hono#init-sst)
Now let’s initialize SST in our app.
Terminal window```


npxsst@latestinit




npminstall


```

Select the defaults and pick **Cloudflare**. This’ll create a `sst.config.ts` file in your project root.
* * *

#### [Set the Cloudflare API token](https://sst.dev/docs/start/cloudflare/hono#set-the-cloudflare-api-token)

You can save your Cloudflare API token in a `.env` file or just set it directly.
Terminal window```

exportCLOUDFLARE_API_TOKEN=aaaaaaaa_aaaaaaaaaaaa_aaaaaaaa

exportCLOUDFLARE_DEFAULT_ACCOUNT_ID=aaaaaaaa_aaaaaaaaaaaa_aaaaaaaa

```

* * *
## [2. Add a Worker](https://sst.dev/docs/start/cloudflare/hono#2-add-a-worker)
Let’s add a Worker. Update your `sst.config.ts`.
sst.config.ts
```typescript


asyncrun() {




const hono = newsst.cloudflare.Worker("Hono", {




url: true,




handler: "index.ts",




});




return {




api: hono.url,



};


}

```

We are enabling the Worker URL, so we can use it as our API.
* * *

## [3. Add an R2 Bucket](https://sst.dev/docs/start/cloudflare/hono#3-add-an-r2-bucket)

Let’s add an R2 bucket for file uploads. Update your `sst.config.ts`.
sst.config.ts

```typescript

const bucket = newsst.cloudflare.Bucket("MyBucket");

```

Add this above the `Worker` component.

#### [Link the bucket](https://sst.dev/docs/start/cloudflare/hono#link-the-bucket)

Now, link the bucket to our Worker.
sst.config.ts

```typescript


const hono = newsst.cloudflare.Worker("Hono", {




url: true,




 [bucket],




handler: "index.ts",




});


```

* * *

## [4. Upload a file](https://sst.dev/docs/start/cloudflare/hono#4-upload-a-file)

We want the `/` route of our API to upload a file to the R2 bucket. Create an `index.ts` file and add the following.
index.ts

```typescript

const app = newHono()

.put("/*", async(c)=> {

const key = crypto.randomUUID();

await Resource.MyBucket.put(key, c.req.raw.body, {

httpMetadata: {

contentType: c.req.header("content-type"),

},

});

return c.text(`Object created with key: ${key}`);

});

exportdefault app;

```

We are uploading to our R2 bucket with the SDK — `Resource.MyBucket.put()`
Add the imports.
index.ts

```typescript


import { Hono } from"hono";




import { Resource } from"sst";


```

And install the npm packages.
Terminal window```

npminstallhono

```

* * *
## [5. Download a file](https://sst.dev/docs/start/cloudflare/hono#5-download-a-file)
We want to download the last uploaded file if you make a `GET` request to the API. Add this to your routes in `index.ts`.
index.ts
```typescript


const app = newHono()



// ...



.get("/", async(c)=> {




const first = await Resource.MyBucket.list().then(




(res) =>




res.objects.sort(




(a, b) => a.uploaded.getTime() - b.uploaded.getTime(),




)[0],



);



const result = await Resource.MyBucket.get(first.key);




c.header("content-type", result.httpMetadata.contentType);




return c.body(result.body);



});

```

We are getting a list of the files in the files in the bucket with `Resource.MyBucket.list()` and we are getting a file for the given key with `Resource.MyBucket.get()`.
* * *

#### [Start dev mode](https://sst.dev/docs/start/cloudflare/hono#start-dev-mode)

Start your app in dev mode.
Terminal window```

npxsstdev

```

This will give you the URL of your API.
```

✓Complete

Hono:<https://my-hono-api-jayair-honoscript.sst-15d.workers.dev>

```

* * *
#### [Test your app](https://sst.dev/docs/start/cloudflare/hono#test-your-app)
Let’s try uploading a file from your project root. Make sure to use your API URL.
Terminal window```


curl-XPUT--upload-filepackage.jsonhttps://my-hono-api-jayair-honoscript.sst-15d.workers.dev


```

Now head over to `https://my-hono-api-jayair-honoscript.sst-15d.workers.dev` in your browser and it’ll load the file you just uploaded.
* * *

## [6. Deploy your app](https://sst.dev/docs/start/cloudflare/hono#6-deploy-your-app)

Finally, let’s deploy your app!
Terminal window```

npxsstdeploy--stageproduction

```

You can use any stage name here but it’s good to create a new stage for production.


[Skip to content](https://sst.dev/docs/reference/sdk#_top)
# SDK
The SST SDK allows your runtime code to interact with your infrastructure in a typesafe way.
You can use the SDK in your **functions** , **frontends** , and **container applications**. You can access links from components. And some components come with SDK clients that you can use.
Check out the _SDK_ section in a component’s API reference doc.
Currently, the SDK is only available for JS/TS, Python, Golang, and Rust. Support for other languages is on the roadmap.
* * *
## [Node.js](https://sst.dev/docs/reference/sdk#nodejs)
The JS SDK is an 
Terminal window```


npminstallsst


```

* * *

### [Links](https://sst.dev/docs/reference/sdk#links)

Import `Resource` to access the linked resources.
src/lambda.ts

```typescript

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

```

The `Resource` object is typesafe and will autocomplete the available resources in your editor.
Here we are assuming that a bucket has been linked to the function. Here’s what that could look like.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket");




newsst.aws.Function("MyFunction", {




handler: "src/lambda.handler",




link: [bucket]



});

```

* * *

#### [Defaults](https://sst.dev/docs/reference/sdk#defaults)

By default, the `Resource` object contains `Resource.App`. This gives you some info about the current app including:

* `App.name`: The name of your SST app.
* `App.stage`: The current stage of your SST app.

src/lambda.ts

```typescript

import { Resource } from"sst";

console.log(Resource.App.name, Resource.App.stage);

```

* * *

### [Clients](https://sst.dev/docs/reference/sdk#clients)

Components like the [`Realtime`](https://sst.dev/docs/component/aws/realtime/) component come with a client that you can use.
src/lambda.ts

```typescript


import { realtime } from"sst/aws/realtime";




export const handler = realtime.authorizer(async (token) => {



// Validate the token



});


```

For example, `realtime.authorizer` lets you create the handler for the authorizer function that `Realtime` needs.
* * *

### [How it works](https://sst.dev/docs/reference/sdk#how-it-works)

In the above example, `Resource.MyBucket.name` works because it’s been injected into the function package on `sst dev` and `sst deploy`.
For functions, this is injected into the `process.env` object.
The JS SDK first checks the `process.env` and then the `globalThis` for the linked resources. You can [read more about how the links are injected](https://sst.dev/docs/linking/#injecting-links).
* * *

## [Python](https://sst.dev/docs/reference/sdk#python)

SST uses
To use the SDK, add it to your `pyproject.toml`.
functions/pyproject.toml```

[tool.uv.sources]

sst = { git = "<https://github.com/sst/sst.git>", subdirectory = "sdk/python", branch = "dev" }

```

And in your function, import the `resource` module and access the linked resource.
functions/src/functions/api.py```


from sst import Resource




defhandler(event, context):




print(Resource.MyBucket.name)


```

Here `MyBucket` is the name of a bucket that’s linked to the function.
sst.config.ts

```typescript

const bucket = newsst.aws.Bucket("MyBucket");

new sst.aws.Function("MyFunction", {

handler: "functions/src/functions/api.handler",

runtime: "python3.11",

link: [bucket]

});

```

Client functions are currently **not supported** in the Python SDK.
* * *

## [Golang](https://sst.dev/docs/reference/sdk#golang)

Use the SST Go SDK package in your Golang functions or container applications.
src/main.go```

import (

"github.com/sst/sst/v3/sdk/golang/resource"

)

```

In your runtime code, use the `resource.Get` function to access the linked resources.
src/main.go```

resource.Get("MyBucket", "name")

```

Where `MyBucket` is the name of a bucket that’s linked to the function.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket");




newsst.aws.Function("MyFunction", {




handler: "./src",




link: [bucket]



});

```

You can also access the current app’s info with.
src/main.go```

resource.Get("App", "name")

resource.Get("App", "stage")

```

Client functions are currently **not supported** in the Go SDK.
* * *
## [Rust](https://sst.dev/docs/reference/sdk#rust)
Use the SST Rust SDK package in your Rust functions or container applications.
Cargo.toml```


sst_sdk = "0.1.0"


```

In your runtime, use the `Resource::get()` function to access linked resources as a typesafe struct, or a `serde_json::Value`.
main.rs```

use sst_sdk::Resource;

# [derive(serde::Deserialize, Debug)]

struct Bucket {

name: String,

}

fnmain() {

letresource= Resource::init().unwrap();

// access your linked resources as a typesafe struct that implements Deserialize

let Bucket { name } =resource.get("MyBucket").unwrap();

// or as a weakly typed json value (that also implements Deserialize)

letopenai_key: serde_json::Value =resource.get("OpenaiSecret").unwrap();

}

```

where `MyBucket` and `OpenaiSecret` are linked to the function.
sst.config.ts
```typescript


const bucket = newsst.aws.Bucket("MyBucket");




const openai = newsst.Secret("OpenaiSecret");




new sst.aws.Function("MyFunction", {




handler: "./",



link: [bucket, openai],



runtime: "rust"



});

```

Client functions are currently **not supported** in the Rust SDK.

`AccessDenied`Access Denied
This XML file does not appear to have any style information associated with it. The document tree is shown below.  

<Error>
<Code>AccessDenied</Code>
<Message>Access Denied</Message>
...
</Error>

[Skip to content](https://sst.dev/docs/state#_top)

# State

When you deploy your app, SST creates a state file locally to keep track of the state of the infrastructure in your app.
So when you make a change, it’ll allow SST to do a diff with the state and only deploy what’s changed.
* * *
The state of your app includes:

  1. A state file for your resources. This is a JSON file.
  2. A passphrase that is used to encrypt the secrets in your state.

Aside from these, SST also creates some other resources when your app is first deployed. We’ll look at this below.
* * *
The state is generated locally but is backed up to your provider using:

  1. A **bucket** to store the state, typically named `sst-state-<hash>`. This is created in the region of your `home`. More on this below.
  2. An **SSM parameter** to store the passphrase used to encrypt your secrets, under `/sst/passphrase/<app>/<stage>`. Also created in the region of your `home`.

Do not delete the SSM parameter that stores the passphrase for your app.
The passphrase is used to encrypt any secrets and sensitive information. Without it SST won’t be able to read the state file and deploy your app.
* * *

## [Home](https://sst.dev/docs/state#home)

Your `sst.config.ts` specifies which provider to use for storing your state. We call this the `home` of your app.
sst.config.ts

```typescript

{

home: "aws"

}

```

You can specify which provider you’d like to use for this. Currently `aws` and `cloudflare` are supported.
Your state file is uploaded to your `home`.
When you specify your home provider, SST assumes you’d like to use that provider in your app as well and adds it to your providers internally. So the above is equivalent to doing this.
sst.config.ts

```typescript

{



home: "aws",



providers: {



aws: true



}


}

```

This also means that if you change the region of the `aws` provider above, you are changing the region for your `home` as well.
You can read more about the `home` provider in [Config](https://sst.dev/docs/reference/config/).
* * *

## [Bootstrap](https://sst.dev/docs/state#bootstrap)

As SST starts deploying the resources in your app, it creates some additional _bootstrap_ resources. If your app has a Lambda function or a Docker container, then SST will create the following in the same region as the given resource:

  1. An assets bucket to store the function packages, typically named `sst-asset-<hash>`.
  2. An ECR repository to store container images, called `sst-asset`.
  3. An SSM parameter to store the assets bucket name and the ECR repository, stored under `/sst/bootstrap`.
  4. An AppSync Events API endpoint to power [Live](https://sst.dev/docs/live).

The SSM parameter is used to look up the location of these resources.
Some additional bootstrap resources are created based on what your app is creating.
When you remove an SST app, it does not remove the _state_ or _bootstrap_ resources. This is because it does not know if there are other apps that might be using this. So if you want to completely remove any SST created resources, you’ll need to manually remove these in the regions you’ve deployed to.
* * *

### [Reset](https://sst.dev/docs/state#reset)

If you accidentally remove the bootstrap resources the SST CLI will not be able to start up.
To fix this you’ll need to reset your bootstrap resources.

  1. Remove the resources that are listed in the parameter. For example, the `asset` or `state` bucket. Or the ECR repository.
  2. Remove the SSM parameter.

Now when you run the SST CLI, it’ll bootstrap your account again.
* * *

## [How it works](https://sst.dev/docs/state#how-it-works)

The state file is a JSON representation of all the low level resources created by your app. It is a cached version of the state of resources in the cloud provider.
So when you do a deploy the following happens.

  1. The components in the `sst.config.ts` get converted into low level resource definitions. These get compared to the the state file.
  2. The differences between the two are turned into API calls that are made to your cloud provider.
     * If there’s a new resource, it gets created.
     * If a resource has been removed, it gets removed.
     * If there’s a change in config of the resource, it gets applied.
  3. The state file is updated to reflect the new state of these resources. Now the `sst.config.ts`, the state file, and the resources in the cloud provider are all in sync.

* * *

### [Out of sync](https://sst.dev/docs/state#out-of-sync)

This process works fine until you manually go change these resources through the cloud provider’s console. This will cause the **state and the resources to not be in sync** anymore. This can cause an issue in some cases.
If you manually change the resources in your cloud provider, they will go out of sync with your app’s state.
Let’s look at a couple of scenarios.
Say we’ve deployed a `Function` with it set to `{ timeout: 10 seconds" }`. At this point, the config, state, and resource are in sync.
* * *

#### [Change the resource](https://sst.dev/docs/state#change-the-resource)

* We now go change the timeout to 20 seconds in the AWS Console.
  * The config and state are out of sync with the resource since they are still set to 10 seconds.
* Now if we deploy our app, the config will be compared to the state.
  * It’ll find no differences and so it won’t update the resource.

The config and state will stay out of sync with the resource.
* * *

#### [Change the config](https://sst.dev/docs/state#change-the-config)

* If we change our config to `{ timeout: 30 seconds" }` and do a deploy.
* The config and state will have some differences.
* SST will make a call to AWS to set the timeout of the resource to 30 seconds.
  * Once updated, it’ll update the state file to match the current state of the resource.

The config, state, and resource are back being in sync.
* * *

#### [Remove the resource](https://sst.dev/docs/state#remove-the-resource)

* Next we go to the AWS Console and remove the function.
  * The config and state still have the function with the timeout set to 30 seconds.
* If we change our config to `{ timeout: 60 seconds }` and do a deploy.
* The config and state will be different.
* SST will make a call to update the timeout of the resource to 60 seconds.
  * But this call to AWS will fail because the function doesn’t exist.

Your deploys will fail moving forward because your state shows that a resource exists but it doesn’t anymore. To fix this, you’ll need to _refresh_ your state file.
* * *

### [Refresh](https://sst.dev/docs/state#refresh)

To fix scenarios where the resources in the cloud are out of sync with the state of your app, you’ll need to run.
Terminal window```

sstrefresh

```

This command does a couple of simple things:
  1. It goes through every single resource in your state.
  2. Makes a call to the cloud provider to check the resource. 
     * If the configs are different, it’ll **update the state** to reflect the change.
     * If the resource doesn’t exist anymore, it’ll **remove it from the state**.


The `sst refresh` does not make changes to the resources in the cloud provider.
Now the state and the resources are in sync. So if we take the scenario from above where we removed the function from the AWS Console but not from our config or state. To fix it, we’ll need to:
  * Run `sst refresh`
    * This will remove the function from the state as well.
  * Now if we change our config to `{ timeout: 60 seconds }` and do a deploy.
  * The config and state will be compared and it’ll find that a function with that config doesn’t exist.
  * So SST will make a call to AWS to create a new function with the given config.


In general we do not recommend manually changing resources in a cloud provider since it puts your state out of sync. But if you find yourself in a situation where this happens, you can use the `sst refresh` command to put them back in sync.


[Skip to content](https://sst.dev/docs/reference-resources#_top)
# Reference Resources
Referencing is the process of _using_ some externally created resources in your SST app; without having SST manage them.
This is for when you have some resources that are either managed by a different team or a different IaC tool. Typically these are low-level resources and not SST’s built-in components.
There are a few different ways this shows up in SST.
* * *
## [Lookup a resource](https://sst.dev/docs/reference-resources#lookup-a-resource)
Let’s say you have an existing resource that you want to use in your SST app.
You can look it up by passing in a property of the resource. For example, to look up a previously created S3 Bucket with the following name.
```

mybucket-xnbmhcvd

```

We can use the 
sst.config.ts
```typescript


const bucket = aws.s3.BucketV2.get("MyBucket", "mybucket-xnbmhcvd");


```

This gives you the same bucket object that you’d get if you had created this resource in your app.
Here we are assuming the bucket wasn’t created through an SST app. This is why we are using the low-level `aws.s3.BucketV2`. If this was created in an SST app or in another stage in the same app, there’s a similar `static sst.aws.Bucket.get` method. Learn more about [sharing across stages](https://sst.dev/docs/share-across-stages).
* * *

#### [How it works](https://sst.dev/docs/reference-resources#how-it-works)

When you create a resource in your SST app, two things happen. First, the resource is created by making a bunch of calls to your cloud provider. Second, SST makes a call to _get_ the resource from the cloud provider. The data that it gets back is stored in your [state](https://sst.dev/docs/state/).
When you lookup a resource or create it, you get the same type of object.
When you lookup a resource, it skips the creation step and just gets the resource. It does this every time you deploy. But the object you get in both cases is the same.
* * *

#### [Lookup properties](https://sst.dev/docs/reference-resources#lookup-properties)

The properties used to do a lookup are the same ones that you’d use if you were trying to import them.
You can look up a resource with its [Import Property](https://sst.dev/docs/import-resources/#import-properties).
We’ve compiled a list of the most commonly lookedup low-level resources and their [Import Properties](https://sst.dev/docs/import-resources/#import-properties).
Most low-level resources come with a `static get` method that use this property to look up the resource.
* * *

#### [Make it linkable](https://sst.dev/docs/reference-resources#make-it-linkable)

Let’s take it a step further.
You can use the [`sst.Linkable`](https://sst.dev/docs/component/linkable/) component, to be able to link any property of this resource.
sst.config.ts

```typescript

const storage = newsst.Linkable("MyStorage", {

properties: {

bucket.bucketDomainName

}

});

```

Here we are using the domain name of the bucket as an example.
* * *

#### [Link to it](https://sst.dev/docs/reference-resources#link-to-it)

And link it to a function.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




handler: "src/lambda.handler",



link: [storage]


});

```

Now you can use the [SDK](https://sst.dev/docs/reference/sdk/) to access them at runtime.
src/lambda.ts

```typescript

import { Resource } from"sst";

console.log(Resource.MyStorage.domain);

```

* * *

## [Pass in a resource](https://sst.dev/docs/reference-resources#pass-in-a-resource)

Aside from looking up resources, you can also pass existing resources in to the built-in SST components. This is typically when you are trying to create a new resource and it takes another resource as a part of it.
For example, let’s say you want to add a previously created function as a subscriber to a queue. You can do so by passing its ARN.
sst.config.ts

```typescript


const queue = newsst.aws.Queue("MyQueue");




queue.subscribe("arn:aws:lambda:us-east-1:123456789012:function:my-function");


```

* * *

#### [How it works](https://sst.dev/docs/reference-resources#how-it-works-1)

SST is simply asking for the props the underlying resource needs. In this case, it only needs the function ARN.
However, for more complicated resources like VPCs, you might have to pass in a lot more. Here we are creating a new function in an existing VPC.
sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

handler: "src/lambda.handler",

vpc: {

subnets: ["subnet-0be8fa4de860618bb"],

securityGroups: ["sg-0be8fa4de860618bb"]

}

});

```

Whereas, for the `Cluster` component, you might need to pass in a lot more.
sst.config.ts

```typescript


new sst.aws.Cluster("MyCluster", {



vpc: {



id: "vpc-0be8fa4de860618bb",




securityGroups: ["sg-0be8fa4de860618bb"],




containerSubnets: ["subnet-0be8fa4de860618bb"],




loadBalancerSubnets: ["subnet-8be8fa4de850618ff"]



}


});

```

These are listed under the `vpc` prop of the `Cluster` component.
* * *

## [Attach to a resource](https://sst.dev/docs/reference-resources#attach-to-a-resource)

Referencing existing resources also comes in handy when you are attaching to an existing resource. For example, to add a subscriber to an externally created queue:
sst.config.ts

```typescript

sst.aws.Queue.subscribe("arn:aws:sqs:us-east-1:123456789012:MyQueue", "src/subscriber.handler");

```

Here we are using the `static subscribe` method of the `Queue` component. And it takes the queue ARN that you are trying to attach to.
There are a few other built-in SST components that have `static` methods like this.

* `Bus`
* `Dynamo`
* `SnsTopic`
* `KinesisStream`

With this you can continue to manage the root resource outside of SST, while still being able to attach to them.

[Skip to content](https://sst.dev/docs/component/aws/realtime#_top)

# Realtime

The `Realtime` component lets you publish and subscribe to messages in realtime.
It offers a **topic-based** messaging network using
Also, provides an [SDK](https://sst.dev/docs/component/aws/realtime#sdk) to authorize clients, grant permissions to subscribe, and publish to topics.
IoT is shared across all apps and stages in your AWS account. So you need to prefix the topics by the app and stage name.
There is **only 1 IoT endpoint** per region per AWS account. Messages from all apps and stages are published to the same IoT endpoint. Make sure to prefix the topics by the app and stage name.

#### [Create a realtime endpoint](https://sst.dev/docs/component/aws/realtime#create-a-realtime-endpoint)

sst.config.ts

```typescript


const server = newsst.aws.Realtime("MyServer", {




authorizer: "src/authorizer.handler"




});


```

#### [Authorize the client](https://sst.dev/docs/component/aws/realtime#authorize-the-client)

src/authorizer.ts

```typescript

import { Resource } from"sst/aws";

import { realtime } from"sst/aws/realtime";

export const handler = realtime.authorizer(async (token) => {

// Validate the token

// Return the topics to subscribe and publish

return {

subscribe: [`${Resource.App.name}/${Resource.App.stage}/chat/room1`],

publish: [`${Resource.App.name}/${Resource.App.stage}/chat/room1`],

};

});

```

#### [Publish and receive messages in your frontend](https://sst.dev/docs/component/aws/realtime#publish-and-receive-messages-in-your-frontend)

app/page.tsx```

import { Resource } from"sst/aws";

const client = newmqtt.MqttClient();

// Configure with

// - Resource.Realtime.endpoint

// - Resource.Realtime.authorizer

const connection = client.new_connection(config);

// Subscribe messages

connection.on("message", (topic, payload)=> {

// Handle the message

});

// Publish messages

connection.publish(topic, payload, mqtt.QoS.AtLeastOnce);

```

#### [Subscribe messages in your backend](https://sst.dev/docs/component/aws/realtime#subscribe-messages-in-your-backend)

sst.config.ts
```typescript

server.subscribe("src/subscriber.handler", {

filter: `${$app.name}/${$app.stage}/chat/room1`

});

```

#### [Publish message from your backend](https://sst.dev/docs/component/aws/realtime#publish-message-from-your-backend)

src/lambda.ts

```typescript


import { IoTDataPlaneClient, PublishCommand } from"@aws-sdk/client-iot-data-plane";




const data = newIoTDataPlaneClient();




await data.send(




newPublishCommand({




payload: Buffer.from(




JSON.stringify({ message: "Hello world" })



),



topic: `${Resource.App.name}/${Resource.App.stage}/chat/room1`,



})


);

```

* * *

## [Constructor](https://sst.dev/docs/component/aws/realtime#constructor)

```


newRealtime(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/realtime#parameters)

* `name` `string`
* `args` [`RealtimeArgs`](https://sst.dev/docs/component/aws/realtime#realtimeargs)
* `opts?`

## [RealtimeArgs](https://sst.dev/docs/component/aws/realtime#realtimeargs)

### [authorizer](https://sst.dev/docs/component/aws/realtime#authorizer)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`>`
The Lambda function that’ll be used to authorize the client on connection.

```

{



authorizer: "src/authorizer.handler"



}

```

### [transform?](https://sst.dev/docs/component/aws/realtime#transform)

**Type** `Object`

* [`authorizer?`](https://sst.dev/docs/component/aws/realtime#transform-authorizer)

[Transform](https://sst.dev/docs/components#transform) how this subscription creates its underlying resources.

#### [transform.authorizer?](https://sst.dev/docs/component/aws/realtime#transform-authorizer)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the IoT authorizer resource.

## [Properties](https://sst.dev/docs/component/aws/realtime#properties)

### [authorizer](https://sst.dev/docs/component/aws/realtime#authorizer-1)

**Type** `Output``<``string``>`
The name of the IoT authorizer.

### [endpoint](https://sst.dev/docs/component/aws/realtime#endpoint)

**Type** `Output``<``string``>`
The IoT endpoint.

### [nodes](https://sst.dev/docs/component/aws/realtime#nodes)

**Type** `Object`

* [`authHandler`](https://sst.dev/docs/component/aws/realtime#nodes-authhandler)
* [`authorizer`](https://sst.dev/docs/component/aws/realtime#nodes-authorizer)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.authHandler](https://sst.dev/docs/component/aws/realtime#nodes-authhandler)

**Type** `Output``<`[`Function`](https://sst.dev/docs/component/aws/function)`>`
The IoT authorizer function resource.

#### [nodes.authorizer](https://sst.dev/docs/component/aws/realtime#nodes-authorizer)

**Type**
The IoT authorizer resource.

## [SDK](https://sst.dev/docs/component/aws/realtime#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/realtime#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `authorizer` `string`
The name of the IoT authorizer.
* `endpoint` `string`
The IoT endpoint.

The `realtime` client SDK is available through the following.
src/authorizer.ts

```typescript

import { realtime } from"sst/aws/realtime";

```

* * *

### [authorizer](https://sst.dev/docs/component/aws/realtime#authorizer-2)

```

realtime.authorizer(input)

```

#### [Parameters](https://sst.dev/docs/component/aws/realtime#parameters-1)

* `input` `(token:`string`) =>`Promise``<`[`AuthResult`](https://sst.dev/docs/component/aws/realtime#authresult)`>``

**Returns**
Creates an authorization handler for the `Realtime` component. It validates the token and grants permissions for the topics the client can subscribe and publish to.
src/authorizer.ts

```typescript


export const handler = realtime.authorizer(async (token) => {



// Validate the token



console.log(token);



// Return the topics to subscribe and publish


return {



subscribe: ["*"],




publish: ["*"],



};



});


```

### [AuthResult](https://sst.dev/docs/component/aws/realtime#authresult)

**Type** `Object`

* [`disconnectAfterInSeconds?`](https://sst.dev/docs/component/aws/realtime#authresult-disconnectafterinseconds)
* [`policyDocuments?`](https://sst.dev/docs/component/aws/realtime#authresult-policydocuments)
* [`principalId?`](https://sst.dev/docs/component/aws/realtime#authresult-principalid)
* [`publish?`](https://sst.dev/docs/component/aws/realtime#authresult-publish)
* [`refreshAfterInSeconds?`](https://sst.dev/docs/component/aws/realtime#authresult-refreshafterinseconds)
* [`subscribe?`](https://sst.dev/docs/component/aws/realtime#authresult-subscribe)

#### [AuthResult.disconnectAfterInSeconds?](https://sst.dev/docs/component/aws/realtime#authresult-disconnectafterinseconds)

**Type** `number`
**Default** `86400`
The maximum duration in seconds of the connection to IoT Core.
This is set when the connection is established and cannot be modified during subsequent policy refresh authorization handler invocations.
The minimum value is 300 seconds, and the maximum is 86400 seconds.

#### [AuthResult.policyDocuments?](https://sst.dev/docs/component/aws/realtime#authresult-policydocuments)

**Type** `[]`
Any additional
There’s a maximum of 10 policy documents. Where each document can contain a maximum of 2048 characters.

```

{


policyDocuments: [


{



Version: "2012-10-17",



Statement: [


{



Action: "iot:Publish",




Effect: "Allow",




Resource: "*"



}


]


}


]


}

```

#### [AuthResult.principalId?](https://sst.dev/docs/component/aws/realtime#authresult-principalid)

**Type** `string`
The principal ID of the authorized client. This could be a user ID, username, or phone number.
The value must be an alphanumeric string with at least one, and no more than 128, characters and match the regex pattern, `([a-zA-Z0-9]){1,128}`.

#### [AuthResult.publish?](https://sst.dev/docs/component/aws/realtime#authresult-publish)

**Type** `string``[]`
The topics the client can publish to.
For example, this publishes to two specific topics.

```

{



publish: ["chat/room1", "chat/room2"]



}

```

And to publish to all topics under a given prefix.

```

{



publish: ["chat/*"]



}

```

#### [AuthResult.refreshAfterInSeconds?](https://sst.dev/docs/component/aws/realtime#authresult-refreshafterinseconds)

**Type** `number`
The duration in seconds between policy refreshes. After the given duration, IoT Core will invoke the authorization handler function.
The minimum value is 300 seconds, and the maximum value is 86400 seconds.

#### [AuthResult.subscribe?](https://sst.dev/docs/component/aws/realtime#authresult-subscribe)

**Type** `string``[]`
The topics the client can subscribe to.
For example, this subscribes to two specific topics.

```

{



subscribe: ["chat/room1", "chat/room2"]



}

```

And to subscribe to all topics under a given prefix.

```

{



subscribe: ["chat/*"]



}

```

## [Methods](https://sst.dev/docs/component/aws/realtime#methods)

### [subscribe](https://sst.dev/docs/component/aws/realtime#subscribe)

```


subscribe(subscriber, args)


```

#### [Parameters](https://sst.dev/docs/component/aws/realtime#parameters-2)

* `subscriber` `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
The function that’ll be notified.
* `args` [`RealtimeSubscriberArgs`](https://sst.dev/docs/component/aws/realtime#realtimesubscriberargs)
Configure the subscription.

**Returns** `Output``<`[`RealtimeLambdaSubscriber`](https://sst.dev/docs/component/aws/realtime-lambda-subscriber)`>`
Subscribe to this Realtime server.
sst.config.ts

```typescript

server.subscribe("src/subscriber.handler", {

filter: `${$app.name}/${$app.stage}/chat/room1`

});

```

Customize the subscriber function.
sst.config.ts

```typescript


server.subscribe(



{



handler: "src/subscriber.handler",




timeout: "60 seconds"



},


{



filter: `${$app.name}/${$app.stage}/chat/room1`



}


);

```

Or pass in the ARN of an existing Lambda function.
sst.config.ts

```typescript

server.subscribe("arn:aws:lambda:us-east-1:123456789012:function:my-function", {

filter: `${$app.name}/${$app.stage}/chat/room1`

});

```

## [RealtimeSubscriberArgs](https://sst.dev/docs/component/aws/realtime#realtimesubscriberargs)

### [filter](https://sst.dev/docs/component/aws/realtime#filter)

**Type** `Input``<``string``>`
Filter the topics that’ll be processed by the subscriber.
Learn more about
Subscribe to a specific topic.

```

{

filter: `${$app.name}/${$app.stage}/chat/room1`

}

```

Subscribe to all topics under a prefix.

```

{

filter: `${$app.name}/${$app.stage}/chat/#`

}

```

### [transform?](https://sst.dev/docs/component/aws/realtime#transform-1)

**Type** `Object`

* [`topicRule?`](https://sst.dev/docs/component/aws/realtime#transform-topicrule)

[Transform](https://sst.dev/docs/components#transform) how this subscription creates its underlying resources.

#### [transform.topicRule?](https://sst.dev/docs/component/aws/realtime#transform-topicrule)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the IoT Topic rule resource.

[Skip to content](https://sst.dev/docs/component/aws/queue#_top)

# Queue

The `Queue` component lets you add a serverless queue to your app. It uses

#### [Create a queue](https://sst.dev/docs/component/aws/queue#create-a-queue)

sst.config.ts

```typescript


const queue = newsst.aws.Queue("MyQueue");


```

#### [Make it a FIFO queue](https://sst.dev/docs/component/aws/queue#make-it-a-fifo-queue)

You can optionally make it a FIFO queue.
sst.config.ts

```typescript

new sst.aws.Queue("MyQueue", {

fifo: true

});

```

#### [Add a subscriber](https://sst.dev/docs/component/aws/queue#add-a-subscriber)

sst.config.ts

```typescript


queue.subscribe("src/subscriber.handler");


```

#### [Link the queue to a resource](https://sst.dev/docs/component/aws/queue#link-the-queue-to-a-resource)

You can link the queue to other resources, like a function or your Next.js app.
sst.config.ts

```typescript

new sst.aws.Nextjs("MyWeb", {

link: [queue]

});

```

Once linked, you can send messages to the queue from your function code.
app/page.tsx```

import { Resource } from"sst";

import { SQSClient, SendMessageCommand } from"@aws-sdk/client-sqs";

const sqs = newSQSClient({});

await sqs.send(newSendMessageCommand({

QueueUrl: Resource.MyQueue.url,

MessageBody: "Hello from Next.js!"

}));

```

* * *

## [Constructor](https://sst.dev/docs/component/aws/queue#constructor)

```

newQueue(name, args?, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/queue#parameters)

* `name` `string`
* `args?` [`QueueArgs`](https://sst.dev/docs/component/aws/queue#queueargs)
* `opts?`

## [QueueArgs](https://sst.dev/docs/component/aws/queue#queueargs)

### [delay?](https://sst.dev/docs/component/aws/queue#delay)

**Type** `Input``<``“``${number} minute``”`` | ``“``${number} minutes``”`` | ``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“0 seconds”`
The period of time which the delivery of all messages in the queue is delayed.
This can range from 0 seconds to 900 seconds (15 minutes).

```

{

delay: "10 seconds"

}

```

### [dlq?](https://sst.dev/docs/component/aws/queue#dlq)

**Type** `Input``<``string`` | ``Object``>`

* [`queue`](https://sst.dev/docs/component/aws/queue#dlq-queue)
* [`retry`](https://sst.dev/docs/component/aws/queue#dlq-retry)

Optionally add a dead-letter queue or DLQ for this queue.
A dead-letter queue is used to store messages that can’t be processed successfully by the subscriber function after the `retry` limit is reached.
This takes either the ARN of the dead-letter queue or an object to configure how the dead-letter queue is used.
For example, here’s how you can create a dead-letter queue and link it to the main queue.
sst.config.ts
```typescript

const deadLetterQueue = newsst.aws.Queue("MyDLQ");

new sst.aws.Queue("MyQueue", {

dlq: deadLetterQueue.arn,

});

```

By default, the main queue will retry processing the message 3 times before sending it to the dead-letter queue. You can customize this.
sst.config.ts

```typescript


new sst.aws.Queue("MyQueue", {



dlq: {



retry: 5,




queue: deadLetterQueue.arn,



}


});

```

#### [dlq.queue](https://sst.dev/docs/component/aws/queue#dlq-queue)

**Type** `Input``<``string``>`
The ARN of the dead-letter queue.

#### [dlq.retry](https://sst.dev/docs/component/aws/queue#dlq-retry)

**Type** `Input``<``number``>`
**Default** `3`
The number of times the main queue will retry the message before sending it to the dead-letter queue.

### [fifo?](https://sst.dev/docs/component/aws/queue#fifo)

**Type** `Input``<``boolean`` | ``Object``>`

* [`contentBasedDeduplication?`](https://sst.dev/docs/component/aws/queue#fifo-contentbaseddeduplication)

**Default** `false`
FIFO or _first-in-first-out_ queues are designed to guarantee that messages are processed exactly once and in the order that they are sent.
Changing a standard queue to a FIFO queue (or the other way around) will cause the queue to be destroyed and recreated.

```

{



fifo: true



}

```

By default, content based deduplication is disabled. You can enable it by configuring the `fifo` property.

```

{


fifo: {



contentBasedDeduplication: true



}


}

```

#### [fifo.contentBasedDeduplication?](https://sst.dev/docs/component/aws/queue#fifo-contentbaseddeduplication)

**Type** `Input``<``boolean``>`
**Default** `false`
Content-based deduplication automatically generates a deduplication ID by hashing the message body to prevent duplicate message delivery.

### [transform?](https://sst.dev/docs/component/aws/queue#transform)

**Type** `Object`

* [`queue?`](https://sst.dev/docs/component/aws/queue#transform-queue)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.queue?](https://sst.dev/docs/component/aws/queue#transform-queue)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the SQS Queue resource.

### [visibilityTimeout?](https://sst.dev/docs/component/aws/queue#visibilitytimeout)

**Type** `Input``<``“``${number} minute``”`` | ``“``${number} minutes``”`` | ``“``${number} hour``”`` | ``“``${number} hours``”`` | ``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“30 seconds”`
Visibility timeout is a period of time during which a message is temporarily invisible to other consumers after a consumer has retrieved it from the queue. This mechanism prevents other consumers from processing the same message concurrently, ensuring that each message is processed only once.
This timeout can range from 0 seconds to 12 hours.

```

{



visibilityTimeout: "1 hour"



}

```

## [Properties](https://sst.dev/docs/component/aws/queue#properties)

### [arn](https://sst.dev/docs/component/aws/queue#arn)

**Type** `Output``<``string``>`
The ARN of the SQS Queue.

### [nodes](https://sst.dev/docs/component/aws/queue#nodes)

**Type** `Object`

* [`queue`](https://sst.dev/docs/component/aws/queue#nodes-queue)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.queue](https://sst.dev/docs/component/aws/queue#nodes-queue)

**Type**
The Amazon SQS Queue.

### [url](https://sst.dev/docs/component/aws/queue#url)

**Type** `Output``<``string``>`
The SQS Queue URL.

## [SDK](https://sst.dev/docs/component/aws/queue#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/queue#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `url` `string`
The SQS Queue URL.

## [Methods](https://sst.dev/docs/component/aws/queue#methods)

### [subscribe](https://sst.dev/docs/component/aws/queue#subscribe)

```


subscribe(subscriber, args?, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/queue#parameters-1)

* `subscriber` `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
The function that’ll be notified.
* `args?` [`QueueSubscriberArgs`](https://sst.dev/docs/component/aws/queue#queuesubscriberargs)
Configure the subscription.
* `opts?`

**Returns** `Output``<`[`QueueLambdaSubscriber`](https://sst.dev/docs/component/aws/queue-lambda-subscriber)`>`
Subscribe to this queue.
sst.config.ts

```typescript

queue.subscribe("src/subscriber.handler");

```

Add a filter to the subscription.
sst.config.ts

```typescript


queue.subscribe("src/subscriber.handler", {



filters: [


{


body: {



RequestCode: ["BBBB"]



}


}


]


});

```

Customize the subscriber function.
sst.config.ts

```typescript

queue.subscribe({

handler: "src/subscriber.handler",

timeout: "60 seconds"

});

```

Or pass in the ARN of an existing Lambda function.
sst.config.ts

```typescript


queue.subscribe("arn:aws:lambda:us-east-1:123456789012:function:my-function");


```

### [static get](https://sst.dev/docs/component/aws/queue#static-get)

```


Queue.get(name, queueUrl, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/queue#parameters-2)

* `name` `string`
The name of the component.
* `queueUrl` `Input``<``string``>`
The URL of the existing SQS Queue.
* `opts?`

**Returns** [`Queue`](https://sst.dev/docs/component/aws/)
Reference an existing SQS Queue with its queue URL. This is useful when you create a queue in one stage and want to share it in another stage. It avoids having to create a new queue in the other stage.
You can use the `static get` method to share SQS queues across stages.
Imagine you create a queue in the `dev` stage. And in your personal stage `frank`, instead of creating a new queue, you want to share the queue from `dev`.
sst.config.ts

```typescript

const queue = $app.stage === "frank"

? sst.aws.Queue.get("MyQueue", "<https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue>")

:new sst.aws.Queue("MyQueue");

```

Here `https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue` is the URL of the queue created in the `dev` stage. You can find this by outputting the queue URL in the `dev` stage.
sst.config.ts

```typescript


return queue.url;


```

### [static subscribe](https://sst.dev/docs/component/aws/queue#static-subscribe)

```


Queue.subscribe(queueArn, subscriber, args?, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/queue#parameters-3)

* `queueArn` `Input``<``string``>`
The ARN of the SQS Queue to subscribe to.
* `subscriber` `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
The function that’ll be notified.
* `args?` [`QueueSubscriberArgs`](https://sst.dev/docs/component/aws/queue#queuesubscriberargs)
Configure the subscription.
* `opts?`

**Returns** `Output``<`[`QueueLambdaSubscriber`](https://sst.dev/docs/component/aws/queue-lambda-subscriber)`>`
Subscribe to an SQS Queue that was not created in your app.
For example, let’s say you have an existing SQS Queue with the following ARN.
sst.config.ts

```typescript

const queueArn = "arn:aws:sqs:us-east-1:123456789012:MyQueue";

```

You can subscribe to it by passing in the ARN.
sst.config.ts

```typescript


sst.aws.Queue.subscribe(queueArn, "src/subscriber.handler");


```

Add a filter to the subscription.
sst.config.ts

```typescript

sst.aws.Queue.subscribe(queueArn, "src/subscriber.handler", {

filters: [

{

body: {

RequestCode: ["BBBB"]

}

}

]

});

```

Customize the subscriber function.
sst.config.ts

```typescript


sst.aws.Queue.subscribe(queueArn, {




handler: "src/subscriber.handler",




timeout: "60 seconds"



});

```

## [QueueSubscriberArgs](https://sst.dev/docs/component/aws/queue#queuesubscriberargs)

### [batch?](https://sst.dev/docs/component/aws/queue#batch)

**Type** `Input``<``Object``>`

* [`partialResponses?`](https://sst.dev/docs/component/aws/queue#batch-partialresponses)
* [`size?`](https://sst.dev/docs/component/aws/queue#batch-size)
* [`window?`](https://sst.dev/docs/component/aws/queue#batch-window)

**Default** `{size: 10, window: “20 seconds”, partialResponses: false}`
Configure batch processing options for the consumer function.

#### [batch.partialResponses?](https://sst.dev/docs/component/aws/queue#batch-partialresponses)

**Type** `Input``<``boolean``>`
**Default** `false`
Whether to return partial successful responses for a batch.
Enables reporting of individual message failures in a batch. When enabled, only failed messages become visible in the queue again, preventing unnecessary reprocessing of successful messages.
The handler function must return a response with failed message IDs.
Ensure your Lambda function is updated to handle `batchItemFailures` responses when enabling this option.
Read more about
Enable partial responses.

```

{


batch: {



partialResponses: true



}


}

```

For a batch of messages (id1, id2, id3, id4, id5), if id2 and id4 fail:

```

{



"batchItemFailures": [



{



"itemIdentifier": "id2"



},


{



"itemIdentifier": "id4"



}


]


}

```

This makes only id2 and id4 visible again in the queue.

#### [batch.size?](https://sst.dev/docs/component/aws/queue#batch-size)

**Type** `Input``<``number``>`
**Default** `10`
The maximum number of events that will be processed together in a single invocation of the consumer function.
Value must be between 1 and 10000.
When `size` is set to a value greater than 10, `window` must be set to at least `1 second`.
Set batch size to 1. This will process events individually.

```

{


batch: {



size: 1



}


}

```

#### [batch.window?](https://sst.dev/docs/component/aws/queue#batch-window)

**Type** `Input``<``“``${number} minute``”`` | ``“``${number} minutes``”`` | ``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“0 seconds”`
The maximum amount of time to wait for collecting events before sending the batch to the consumer function, even if the batch size hasn’t been reached.
Value must be between 0 seconds and 5 minutes (300 seconds).

```

{


batch: {



window: "20 seconds"



}


}

```

### [filters?](https://sst.dev/docs/component/aws/queue#filters)

**Type** `Input``<``Input``<``Record``<``string`, `any``>``>``[]``>`
Filter the records that’ll be processed by the `subscriber` function.
You can pass in up to 5 different filters.
You can pass in up to 5 different filter policies. These will logically ORed together. Meaning that if any single policy matches, the record will be processed. Learn more about the
For example, if you Queue contains records in this JSON format.

```

{



RecordNumber: 0000,




RequestCode: "AAAA",




TimeStamp: "yyyy-mm-ddThh:mm:ss"



}

```

To process only those records where the `RequestCode` is `BBBB`.

```

{


filters: [


{


body: {



RequestCode: ["BBBB"]



}


}


]


}

```

And to process only those records where `RecordNumber` greater than `9999`.

```

{


filters: [


{


body: {



RecordNumber: [{ numeric: [ ">", 9999 ] }]



}


}


]


}

```

### [transform?](https://sst.dev/docs/component/aws/queue#transform-1)

**Type** `Object`

* [`eventSourceMapping?`](https://sst.dev/docs/component/aws/queue#transform-eventsourcemapping)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.eventSourceMapping?](https://sst.dev/docs/component/aws/queue#transform-eventsourcemapping)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Lambda Event Source Mapping resource.

[Skip to content](https://sst.dev/docs/import-resources#_top)

# Import Resources

Importing is the process of bringing some previously created resources into your SST app. This’ll allow SST to manage them moving forward.
This is useful for when you are migrating to SST or if you had manually created some resources in the past.
* * *

## [How it works](https://sst.dev/docs/import-resources#how-it-works)

SST keeps a [state](https://sst.dev/docs/state/) of your app. It contains all the resources that are managed by your app.
Once you import a resource it’s managed by SST moving forward.
When you import a resource, it gets added to this state. This means that if you remove this resource in your code, it’ll also remove the resource.
It’s as if this resource had been created by your app.
* * *

#### [When not to import](https://sst.dev/docs/import-resources#when-not-to-import)

This is fine for most cases. But for some teams these resources might be managed by other teams. Or they are being managed by a different IaC tool. Meaning that you don’t want to manage it in your app.
Do not import resources that are being managed by another team or a different IaC tool.
In these cases you should not be importing these resources. You are probably looking to [reference these resources](https://sst.dev/docs/reference-resources/).
* * *

## [How to import](https://sst.dev/docs/import-resources#how-to-import)

You import resources by passing in a property of the resource you want to import into your app. Resources have a property that you can import with and this is different for different resources. We’ll look at this below.
If you are importing into an SST component, you’ll need to use a [`transform`](https://sst.dev/docs/components/#transform) to pass it into the underlying resource.
So let’s look at two examples.

  1. Importing into an SST component
  2. Importing into a Pulumi resource

* * *

### [SST component](https://sst.dev/docs/import-resources#sst-component)

Let’s start with an existing S3 Bucket with the following name.

```

mybucket-xnbmhcvd

```

We want to import this bucket into the [`Bucket`](https://sst.dev/docs/component/aws/bucket/) component.

  1. Start by adding the `import` option in the `transform`.
sst.config.ts

```typescript

new sst.aws.Bucket("MyBucket", {

transform: {

bucket: (args, opts)=> {

opts.import="mybucket-xnbmhcvd";

}

}

});

```

The `transform.bucket` is telling this component that instead of creating a new underlying S3 Bucket resource, we want to import an existing bucket.
Let’s deploy this.

```

sstdeploy

```

This will give you an error that looks something like this.

```

✕  Failed

inputs to import do not match the existing resource

Set the following in your transform:

* `args.bucket = "mybucket-xnbmhcvd";`

* `args.forceDestroy = undefined;`

```

This is telling us that the resource that the `Bucket` component is trying to create does not match the one you are trying to import. This makes sense because you might’ve previously created this with a configuration that’s different from what SST creates by default.
  2. Update the `args`
The above error tells us exactly what we need to do next. Add the given lines to your `transform`.
sst.config.ts

```typescript


new sst.aws.Bucket("MyBucket", {



transform: {



bucket: (args, opts)=> {




args.bucket="mybucket-xnbmhcvd";




args.forceDestroy=undefined;




opts.import="mybucket-xnbmhcvd";



}


}


});

```

Now if you deploy this again.

```


sstdeploy


```

You’ll notice that the bucket has been imported.

```


|ImportedMyBucketaws:s3:BucketV2


```

  3. Finally, to clean things up we can remove the `import` line.
sst.config.ts

```typescript

new sst.aws.Bucket("MyBucket", {

transform: {

bucket: (args, opts)=> {

args.bucket="mybucket-xnbmhcvd";

args.forceDestroy=undefined;

opts.import="mybucket-xnbmhcvd";

}

}

});

```

This bucket is now managed by your app and you can now deploy as usual.
You **do not want to remove** the `args` changes. This matters for the `args.bucket` prop because the name is generated by SST. So if you remove this, SST will generate a new bucket name and remove the old one!

* * *

### [Pulumi resource](https://sst.dev/docs/import-resources#pulumi-resource)

You might want to also import resources into your SST app that don’t have a built-in SST component. In these cases, you can import them into a low-level Pulumi resource.
Let’s take the same S3 Bucket example. Say you have an existing bucket with the following name.

```

mybucket-xnbmhcvd

```

We want to import this bucket into the

  1. Start by adding the `import` option.
sst.config.ts

```typescript


new aws.s3.BucketV2("MyBucket",



{



objectLockEnabled: undefined



},


{



import: "mybucket-xnbmhcvd"



}


);

```

The `objectLockEnabled` prop here, is for illustrative purposes. We are trying to demonstrate a case where you are importing a resource in a way that it wasn’t created.
Let’s deploy this.

```


sstdeploy


```

This will give you an error that looks something like this.

```

✕  Failed


inputs to import do not match the existing resource


Set the following:


- `objectLockEnabled: undefined,`

```

This is telling us that the resource that the `BucketV2` component is trying to create does not match the one you are trying to import.
This makes sense because you might’ve previously created this with a configuration that’s different from what you are defining. Recall the `objectLockEnabled` prop we had added above.
  2. Update the `args`
The above error tells us exactly what we need to do next. Add the given lines in your `args`.
sst.config.ts

```typescript

new aws.s3.BucketV2("MyBucket",

{

objectLockEnabled: undefined

},

{

import: "mybucket-xnbmhcvd"

}

);

```

Now if you deploy this again.

```

sstdeploy

```

You’ll notice that the bucket has been imported.

```

|ImportedMyBucketaws:s3:BucketV2

```

  3. Finally, to clean things up we can remove the `import` line.
sst.config.ts

```typescript


new aws.s3.BucketV2("MyBucket",



{



objectLockEnabled: undefined



},


{



import: "mybucket-xnbmhcvd"



}


);

```

This bucket is now managed by your app and you can now deploy as usual.

* * *

## [Import properties](https://sst.dev/docs/import-resources#import-properties)

In the above examples we are importing a bucket using the bucket name. We need the bucket name because that’s what AWS internally uses to do a lookup. But this is different for different resources.
So we’ve compiled a list of the most common resources you might import, along with the **property to import them with**.
You can look this up by going to the **Import** section of a resource’s doc. For example, here’s the one for a
* * *
The following table lists the properties you need to pass in to the `import` prop of the given resource to be able to import it.
For example, for `aws.s3.BucketV2`, the property is _bucket name_ and it looks something like, `some-unique-bucket-name`.

Resource | Property | Example  
---|---|---  
| VPC ID | `vpc-a01106c2`  
| Role name | `role-name`  
| Queue URL | `https://queue.amazonaws.com/80398EXAMPLE/MyQueue`  
| Topic ARN | `arn:aws:sns:us-west-2:0123456789012:my-topic`  
| Cluster identifier | `aurora-prod-cluster`  
| Cluster and service name | `cluster-name/service-name`  
| Cluster name | `cluster-name`  
| Bucket name | `bucket-name`  
| Stream name | `my-kinesis-stream`  
| Table name | `table-name`  
| Function name | `function-name`  
| API ID | `12345abcde`  
| User Pool ID | `us-east-1_abc123`  
| REST API ID | `12345abcde`  
| Log Group name | `my-log-group`  
| Identity Pool ID | `us-east-1:1a234567-8901-234b-5cde-f6789g01h2i3`  
| Distribution ID | `E74FTE3EXAMPLE`  
Feel free to _Edit this page_ and submit a PR if you want to add to this list.

[Skip to content](https://sst.dev/docs/component/aws/vpc-v1#_top)

# Vpc.v1

The `Vpc` component lets you add a VPC to your app, but it has been deprecated because it does not support modifying the number of Availability Zones (AZs) after VPC creation.
For existing usage, rename `sst.aws.Vpc` to `sst.aws.Vpc.v1`. For new VPCs, use the latest [`Vpc`](https://sst.dev/docs/component/aws/vpc) component instead.
This component has been deprecated.
This creates a VPC with 2 Availability Zones by default. It also creates the following resources:

  1. A security group.
  2. A public subnet in each AZ.
  3. A private subnet in each AZ.
  4. An Internet Gateway, all the traffic from the public subnets are routed through it.
  5. A NAT Gateway in each AZ. All the traffic from the private subnets are routed to the NAT Gateway in the same AZ.

By default, this creates two NAT Gateways, one in each AZ. And it roughly costs $33 per NAT Gateway per month.
NAT Gateways are billed per hour and per gigabyte of data processed. By default, this creates a NAT Gateway in each AZ. And this would be roughly $33 per NAT Gateway per month. Make sure to

#### [Create a VPC](https://sst.dev/docs/component/aws/vpc-v1#create-a-vpc)

sst.config.ts

```typescript

new sst.aws.Vpc.v1("MyVPC");

```

#### [Create it with 3 Availability Zones](https://sst.dev/docs/component/aws/vpc-v1#create-it-with-3-availability-zones)

sst.config.ts

```typescript


new sst.aws.Vpc.v1("MyVPC", {




az: 3



});

```

* * *

## [Constructor](https://sst.dev/docs/component/aws/vpc-v1#constructor)

```


new Vpc.v1(name, args?, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/vpc-v1#parameters)

* `name` `string`
* `args?` [`VpcArgs`](https://sst.dev/docs/component/aws/vpc-v1#vpcargs)
* `opts?`

## [VpcArgs](https://sst.dev/docs/component/aws/vpc-v1#vpcargs)

### [az?](https://sst.dev/docs/component/aws/vpc-v1#az)

**Type** `Input``<``number``>`
**Default** `2`
Number of Availability Zones or AZs for the VPC. By default, it creates a VPC with 2 AZs since services like RDS and Fargate need at least 2 AZs.

```

{



az: 3



}

```

### [transform?](https://sst.dev/docs/component/aws/vpc-v1#transform)

**Type** `Object`

* [`elasticIp?`](https://sst.dev/docs/component/aws/vpc-v1#transform-elasticip)
* [`internetGateway?`](https://sst.dev/docs/component/aws/vpc-v1#transform-internetgateway)
* [`natGateway?`](https://sst.dev/docs/component/aws/vpc-v1#transform-natgateway)
* [`privateRouteTable?`](https://sst.dev/docs/component/aws/vpc-v1#transform-privateroutetable)
* [`privateSubnet?`](https://sst.dev/docs/component/aws/vpc-v1#transform-privatesubnet)
* [`publicRouteTable?`](https://sst.dev/docs/component/aws/vpc-v1#transform-publicroutetable)
* [`publicSubnet?`](https://sst.dev/docs/component/aws/vpc-v1#transform-publicsubnet)
* [`securityGroup?`](https://sst.dev/docs/component/aws/vpc-v1#transform-securitygroup)
* [`vpc?`](https://sst.dev/docs/component/aws/vpc-v1#transform-vpc)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.elasticIp?](https://sst.dev/docs/component/aws/vpc-v1#transform-elasticip)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 Elastic IP resource.

#### [transform.internetGateway?](https://sst.dev/docs/component/aws/vpc-v1#transform-internetgateway)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 Internet Gateway resource.

#### [transform.natGateway?](https://sst.dev/docs/component/aws/vpc-v1#transform-natgateway)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 NAT Gateway resource.

#### [transform.privateRouteTable?](https://sst.dev/docs/component/aws/vpc-v1#transform-privateroutetable)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 route table resource for the private subnet.

#### [transform.privateSubnet?](https://sst.dev/docs/component/aws/vpc-v1#transform-privatesubnet)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 private subnet resource.

#### [transform.publicRouteTable?](https://sst.dev/docs/component/aws/vpc-v1#transform-publicroutetable)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 route table resource for the public subnet.

#### [transform.publicSubnet?](https://sst.dev/docs/component/aws/vpc-v1#transform-publicsubnet)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 public subnet resource.

#### [transform.securityGroup?](https://sst.dev/docs/component/aws/vpc-v1#transform-securitygroup)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 Security Group resource.

#### [transform.vpc?](https://sst.dev/docs/component/aws/vpc-v1#transform-vpc)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 VPC resource.

## [Properties](https://sst.dev/docs/component/aws/vpc-v1#properties)

### [id](https://sst.dev/docs/component/aws/vpc-v1#id)

**Type** `Output``<``string``>`
The VPC ID.

### [nodes](https://sst.dev/docs/component/aws/vpc-v1#nodes)

**Type** `Object`

* [`elasticIps`](https://sst.dev/docs/component/aws/vpc-v1#nodes-elasticips)
* [`internetGateway`](https://sst.dev/docs/component/aws/vpc-v1#nodes-internetgateway)
* [`natGateways`](https://sst.dev/docs/component/aws/vpc-v1#nodes-natgateways)
* [`privateRouteTables`](https://sst.dev/docs/component/aws/vpc-v1#nodes-privateroutetables)
* [`privateSubnets`](https://sst.dev/docs/component/aws/vpc-v1#nodes-privatesubnets)
* [`publicRouteTables`](https://sst.dev/docs/component/aws/vpc-v1#nodes-publicroutetables)
* [`publicSubnets`](https://sst.dev/docs/component/aws/vpc-v1#nodes-publicsubnets)
* [`securityGroup`](https://sst.dev/docs/component/aws/vpc-v1#nodes-securitygroup)
* [`vpc`](https://sst.dev/docs/component/aws/vpc-v1#nodes-vpc)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.elasticIps](https://sst.dev/docs/component/aws/vpc-v1#nodes-elasticips)

**Type** `Output``<``[]``>`
The Amazon EC2 Elastic IP.

#### [nodes.internetGateway](https://sst.dev/docs/component/aws/vpc-v1#nodes-internetgateway)

**Type**
The Amazon EC2 Internet Gateway.

#### [nodes.natGateways](https://sst.dev/docs/component/aws/vpc-v1#nodes-natgateways)

**Type** `Output``<``[]``>`
The Amazon EC2 NAT Gateway.

#### [nodes.privateRouteTables](https://sst.dev/docs/component/aws/vpc-v1#nodes-privateroutetables)

**Type** `Output``<``[]``>`
The Amazon EC2 route table for the private subnet.

#### [nodes.privateSubnets](https://sst.dev/docs/component/aws/vpc-v1#nodes-privatesubnets)

**Type** `Output``<``[]``>`
The Amazon EC2 private subnet.

#### [nodes.publicRouteTables](https://sst.dev/docs/component/aws/vpc-v1#nodes-publicroutetables)

**Type** `Output``<``[]``>`
The Amazon EC2 route table for the public subnet.

#### [nodes.publicSubnets](https://sst.dev/docs/component/aws/vpc-v1#nodes-publicsubnets)

**Type** `Output``<``[]``>`
The Amazon EC2 public subnet.

#### [nodes.securityGroup](https://sst.dev/docs/component/aws/vpc-v1#nodes-securitygroup)

**Type**
The Amazon EC2 Security Group.

#### [nodes.vpc](https://sst.dev/docs/component/aws/vpc-v1#nodes-vpc)

**Type**
The Amazon EC2 VPC.

### [privateSubnets](https://sst.dev/docs/component/aws/vpc-v1#privatesubnets)

**Type** `Output``<``Output``<``string``>``[]``>`
A list of private subnet IDs in the VPC.

### [publicSubnets](https://sst.dev/docs/component/aws/vpc-v1#publicsubnets)

**Type** `Output``<``Output``<``string``>``[]``>`
A list of public subnet IDs in the VPC.

### [securityGroups](https://sst.dev/docs/component/aws/vpc-v1#securitygroups)

**Type** `Output``<``string``>``[]`
A list of VPC security group IDs.

## [Methods](https://sst.dev/docs/component/aws/vpc-v1#methods)

### [static get](https://sst.dev/docs/component/aws/vpc-v1#static-get)

```


Vpc.get(name, vpcID)


```

#### [Parameters](https://sst.dev/docs/component/aws/vpc-v1#parameters-1)

* `name` `string`
The name of the component.
* `vpcID` `Input``<``string``>`
The ID of the existing VPC.

**Returns** [`Vpc`](https://sst.dev/docs/component/aws/)
Reference an existing VPC with the given ID. This is useful when you create a VPC in one stage and want to share it in another stage. It avoids having to create a new VPC in the other stage.
You can use the `static get` method to share VPCs across stages.
Imagine you create a VPC in the `dev` stage. And in your personal stage `frank`, instead of creating a new VPC, you want to share the VPC from `dev`.
sst.config.ts

```typescript

const vpc = $app.stage === "frank"

? sst.aws.Vpc.v1.get("MyVPC", "vpc-0be8fa4de860618bb")

:new sst.aws.Vpc.v1("MyVPC");

```

Here `vpc-0be8fa4de860618bb` is the ID of the VPC created in the `dev` stage. You can find this by outputting the VPC ID in the `dev` stage.
sst.config.ts

```typescript


return {




vpc: vpc.id



};

```

[Skip to content](https://sst.dev/docs/component/vercel/dns#_top)

# Vercel DNS Adapter

The Vercel DNS Adapter is used to create DNS records to manage domains hosted on
You need to [add the Vercel provider](https://sst.dev/docs/all-providers#directory) to use this adapter.
This adapter is passed in as `domain.dns` when setting a custom domain; where `example.com` is hosted on Vercel.

```

{


domain: {



name: "example.com",




dns: sst.vercel.dns({




domain: "example.com"



})


}


}

```

#### [Configure provider](https://sst.dev/docs/component/vercel/dns#configure-provider)

  1. To use this component, add the `@pulumiverse/vercel` provider to your app.
Terminal window```

sstadd@pulumiverse/vercel

```

  2. If you don’t already have a Vercel Access Token, 
  3. Add a `VERCEL_API_TOKEN` environment variable with the access token value. If the domain belongs to a team, also add a `VERCEL_TEAM_ID` environment variable with the Team ID. You can find your Team ID inside your team’s general project settings in the Vercel dashboard.


* * *
## [Functions](https://sst.dev/docs/component/vercel/dns#functions)
### [dns](https://sst.dev/docs/component/vercel/dns#dns)
```

dns(args)

```

#### [Parameters](https://sst.dev/docs/component/vercel/dns#parameters)
  * `args` [`DnsArgs`](https://sst.dev/docs/component/vercel/dns#dnsargs)


**Returns** `Object`
## [DnsArgs](https://sst.dev/docs/component/vercel/dns#dnsargs)
### [domain](https://sst.dev/docs/component/vercel/dns#domain)
**Type** `Input``<``string``>`
The domain name in your Vercel account to create the record in.
```

{

domain: "example.com"

}

```

### [transform?](https://sst.dev/docs/component/vercel/dns#transform)
**Type** `Object`
  * [`record?`](https://sst.dev/docs/component/vercel/dns#transform-record)


[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.
####  [transform.record?](https://sst.dev/docs/component/vercel/dns#transform-record)
**Type** ` | ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Vercel record resource.


[Skip to content](https://sst.dev/docs/component/aws/cdn#_top)
# Cdn
The `Cdn` component is internally used by other components to deploy a CDN to AWS. It uses 
This component is not intended to be created directly.
You’ll find this component exposed in the `transform` of other components. And you can customize the args listed here. For example:
sst.config.ts
```typescript


new sst.aws.Nextjs("MyWeb", {



transform: {



cdn: (args)=> {




args.wait=false;



}


}


});

```

* * *

## [Constructor](https://sst.dev/docs/component/aws/cdn#constructor)

```


newCdn(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cdn#parameters)

* `name` `string`
* `args` [`CdnArgs`](https://sst.dev/docs/component/aws/cdn#cdnargs)
* `opts?`

## [CdnArgs](https://sst.dev/docs/component/aws/cdn#cdnargs)

### [comment?](https://sst.dev/docs/component/aws/cdn#comment)

**Type** `Input``<``string``>`
A comment to describe the distribution. It cannot be longer than 128 characters.

### [customErrorResponses?](https://sst.dev/docs/component/aws/cdn#customerrorresponses)

**Type** `Input``<``Input``<``>``[]``>`
One or more custom error responses.

### [defaultCacheBehavior](https://sst.dev/docs/component/aws/cdn#defaultcachebehavior)

**Type** `Input``<``>`
The default cache behavior for this distribution.

### [defaultRootObject?](https://sst.dev/docs/component/aws/cdn#defaultrootobject)

**Type** `Input``<``string``>`
An object you want CloudFront to return when a user requests the root URL. For example, the `index.html`.

### [domain?](https://sst.dev/docs/component/aws/cdn#domain)

**Type** `Input``<``string`` | ``Object``>`

* [`aliases?`](https://sst.dev/docs/component/aws/cdn#domain-aliases)
* [`cert?`](https://sst.dev/docs/component/aws/cdn#domain-cert)
* [`dns?`](https://sst.dev/docs/component/aws/cdn#domain-dns)
* [`name`](https://sst.dev/docs/component/aws/cdn#domain-name)
* [`redirects?`](https://sst.dev/docs/component/aws/cdn#domain-redirects)

Set a custom domain for your distribution.
Automatically manages domains hosted on AWS Route 53, Cloudflare, and Vercel. For other providers, you’ll need to pass in a `cert` that validates domain ownership and add the DNS records.
Built-in support for AWS Route 53, Cloudflare, and Vercel. And manual setup for other providers.
By default this assumes the domain is hosted on Route 53.

```

{



domain: "example.com"



}

```

For domains hosted on Cloudflare.

```

{


domain: {



name: "example.com",




dns: sst.cloudflare.dns()



}


}

```

Specify a `www.` version of the custom domain.

```

{


domain: {



name: "domain.com",




redirects: ["www.domain.com"]



}


}

```

#### [domain.aliases?](https://sst.dev/docs/component/aws/cdn#domain-aliases)

**Type** `Input``<``string``[]``>`
Alias domains that should be used. Unlike the `redirect` option, this keeps your visitors on this alias domain.
So if your users visit `app2.domain.com`, they will stay on `app2.domain.com` in their browser.

```

{


domain: {



name: "app1.domain.com",




aliases: ["app2.domain.com"]



}


}

```

#### [domain.cert?](https://sst.dev/docs/component/aws/cdn#domain-cert)

**Type** `Input``<``string``>`
The ARN of an ACM (AWS Certificate Manager) certificate that proves ownership of the domain. By default, a certificate is created and validated automatically.
The certificate will be created in the `us-east-1` region as required by AWS CloudFront. If you are creating your own certificate, you must also create it in `us-east-1`.
You need to pass in a `cert` for domains that are not hosted on supported `dns` providers.
To manually set up a domain on an unsupported provider, you’ll need to:

  1. Once validated, set the certificate ARN as the `cert` and set `dns` to `false`.
  2. Add the DNS records in your provider to point to the CloudFront distribution URL.

```

{


domain: {



name: "domain.com",




dns: false,




cert: "arn:aws:acm:us-east-1:112233445566:certificate/3a958790-8878-4cdc-a396-06d95064cf63"



}


}

```

#### [domain.dns?](https://sst.dev/docs/component/aws/cdn#domain-dns)

**Type** `Input``<``false`` |`[`sst.aws.dns`](https://sst.dev/docs/component/aws/dns/)` | `[`sst.cloudflare.dns`](https://sst.dev/docs/component/cloudflare/dns/)` | `[`sst.vercel.dns`](https://sst.dev/docs/component/vercel/dns/)`>`
**Default** `sst.aws.dns`
The DNS provider to use for the domain. Defaults to the AWS.
Takes an adapter that can create the DNS records on the provider. This can automate validating the domain and setting up the DNS routing.
Supports Route 53, Cloudflare, and Vercel adapters. For other providers, you’ll need to set `dns` to `false` and pass in a certificate validating ownership via `cert`.
Specify the hosted zone ID for the Route 53 domain.

```

{


domain: {



name: "example.com",




dns: sst.aws.dns({




zone: "Z2FDTNDATAQYW2"



})


}


}

```

Use a domain hosted on Cloudflare, needs the Cloudflare provider.

```

{


domain: {



name: "example.com",




dns: sst.cloudflare.dns()



}


}

```

Use a domain hosted on Vercel, needs the Vercel provider.

```

{


domain: {



name: "example.com",




dns: sst.vercel.dns()



}


}

```

#### [domain.name](https://sst.dev/docs/component/aws/cdn#domain-name)

**Type** `Input``<``string``>`
The custom domain you want to use.

```

{


domain: {



name: "example.com"



}


}

```

Can also include subdomains based on the current stage.

```

{


domain: {



name: `${$app.stage}.example.com`



}


}

```

#### [domain.redirects?](https://sst.dev/docs/component/aws/cdn#domain-redirects)

**Type** `Input``<``string``[]``>`
Alternate domains to be used. Visitors to the alternate domains will be redirected to the main `name`.
Unlike the `aliases` option, this will redirect visitors back to the main `name`.
Use this to create a `www.` version of your domain and redirect visitors to the apex domain.

```

{


domain: {



name: "domain.com",




redirects: ["www.domain.com"]



}


}

```

### [orderedCacheBehaviors?](https://sst.dev/docs/component/aws/cdn#orderedcachebehaviors)

**Type** `Input``<``Input``<``>``[]``>`
An ordered list of cache behaviors for this distribution. Listed in order of precedence. The first cache behavior will have precedence 0.

### [originGroups?](https://sst.dev/docs/component/aws/cdn#origingroups)

**Type** `Input``<``Input``<``>``[]``>`
One or more origin groups for this distribution.

### [origins](https://sst.dev/docs/component/aws/cdn#origins)

**Type** `Input``<``Input``<``>``[]``>`
One or more origins for this distribution.

### [tags?](https://sst.dev/docs/component/aws/cdn#tags)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Tags to apply to the distribution.

### [transform?](https://sst.dev/docs/component/aws/cdn#transform)

**Type** `Object`

* [`distribution`](https://sst.dev/docs/component/aws/cdn#transform-distribution)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.distribution](https://sst.dev/docs/component/aws/cdn#transform-distribution)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the CloudFront distribution resource.

### [wait?](https://sst.dev/docs/component/aws/cdn#wait)

**Type** `Input``<``boolean``>`
**Default** `true`
Whether to wait for the CloudFront distribution to be deployed before completing the deployment of the app. This is necessary if you need to use the distribution URL in other resources.

## [Properties](https://sst.dev/docs/component/aws/cdn#properties)

### [domainUrl](https://sst.dev/docs/component/aws/cdn#domainurl)

**Type** `Output``<``undefined`` | ``string``>`
If the custom domain is enabled, this is the URL of the distribution with the custom domain.

### [nodes](https://sst.dev/docs/component/aws/cdn#nodes)

**Type** `Object`

* [`distribution`](https://sst.dev/docs/component/aws/cdn#nodes-distribution)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.distribution](https://sst.dev/docs/component/aws/cdn#nodes-distribution)

**Type** `Output``<``>`
The Amazon CloudFront distribution.

### [url](https://sst.dev/docs/component/aws/cdn#url)

**Type** `Output``<``string``>`
The CloudFront URL of the distribution.

## [Methods](https://sst.dev/docs/component/aws/cdn#methods)

### [static get](https://sst.dev/docs/component/aws/cdn#static-get)

```


Cdn.get(name, distributionID, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cdn#parameters-1)

* `name` `string`
The name of the component.
* `distributionID` `Input``<``string``>`
The id of the existing CDN distribution.
* `opts?`

**Returns** [`Cdn`](https://sst.dev/docs/component/aws/)
Reference an existing CDN with the given distribution ID. This is useful when you create a Router in one stage and want to share it in another. It avoids having to create a new Router in the other stage.
You can use the `static get` method to share Routers across stages.

## [CdnDomainArgs](https://sst.dev/docs/component/aws/cdn#cdndomainargs)

### [aliases?](https://sst.dev/docs/component/aws/cdn#aliases)

**Type** `Input``<``string``[]``>`
Alias domains that should be used. Unlike the `redirect` option, this keeps your visitors on this alias domain.
So if your users visit `app2.domain.com`, they will stay on `app2.domain.com` in their browser.

```

{


domain: {



name: "app1.domain.com",




aliases: ["app2.domain.com"]



}


}

```

### [cert?](https://sst.dev/docs/component/aws/cdn#cert)

**Type** `Input``<``string``>`
The ARN of an ACM (AWS Certificate Manager) certificate that proves ownership of the domain. By default, a certificate is created and validated automatically.
The certificate will be created in the `us-east-1` region as required by AWS CloudFront. If you are creating your own certificate, you must also create it in `us-east-1`.
You need to pass in a `cert` for domains that are not hosted on supported `dns` providers.
To manually set up a domain on an unsupported provider, you’ll need to:

  1. Once validated, set the certificate ARN as the `cert` and set `dns` to `false`.
  2. Add the DNS records in your provider to point to the CloudFront distribution URL.

```

{


domain: {



name: "domain.com",




dns: false,




cert: "arn:aws:acm:us-east-1:112233445566:certificate/3a958790-8878-4cdc-a396-06d95064cf63"



}


}

```

### [dns?](https://sst.dev/docs/component/aws/cdn#dns)

**Type** `Input``<``false`` |`[`sst.aws.dns`](https://sst.dev/docs/component/aws/dns/)` | `[`sst.cloudflare.dns`](https://sst.dev/docs/component/cloudflare/dns/)` | `[`sst.vercel.dns`](https://sst.dev/docs/component/vercel/dns/)`>`
**Default** `sst.aws.dns`
The DNS provider to use for the domain. Defaults to the AWS.
Takes an adapter that can create the DNS records on the provider. This can automate validating the domain and setting up the DNS routing.
Supports Route 53, Cloudflare, and Vercel adapters. For other providers, you’ll need to set `dns` to `false` and pass in a certificate validating ownership via `cert`.
Specify the hosted zone ID for the Route 53 domain.

```

{


domain: {



name: "example.com",




dns: sst.aws.dns({




zone: "Z2FDTNDATAQYW2"



})


}


}

```

Use a domain hosted on Cloudflare, needs the Cloudflare provider.

```

{


domain: {



name: "example.com",




dns: sst.cloudflare.dns()



}


}

```

Use a domain hosted on Vercel, needs the Vercel provider.

```

{


domain: {



name: "example.com",




dns: sst.vercel.dns()



}


}

```

### [name](https://sst.dev/docs/component/aws/cdn#name)

**Type** `Input``<``string``>`
The custom domain you want to use.

```

{


domain: {



name: "example.com"



}


}

```

Can also include subdomains based on the current stage.

```

{


domain: {



name: `${$app.stage}.example.com`



}


}

```

### [redirects?](https://sst.dev/docs/component/aws/cdn#redirects)

**Type** `Input``<``string``[]``>`
Alternate domains to be used. Visitors to the alternate domains will be redirected to the main `name`.
Unlike the `aliases` option, this will redirect visitors back to the main `name`.
Use this to create a `www.` version of your domain and redirect visitors to the apex domain.

```

{


domain: {



name: "domain.com",




redirects: ["www.domain.com"]



}


}

```

[Skip to content](https://sst.dev/docs/component/aws/router#_top)

# Router

The `Router` component lets you use a CloudFront distribution to direct requests to various parts of your application like:

* A URL
* A function
* A frontend
* An S3 bucket

#### [Minimal example](https://sst.dev/docs/component/aws/router#minimal-example)

sst.config.ts

```typescript

new sst.aws.Router("MyRouter");

```

#### [Add a custom domain](https://sst.dev/docs/component/aws/router#add-a-custom-domain)

sst.config.ts

```typescript


new sst.aws.Router("MyRouter", {




domain: "myapp.com"



});

```

#### [Sharing the router across stages](https://sst.dev/docs/component/aws/router#sharing-the-router-across-stages)

sst.config.ts

```typescript

const router = $app.stage === "production"

?new sst.aws.Router("MyRouter", {

domain: {

name: "example.com",

aliases: ["*.example.com"]

}

})

: sst.aws.Router.get("MyRouter", "E1XWRGCYGTFB7Z");

```

#### [Route to a URL](https://sst.dev/docs/component/aws/router#route-to-a-url)

sst.config.ts

```typescript


const router = newsst.aws.Router("MyRouter");




router.route("/", "https://some-external-service.com");


```

#### [Route to an S3 bucket](https://sst.dev/docs/component/aws/router#route-to-an-s3-bucket)

sst.config.ts

```typescript

const myBucket = newsst.aws.Bucket("MyBucket", {

"cloudfront"

});

const router = newsst.aws.Router("MyRouter");

router.routeBucket("/files", myBucket);

```

You need to allow CloudFront to access the bucket by setting the `access` prop on the bucket.

#### [Route to a function](https://sst.dev/docs/component/aws/router#route-to-a-function)

sst.config.ts

```typescript


const router = newsst.aws.Router("MyRouter", {




domain: "example.com"




});




const myFunction = newsst.aws.Function("MyFunction", {




handler: "src/api.handler",



url: {



router,




"/api"



}



});


```

Setting the route through the function, instead of `router.route()` makes it so that `myFunction.url` gives you the URL based on the Router domain.

#### [Route to a frontend](https://sst.dev/docs/component/aws/router#route-to-a-frontend)

sst.config.ts

```typescript

const router = newsst.aws.Router("MyRouter");

const mySite = newsst.aws.Nextjs("MyWeb", {

router

});

```

Setting the route through the site, instead of `router.route()` makes it so that `mySite.url` gives you the URL based on the Router domain.

#### [Route to a frontend on a path](https://sst.dev/docs/component/aws/router#route-to-a-frontend-on-a-path)

sst.config.ts

```typescript


const router = newsst.aws.Router("MyRouter");




new sst.aws.Nextjs("MyWeb", {



router: {


instance: router,



path: "/docs"



}


});

```

If you are routing to a path, you’ll need to configure the base path in your frontend app as well. [Learn more](https://sst.dev/docs/component/aws/nextjs/#router).

#### [Route to a frontend on a subdomain](https://sst.dev/docs/component/aws/router#route-to-a-frontend-on-a-subdomain)

sst.config.ts

```typescript

const router = newsst.aws.Router("MyRouter", {

domain: {

name: "example.com",

 ["*.example.com"]

}

});

new sst.aws.Nextjs("MyWeb", {

router: {

instance: router,

domain: "docs.example.com"

}

});

```

We configure `*.example.com` as an alias so that we can route to a subdomain.

#### [How it works](https://sst.dev/docs/component/aws/router#how-it-works)

This uses a CloudFront KeyValueStore to store the routing data and a CloudFront function to route the request. As routes are added, the store is updated.
So when a request comes in, it does a lookup in the store and dynamically sets the origin based on the routing data. For frontends, that have their server functions deployed to multiple `regions`, it routes to the closest region based on the user’s location.
You might notice a _placeholder.sst.dev_ behavior in CloudFront. This is not used and is only there because CloudFront requires a default behavior.

#### [Limits](https://sst.dev/docs/component/aws/router#limits)

There are some limits on this setup but it’s managed by SST.

* The CloudFront function can be a maximum of 10KB in size. But because all the route data is stored in the KeyValueStore, the function can be kept small.
* Each value in the KeyValueStore needs to be less than 1KB. This component splits the routes into multiple values to keep it under the limit.
* The KeyValueStore can be a maximum of 5MB. This is fairly large. But to handle sites that have a lot of files, only top-level assets get individual entries.

* * *

## [Constructor](https://sst.dev/docs/component/aws/router#constructor)

```

newRouter(name, args?, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/router#parameters)

* `name` `string`
* `args?` [`RouterArgs`](https://sst.dev/docs/component/aws/router#routerargs)
* `opts?`

## [RouterArgs](https://sst.dev/docs/component/aws/router#routerargs)

### [domain?](https://sst.dev/docs/component/aws/router#domain)

**Type** `Input``<``string`` | ``Object``>`

* [`aliases?`](https://sst.dev/docs/component/aws/router#domain-aliases)
* [`cert?`](https://sst.dev/docs/component/aws/router#domain-cert)
* [`dns?`](https://sst.dev/docs/component/aws/router#domain-dns)
* [`name`](https://sst.dev/docs/component/aws/router#domain-name)
* [`redirects?`](https://sst.dev/docs/component/aws/router#domain-redirects)

Set a custom domain for your Router.
Automatically manages domains hosted on AWS Route 53, Cloudflare, and Vercel. For other providers, you’ll need to pass in a `cert` that validates domain ownership and add the DNS records.
Built-in support for AWS Route 53, Cloudflare, and Vercel. And manual setup for other providers.
By default this assumes the domain is hosted on Route 53.

```

{

domain: "example.com"

}

```

For domains hosted on Cloudflare.

```

{

domain: {

name: "example.com",

dns: sst.cloudflare.dns()

}

}

```

Specify a `www.` version of the custom domain.

```

{

domain: {

name: "domain.com",

redirects: ["www.domain.com"]

}

}

```

#### [domain.aliases?](https://sst.dev/docs/component/aws/router#domain-aliases)

**Type** `Input``<``string``[]``>`
Alias domains that should be used. Unlike the `redirect` option, this keeps your visitors on this alias domain.
So if your users visit `app2.domain.com`, they will stay on `app2.domain.com` in their browser.

```

{

domain: {

name: "app1.domain.com",

aliases: ["app2.domain.com"]

}

}

```

#### [domain.cert?](https://sst.dev/docs/component/aws/router#domain-cert)

**Type** `Input``<``string``>`
The ARN of an ACM (AWS Certificate Manager) certificate that proves ownership of the domain. By default, a certificate is created and validated automatically.
The certificate will be created in the `us-east-1` region as required by AWS CloudFront. If you are creating your own certificate, you must also create it in `us-east-1`.
You need to pass in a `cert` for domains that are not hosted on supported `dns` providers.
To manually set up a domain on an unsupported provider, you’ll need to:

  1. Once validated, set the certificate ARN as the `cert` and set `dns` to `false`.
  2. Add the DNS records in your provider to point to the CloudFront distribution URL.

```

{

domain: {

name: "domain.com",

dns: false,

cert: "arn:aws:acm:us-east-1:112233445566:certificate/3a958790-8878-4cdc-a396-06d95064cf63"

}

}

```

#### [domain.dns?](https://sst.dev/docs/component/aws/router#domain-dns)

**Type** `Input``<``false`` |`[`sst.aws.dns`](https://sst.dev/docs/component/aws/dns/)` | `[`sst.cloudflare.dns`](https://sst.dev/docs/component/cloudflare/dns/)` | `[`sst.vercel.dns`](https://sst.dev/docs/component/vercel/dns/)`>`
**Default** `sst.aws.dns`
The DNS provider to use for the domain. Defaults to the AWS.
Takes an adapter that can create the DNS records on the provider. This can automate validating the domain and setting up the DNS routing.
Supports Route 53, Cloudflare, and Vercel adapters. For other providers, you’ll need to set `dns` to `false` and pass in a certificate validating ownership via `cert`.
Specify the hosted zone ID for the Route 53 domain.

```

{

domain: {

name: "example.com",

dns: sst.aws.dns({

zone: "Z2FDTNDATAQYW2"

})

}

}

```

Use a domain hosted on Cloudflare, needs the Cloudflare provider.

```

{

domain: {

name: "example.com",

dns: sst.cloudflare.dns()

}

}

```

Use a domain hosted on Vercel, needs the Vercel provider.

```

{

domain: {

name: "example.com",

dns: sst.vercel.dns()

}

}

```

#### [domain.name](https://sst.dev/docs/component/aws/router#domain-name)

**Type** `Input``<``string``>`
The custom domain you want to use.

```

{

domain: {

name: "example.com"

}

}

```

Can also include subdomains based on the current stage.

```

{

domain: {

name: `${$app.stage}.example.com`

}

}

```

#### [domain.redirects?](https://sst.dev/docs/component/aws/router#domain-redirects)

**Type** `Input``<``string``[]``>`
Alternate domains to be used. Visitors to the alternate domains will be redirected to the main `name`.
Unlike the `aliases` option, this will redirect visitors back to the main `name`.
Use this to create a `www.` version of your domain and redirect visitors to the apex domain.

```

{

domain: {

name: "domain.com",

redirects: ["www.domain.com"]

}

}

```

### [edge?](https://sst.dev/docs/component/aws/router#edge)

**Type** `Object`

* [`viewerRequest?`](https://sst.dev/docs/component/aws/router#edge-viewerrequest) `Input``<``Object``>`
  * [`injection`](https://sst.dev/docs/component/aws/router#edge-viewerrequest-injection)
  * [`kvStore?`](https://sst.dev/docs/component/aws/router#edge-viewerrequest-kvstore)
* [`viewerResponse?`](https://sst.dev/docs/component/aws/router#edge-viewerresponse) `Input``<``Object``>`
  * [`injection`](https://sst.dev/docs/component/aws/router#edge-viewerresponse-injection)
  * [`kvStore?`](https://sst.dev/docs/component/aws/router#edge-viewerresponse-kvstore)

Configure CloudFront Functions to customize the behavior of HTTP requests and responses at the edge.

#### [edge.viewerRequest?](https://sst.dev/docs/component/aws/router#edge-viewerrequest)

**Type** `Input``<``Object``>`
Configure the viewer request function.
The viewer request function can be used to modify incoming requests before they reach your origin server. For example, you can redirect users, rewrite URLs, or add headers.

##### [edge.viewerRequest.injection](https://sst.dev/docs/component/aws/router#edge-viewerrequest-injection)

**Type** `Input``<``string``>`
The code to inject into the viewer request function.
By default, a viewer request function is created to:

* Disable CloudFront default URL if custom domain is set.
* Add the `x-forwarded-host` header.
* Route requests to the corresponding target based on the domain and request path.

The given code will be injected at the beginning of this function.

```

asyncfunctionhandler(event) {

// User injected code

// Default behavior code

returnevent.request;

}

```

To add a custom header to all requests.

```

{

edge: {

viewerRequest: {

injection: `event.request.headers["x-foo"] = { value: "bar" };`

}

}

}

```

##### [edge.viewerRequest.kvStore?](https://sst.dev/docs/component/aws/router#edge-viewerrequest-kvstore)

**Type** `Input``<``string``>`
The KeyValueStore to associate with the viewer request function.

```

{

edge: {

viewerRequest: {

kvStore: "arn:aws:cloudfront::123456789012:key-value-store/my-store"

}

}

}

```

#### [edge.viewerResponse?](https://sst.dev/docs/component/aws/router#edge-viewerresponse)

**Type** `Input``<``Object``>`
Configure the viewer response function.
The viewer response function can be used to modify outgoing responses before they are sent to the client. For example, you can add security headers or change the response status code.
By default, no viewer response function is set. A new function will be created with the provided code.

##### [edge.viewerResponse.injection](https://sst.dev/docs/component/aws/router#edge-viewerresponse-injection)

**Type** `Input``<``string``>`
The code to inject into the viewer response function.

```

asyncfunctionhandler(event) {

// User injected code

returnevent.response;

}

```

To add a custom header to all responses.

```

{

edge: {

viewerResponse: {

injection: `event.response.headers["x-foo"] = { value: "bar" };`

}

}

}

```

##### [edge.viewerResponse.kvStore?](https://sst.dev/docs/component/aws/router#edge-viewerresponse-kvstore)

**Type** `Input``<``string``>`
The KeyValueStore to associate with the viewer response function.

```

{

edge: {

viewerResponse: {

kvStore: "arn:aws:cloudfront::123456789012:key-value-store/my-store"

}

}

}

```

### [invalidation?](https://sst.dev/docs/component/aws/router#invalidation)

**Type** `Input``<``boolean`` | ``Object``>`

* [`paths?`](https://sst.dev/docs/component/aws/router#invalidation-paths)
* [`token?`](https://sst.dev/docs/component/aws/router#invalidation-token)
* [`wait?`](https://sst.dev/docs/component/aws/router#invalidation-wait)

**Default** Invalidation is turned off
Configure how the CloudFront cache invalidations are handled.
You get 1000 free invalidations per month. After that you pay $0.005 per invalidation path.
Setting this to `true` will invalidate all paths. It’s equivalent to passing in `{ paths: ["/*"] }`.

```

{

invalidation: true

}

```

#### [invalidation.paths?](https://sst.dev/docs/component/aws/router#invalidation-paths)

**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `[”/*”]`
Specify an array of glob pattern of paths to invalidate.
Each glob pattern counts as a single invalidation. Whereas, invalidating `/*` counts as a single invalidation.
Invalidate the `index.html` and all files under the `products/` route.

```

{

invalidation: {

paths: ["/index.html", "/products/*"]

}

}

```

This counts as two invalidations.

#### [invalidation.token?](https://sst.dev/docs/component/aws/router#invalidation-token)

**Type** `Input``<``string``>`
**Default** A unique value is auto-generated on each deploy
A token used to determine if the cache should be invalidated. If the token is the same as the previous deployment, the cache will not be invalidated.
You can set this to a hash that’s computed on every deploy. So if the hash changes, the cache will be invalidated.

```

{

invalidation: {

token: "foo123"

}

}

```

#### [invalidation.wait?](https://sst.dev/docs/component/aws/router#invalidation-wait)

**Type** `Input``<``boolean``>`
**Default** `false`
Configure if `sst deploy` should wait for the CloudFront cache invalidation to finish.
For non-prod environments it might make sense to pass in `false`.
Waiting for this process to finish ensures that new content will be available after the deploy finishes. However, this process can sometimes take more than 5 mins.

```

{

invalidation: {

wait: true

}

}

```

### [transform?](https://sst.dev/docs/component/aws/router#transform)

**Type** `Object`

* [`cachePolicy?`](https://sst.dev/docs/component/aws/router#transform-cachepolicy)
* [`cdn?`](https://sst.dev/docs/component/aws/router#transform-cdn)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.cachePolicy?](https://sst.dev/docs/component/aws/router#transform-cachepolicy)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Cache Policy that’s attached to each CloudFront behavior.

#### [transform.cdn?](https://sst.dev/docs/component/aws/router#transform-cdn)

**Type** [`CdnArgs`](https://sst.dev/docs/component/aws/cdn#cdnargs)` | ``(``args``: `[`CdnArgs`](https://sst.dev/docs/component/aws/cdn#cdnargs)`, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the CloudFront CDN resource.

## [Properties](https://sst.dev/docs/component/aws/router#properties)

### [distributionID](https://sst.dev/docs/component/aws/router#distributionid)

**Type** `Output``<``string``>`
The ID of the Router distribution.

### [nodes](https://sst.dev/docs/component/aws/router#nodes)

**Type** `Object`

* [`cdn`](https://sst.dev/docs/component/aws/router#nodes-cdn)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.cdn](https://sst.dev/docs/component/aws/router#nodes-cdn)

**Type** `Output``<`[`Cdn`](https://sst.dev/docs/component/aws/cdn)`>`
The Amazon CloudFront CDN resource.

### [url](https://sst.dev/docs/component/aws/router#url)

**Type** `Output``<``string``>`
The URL of the Router.
If the `domain` is set, this is the URL with the custom domain. Otherwise, it’s the auto-generated CloudFront URL.

## [SDK](https://sst.dev/docs/component/aws/router#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/router#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `url` `string`
The URL of the Router.
If the `domain` is set, this is the URL with the custom domain. Otherwise, it’s the auto-generated CloudFront URL.

## [Methods](https://sst.dev/docs/component/aws/router#methods)

### [route](https://sst.dev/docs/component/aws/router#route)

```

route(pattern, url, args?)

```

#### [Parameters](https://sst.dev/docs/component/aws/router#parameters-1)

* `pattern` `Input``<``string``>`
The path prefix to match for this route.
* `url` `Input``<``string``>`
The destination URL to route matching requests to.
* `args?` `Input``<`[`RouterUrlRouteArgs`](https://sst.dev/docs/component/aws/router#routerurlrouteargs)`>`
Configure the route.

**Returns** `void`
Add a route to a destination URL.
You can match a route based on:

* A path prefix like `/api`
* A domain pattern like `api.example.com`
* A combined pattern like `dev.example.com/api`

For example, to match a path prefix.
sst.config.ts

```typescript


router.route("/api", "https://api.example.com");


```

Or match a domain.
sst.config.ts

```typescript

router.route("api.myapp.com/", "<https://api.example.com>");

```

Or a combined pattern.
sst.config.ts

```typescript


router.route("dev.myapp.com/api", "https://api.example.com");


```

You can also rewrite the request path.
sst.config.ts

```typescript

router.route("/api", "<https://api.example.com>", {

rewrite: {

regex: "^/api/(.*)$",

to: "/$1"

}

});

```

Here something like `/api/users/profile` will be routed to `https://api.example.com/users/profile`.

### [routeBucket](https://sst.dev/docs/component/aws/router#routebucket)

```

routeBucket(pattern, bucket, args?)

```

#### [Parameters](https://sst.dev/docs/component/aws/router#parameters-2)

* `pattern` `Input``<``string``>`
The path prefix to match for this route.
* `bucket` `Input``<`[`Bucket`](https://sst.dev/docs/component/aws/bucket)`>`
The S3 bucket to route matching requests to.
* `args?` `Input``<`[`RouterBucketRouteArgs`](https://sst.dev/docs/component/aws/router#routerbucketrouteargs)`>`
Configure the route.

**Returns** `void`
Add a route to an S3 bucket.
Let’s say you have an S3 bucket that gives CloudFront `access`.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket", {




"cloudfront"




});


```

You can match a pattern and route to it based on:

* A path prefix like `/api`
* A domain pattern like `api.example.com`
* A combined pattern like `dev.example.com/api`

For example, to match a path prefix.
sst.config.ts

```typescript

router.routeBucket("/files", bucket);

```

Or match a domain.
sst.config.ts

```typescript


router.routeBucket("files.example.com", bucket);


```

Or a combined pattern.
sst.config.ts

```typescript

router.routeBucket("dev.example.com/files", bucket);

```

You can also rewrite the request path.
sst.config.ts

```typescript


router.routeBucket("/files", bucket, {



rewrite: {



regex: "^/files/(.*)$",




to: "/$1"



}


});

```

Here something like `/files/logo.png` will be routed to `/logo.png`.

### [static get](https://sst.dev/docs/component/aws/router#static-get)

```


Router.get(name, distributionID, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/router#parameters-3)

* `name` `string`
The name of the component.
* `distributionID` `Input``<``string``>`
The ID of the existing Router distribution.
* `opts?`

**Returns** [`Router`](https://sst.dev/docs/component/aws/)
Reference an existing Router with the given Router distribution ID.
Let’s say you create a Router in the `dev` stage. And in your personal stage `frank`, you want to share the same Router.
sst.config.ts

```typescript

const router = $app.stage === "frank"

? sst.aws.Router.get("MyRouter", "E2IDLMESRN6V62")

:new sst.aws.Router("MyRouter");

```

Here `E2IDLMESRN6V62` is the ID of the Router distribution created in the `dev` stage. You can find this by outputting the distribution ID in the `dev` stage.
sst.config.ts

```typescript


return {




router: router.distributionID



};

```

Learn more about [how to configure a router for your app](https://sst.dev/docs/configure-a-router).

## [RouterBucketRouteArgs](https://sst.dev/docs/component/aws/router#routerbucketrouteargs)

### [connectionAttempts?](https://sst.dev/docs/component/aws/router#connectionattempts)

**Type** `Input``<``number``>`
**Default** 3
The number of times that CloudFront attempts to connect to the origin. Must be between 1 and 3.

```

{



connectionAttempts: 1



}

```

### [connectionTimeout?](https://sst.dev/docs/component/aws/router#connectiontimeout)

**Type** `Input``<``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“10 seconds”`
The number of seconds that CloudFront waits before timing out and closing the connection to the origin. Must be between 1 and 10 seconds.

```

{



connectionTimeout: "3 seconds"



}

```

### [rewrite?](https://sst.dev/docs/component/aws/router#rewrite)

**Type** `Input``<``Object``>`

* [`regex`](https://sst.dev/docs/component/aws/router#rewrite-regex)
* [`to`](https://sst.dev/docs/component/aws/router#rewrite-to)

Rewrite the request path.
If the route path is `/files/*` and a request comes in for `/files/logo.png`, the request path the destination sees is `/files/logo.png`.
If you want to serve the file from the root of the bucket, you can rewrite the request path to `/logo.png`.

```

{


rewrite: {



regex: "^/files/(.*)$",




to: "/$1"



}


}

```

#### [rewrite.regex](https://sst.dev/docs/component/aws/router#rewrite-regex)

**Type** `Input``<``string``>`
The regex to match the request path.

#### [rewrite.to](https://sst.dev/docs/component/aws/router#rewrite-to)

**Type** `Input``<``string``>`
The replacement for the matched path.

## [RouterUrlRouteArgs](https://sst.dev/docs/component/aws/router#routerurlrouteargs)

### [connectionAttempts?](https://sst.dev/docs/component/aws/router#connectionattempts-1)

**Type** `Input``<``number``>`
**Default** 3
The number of times that CloudFront attempts to connect to the origin. Must be between 1 and 3.

```

{



connectionAttempts: 1



}

```

### [connectionTimeout?](https://sst.dev/docs/component/aws/router#connectiontimeout-1)

**Type** `Input``<``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“10 seconds”`
The number of seconds that CloudFront waits before timing out and closing the connection to the origin. Must be between 1 and 10 seconds.

```

{



connectionTimeout: "3 seconds"



}

```

### [keepAliveTimeout?](https://sst.dev/docs/component/aws/router#keepalivetimeout)

**Type** `Input``<``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“5 seconds”`
The number of seconds that CloudFront should try to maintain the connection to the destination after receiving the last packet of the response. Must be between 1 and 60 seconds

```

{



keepAliveTimeout: "10 seconds"



}

```

### [readTimeout?](https://sst.dev/docs/component/aws/router#readtimeout)

**Type** `Input``<``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“20 seconds”`
The number of seconds that CloudFront waits for a response after routing a request to the destination. Must be between 1 and 60 seconds.
When compared to the `connectionTimeout`, this is the total time for the request.

```

{



readTimeout: "60 seconds"



}

```

### [rewrite?](https://sst.dev/docs/component/aws/router#rewrite-1)

**Type** `Input``<``Object``>`

* [`regex`](https://sst.dev/docs/component/aws/router#rewrite-regex-1)
* [`to`](https://sst.dev/docs/component/aws/router#rewrite-to-1)

Rewrite the request path.
If the route path is `/api/*` and a request comes in for `/api/users/profile`, the request path the destination sees is `/api/users/profile`.
If you want to serve the route from the root, you can rewrite the request path to `/users/profile`.

```

{


rewrite: {



regex: "^/api/(.*)$",




to: "/$1"



}


}

```

#### [rewrite.regex](https://sst.dev/docs/component/aws/router#rewrite-regex-1)

**Type** `Input``<``string``>`
The regex to match the request path.

#### [rewrite.to](https://sst.dev/docs/component/aws/router#rewrite-to-1)

**Type** `Input``<``string``>`
The replacement for the matched path.

[Skip to content](https://sst.dev/docs/component/aws/dns#_top)

# AWS DNS Adapter

The AWS DNS Adapter is used to create DNS records to manage domains hosted on
This adapter is passed in as `domain.dns` when setting a custom domain.

```

{


domain: {



name: "example.com",




dns: sst.aws.dns()



}


}

```

You can also specify a hosted zone ID if you have multiple hosted zones with the same domain.

```

{


domain: {



name: "example.com",




dns: sst.aws.dns({




zone: "Z2FDTNDATAQYW2"



})


}


}

```

* * *

## [Functions](https://sst.dev/docs/component/aws/dns#functions)

### [dns](https://sst.dev/docs/component/aws/dns#dns)

```


dns(args?)


```

#### [Parameters](https://sst.dev/docs/component/aws/dns#parameters)

* `args?` [`DnsArgs`](https://sst.dev/docs/component/aws/dns#dnsargs)

**Returns** `Object`

## [DnsArgs](https://sst.dev/docs/component/aws/dns#dnsargs)

### [override?](https://sst.dev/docs/component/aws/dns#override)

**Type** `Input``<``boolean``>`
**Default** `false`
Set to `true` if you want to let the new DNS records replace the existing ones.
Use this to migrate over your domain without any downtime.
This is useful if your domain is currently used by another app and you want to switch it to your current app. Without setting this, you’ll first have to remove the existing DNS records and then add the new one. This can cause downtime.
You can avoid this by setting this to `true` and the existing DNS records will be replaced without any downtime. Just make sure that when you remove your old app, you don’t remove the DNS records.

```

{



override: true



}

```

### [transform?](https://sst.dev/docs/component/aws/dns#transform)

**Type** `Object`

* [`record?`](https://sst.dev/docs/component/aws/dns#transform-record)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.record?](https://sst.dev/docs/component/aws/dns#transform-record)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the AWS Route 53 record resource.

### [zone?](https://sst.dev/docs/component/aws/dns#zone)

**Type** `Input``<``string``>`
Set the hosted zone ID if you have multiple hosted zones that have the same domain in Route 53.
The 14 letter ID of the `domainName`. You can find the hosted zone ID in the Route 53 part of the AWS Console.

```

{



zone: "Z2FDTNDATAQYW2"



}

```

[Skip to content](https://sst.dev/docs/component/aws/vpc#_top)

# Vpc

The `Vpc` component lets you add a VPC to your app. It uses
This creates a VPC with 2 Availability Zones by default. It also creates the following resources:

  1. A default security group blocking all incoming internet traffic.
  2. A public subnet in each AZ.
  3. A private subnet in each AZ.
  4. An Internet Gateway. All the traffic from the public subnets are routed through it.
  5. If `nat` is enabled, a NAT Gateway or NAT instance in each AZ. All the traffic from the private subnets are routed to the NAT in the same AZ.

By default, this does not create NAT Gateways or NAT instances.

#### [Create a VPC](https://sst.dev/docs/component/aws/vpc#create-a-vpc)

sst.config.ts

```typescript

new sst.aws.Vpc("MyVPC");

```

#### [Create it with 3 Availability Zones](https://sst.dev/docs/component/aws/vpc#create-it-with-3-availability-zones)

sst.config.ts

```typescript


new sst.aws.Vpc("MyVPC", {




az: 3



});

```

#### [Enable NAT](https://sst.dev/docs/component/aws/vpc#enable-nat)

sst.config.ts

```typescript

new sst.aws.Vpc("MyVPC", {

nat: "managed"

});

```

* * *

### [Cost](https://sst.dev/docs/component/aws/vpc#cost)

By default, this component is **free**. Following is the cost to enable the `nat` or `bastion` options.

#### [Managed NAT](https://sst.dev/docs/component/aws/vpc#managed-nat)

If you enable `nat` with the `managed` option, it uses a _NAT Gateway_ per `az` at $0.045 per hour, and $0.045 per GB processed per month.
That works out to a minimum of $0.045 x 2 x 24 x 30 or **$65 per month**. Adjust this for the number of `az` and add $0.045 per GB processed per month.
The above are rough estimates for _us-east-1_ , check out the

#### [EC2 NAT](https://sst.dev/docs/component/aws/vpc#ec2-nat)

If you enable `nat` with the `ec2` option, it uses `t4g.nano` EC2 _On Demand_ instances per `az` at $0.0042 per hour, and $0.09 per GB processed per month for the first 10TB.
That works out to a minimum of $0.0042 x 2 x 24 x 30 or **$6 per month**. Adjust this for the `nat.ec2.instance` you are using and add $0.09 per GB processed per month.
The above are rough estimates for _us-east-1_ , check out the

#### [Bastion](https://sst.dev/docs/component/aws/vpc#bastion)

If you enable `bastion`, it uses a single `t4g.nano` EC2 _On Demand_ instance at $0.0042 per hour, and $0.09 per GB processed per month for the first 10TB.
That works out to $0.0042 x 24 x 30 or **$3 per month**. Add $0.09 per GB processed per month.
However if `nat: "ec2"` is enabled, one of the NAT EC2 instances will be reused; making this **free**.
The above are rough estimates for _us-east-1_ , check out the
* * *

## [Constructor](https://sst.dev/docs/component/aws/vpc#constructor)

```

newVpc(name, args?, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/vpc#parameters)

* `name` `string`
* `args?` [`VpcArgs`](https://sst.dev/docs/component/aws/vpc#vpcargs)
* `opts?`

## [VpcArgs](https://sst.dev/docs/component/aws/vpc#vpcargs)

### [az?](https://sst.dev/docs/component/aws/vpc#az)

**Type** `Input``<``number`` | ``Input``<``string``>``[]``>`
**Default** `2`
Specify the Availability Zones or AZs for the VPC.
You can specify a number of AZs or a list of AZs. If you specify a number, it will look up the availability zones in the region and automatically select that number of AZs. If you specify a list of AZs, it will use that list of AZs.
By default, it creates a VPC with 2 availability zones since services like RDS and Fargate need at least 2 AZs.
Create a VPC with 3 AZs

```

{

az: 3

}

```

Create a VPC with specific AZs

```

{

az: ["us-east-1a", "us-east-1b"]

}

```

### [bastion?](https://sst.dev/docs/component/aws/vpc#bastion-1)

**Type** `Input``<``boolean``>`
**Default** `false`
Configures a bastion host that can be used to connect to resources in the VPC.
When enabled, an EC2 instance of type `t4g.nano` with the bastion AMI will be launched in a public subnet. The instance will have AWS SSM (AWS Session Manager) enabled for secure access without the need for SSH key.
It costs roughly $3 per month to run the `t4g.nano` instance.
If `nat: "ec2"` is enabled, the bastion host will reuse the NAT EC2 instance.
However if `nat: "ec2"` is enabled, the EC2 instance that NAT creates will be used as the bastion host. No additional EC2 instance will be created.
If you are running `sst dev`, a tunnel will be automatically created to the bastion host. This uses a network interface to forward traffic from your local machine to the bastion host.
You can learn more about [`sst tunnel`](https://sst.dev/docs/reference/cli#tunnel).

```

{

bastion: true

}

```

### [nat?](https://sst.dev/docs/component/aws/vpc#nat)

**Type** `Input``<``“``ec2``”`` | ``“``managed``”`` | ``Object``>`

* [`ec2?`](https://sst.dev/docs/component/aws/vpc#nat-ec2) `Input``<``Object``>`
  * [`ami?`](https://sst.dev/docs/component/aws/vpc#nat-ec2-ami)
  * [`instance`](https://sst.dev/docs/component/aws/vpc#nat-ec2-instance)
* [`ip?`](https://sst.dev/docs/component/aws/vpc#nat-ip)
* [`type?`](https://sst.dev/docs/component/aws/vpc#nat-type)

**Default** NAT is disabled
Configures NAT. Enabling NAT allows resources in private subnets to connect to the internet.
There are two NAT options:

  1. `"managed"` creates a
  2. `"ec2"` creates an

For `"managed"`, a NAT Gateway is created in each AZ. All the traffic from the private subnets are routed to the NAT Gateway in the same AZ.
NAT Gateways are billed per hour and per gigabyte of data processed. A NAT Gateway for two AZs costs $65 per month. This is relatively expensive but it automatically scales based on the traffic.
For `"ec2"`, an EC2 instance of type `t4g.nano` will be launched in each AZ with the
The `"ec2"` option uses fck-nat and is 10x cheaper than the `"managed"` NAT Gateway.
NAT EC2 instances are much cheaper than NAT Gateways, the `t4g.nano` instance type is around $3 per month. But you’ll need to scale it up manually if you need more bandwidth.

```

{

nat: "managed"

}

```

#### [nat.ec2?](https://sst.dev/docs/component/aws/vpc#nat-ec2)

**Type** `Input``<``Object``>`
**Default** `{instance: “t4g.nano”}`
Configures the NAT EC2 instance.

```

{

nat: {

ec2: {

instance: "t4g.large"

}

}

}

```

##### [nat.ec2.ami?](https://sst.dev/docs/component/aws/vpc#nat-ec2-ami)

**Type** `Input``<``string``>`
**Default** The latest `fck-nat` AMI
The AMI to use for the NAT.
By default, the latest public

```

{

nat: {

ec2: {

ami: "ami-1234567890abcdef0"

}

}

}

```

##### [nat.ec2.instance](https://sst.dev/docs/component/aws/vpc#nat-ec2-instance)

**Type** `Input``<``string``>`
**Default** `“t4g.nano”`
The type of instance to use for the NAT.

#### [nat.ip?](https://sst.dev/docs/component/aws/vpc#nat-ip)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of Elastic IP allocation IDs to use for the NAT Gateways or NAT instances. The number of allocation IDs must match the number of AZs.
By default, new Elastic IP addresses are created.

```

{

nat: {

ip: ["eipalloc-0123456789abcdef0", "eipalloc-0123456789abcdef1"]

}

}

```

#### [nat.type?](https://sst.dev/docs/component/aws/vpc#nat-type)

**Type** `Input``<``“``ec2``”`` | ``“``managed``”``>`
Configures the type of NAT to create.

* If `nat.ec2` is provided, `nat.type` defaults to `"ec2"`.
* Otherwise, `nat.type` must be explicitly specified.

### [transform?](https://sst.dev/docs/component/aws/vpc#transform)

**Type** `Object`

* [`bastionInstance?`](https://sst.dev/docs/component/aws/vpc#transform-bastioninstance)
* [`bastionSecurityGroup?`](https://sst.dev/docs/component/aws/vpc#transform-bastionsecuritygroup)
* [`elasticIp?`](https://sst.dev/docs/component/aws/vpc#transform-elasticip)
* [`internetGateway?`](https://sst.dev/docs/component/aws/vpc#transform-internetgateway)
* [`natGateway?`](https://sst.dev/docs/component/aws/vpc#transform-natgateway)
* [`natInstance?`](https://sst.dev/docs/component/aws/vpc#transform-natinstance)
* [`natSecurityGroup?`](https://sst.dev/docs/component/aws/vpc#transform-natsecuritygroup)
* [`privateRouteTable?`](https://sst.dev/docs/component/aws/vpc#transform-privateroutetable)
* [`privateSubnet?`](https://sst.dev/docs/component/aws/vpc#transform-privatesubnet)
* [`publicRouteTable?`](https://sst.dev/docs/component/aws/vpc#transform-publicroutetable)
* [`publicSubnet?`](https://sst.dev/docs/component/aws/vpc#transform-publicsubnet)
* [`securityGroup?`](https://sst.dev/docs/component/aws/vpc#transform-securitygroup)
* [`vpc?`](https://sst.dev/docs/component/aws/vpc#transform-vpc)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.bastionInstance?](https://sst.dev/docs/component/aws/vpc#transform-bastioninstance)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 bastion instance resource.

#### [transform.bastionSecurityGroup?](https://sst.dev/docs/component/aws/vpc#transform-bastionsecuritygroup)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 bastion security group resource.

#### [transform.elasticIp?](https://sst.dev/docs/component/aws/vpc#transform-elasticip)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 Elastic IP resource.

#### [transform.internetGateway?](https://sst.dev/docs/component/aws/vpc#transform-internetgateway)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 Internet Gateway resource.

#### [transform.natGateway?](https://sst.dev/docs/component/aws/vpc#transform-natgateway)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 NAT Gateway resource.

#### [transform.natInstance?](https://sst.dev/docs/component/aws/vpc#transform-natinstance)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 NAT instance resource.

#### [transform.natSecurityGroup?](https://sst.dev/docs/component/aws/vpc#transform-natsecuritygroup)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 NAT security group resource.

#### [transform.privateRouteTable?](https://sst.dev/docs/component/aws/vpc#transform-privateroutetable)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 route table resource for the private subnet.

#### [transform.privateSubnet?](https://sst.dev/docs/component/aws/vpc#transform-privatesubnet)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 private subnet resource.

#### [transform.publicRouteTable?](https://sst.dev/docs/component/aws/vpc#transform-publicroutetable)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 route table resource for the public subnet.

#### [transform.publicSubnet?](https://sst.dev/docs/component/aws/vpc#transform-publicsubnet)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 public subnet resource.

#### [transform.securityGroup?](https://sst.dev/docs/component/aws/vpc#transform-securitygroup)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 Security Group resource.

#### [transform.vpc?](https://sst.dev/docs/component/aws/vpc#transform-vpc)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EC2 VPC resource.

## [Properties](https://sst.dev/docs/component/aws/vpc#properties)

### [bastion](https://sst.dev/docs/component/aws/vpc#bastion-2)

**Type** `Output``<``string``>`
The bastion instance ID.

### [id](https://sst.dev/docs/component/aws/vpc#id)

**Type** `Output``<``string``>`
The VPC ID.

### [nodes](https://sst.dev/docs/component/aws/vpc#nodes)

**Type** `Object`

* [`bastionInstance`](https://sst.dev/docs/component/aws/vpc#nodes-bastioninstance)
* [`cloudmapNamespace`](https://sst.dev/docs/component/aws/vpc#nodes-cloudmapnamespace)
* [`elasticIps`](https://sst.dev/docs/component/aws/vpc#nodes-elasticips)
* [`internetGateway`](https://sst.dev/docs/component/aws/vpc#nodes-internetgateway)
* [`natGateways`](https://sst.dev/docs/component/aws/vpc#nodes-natgateways)
* [`natInstances`](https://sst.dev/docs/component/aws/vpc#nodes-natinstances)
* [`privateRouteTables`](https://sst.dev/docs/component/aws/vpc#nodes-privateroutetables)
* [`privateSubnets`](https://sst.dev/docs/component/aws/vpc#nodes-privatesubnets)
* [`publicRouteTables`](https://sst.dev/docs/component/aws/vpc#nodes-publicroutetables)
* [`publicSubnets`](https://sst.dev/docs/component/aws/vpc#nodes-publicsubnets)
* [`securityGroup`](https://sst.dev/docs/component/aws/vpc#nodes-securitygroup)
* [`vpc`](https://sst.dev/docs/component/aws/vpc#nodes-vpc)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.bastionInstance](https://sst.dev/docs/component/aws/vpc#nodes-bastioninstance)

**Type** `Output``<``undefined`` | ``>`
The Amazon EC2 bastion instance.

#### [nodes.cloudmapNamespace](https://sst.dev/docs/component/aws/vpc#nodes-cloudmapnamespace)

**Type**
The AWS Cloudmap namespace.

#### [nodes.elasticIps](https://sst.dev/docs/component/aws/vpc#nodes-elasticips)

**Type** `Output``<``[]``>`
The Amazon EC2 Elastic IP.

#### [nodes.internetGateway](https://sst.dev/docs/component/aws/vpc#nodes-internetgateway)

**Type**
The Amazon EC2 Internet Gateway.

#### [nodes.natGateways](https://sst.dev/docs/component/aws/vpc#nodes-natgateways)

**Type** `Output``<``[]``>`
The Amazon EC2 NAT Gateway.

#### [nodes.natInstances](https://sst.dev/docs/component/aws/vpc#nodes-natinstances)

**Type** `Output``<``[]``>`
The Amazon EC2 NAT instances.

#### [nodes.privateRouteTables](https://sst.dev/docs/component/aws/vpc#nodes-privateroutetables)

**Type** `Output``<``[]``>`
The Amazon EC2 route table for the private subnet.

#### [nodes.privateSubnets](https://sst.dev/docs/component/aws/vpc#nodes-privatesubnets)

**Type** `Output``<``[]``>`
The Amazon EC2 private subnet.

#### [nodes.publicRouteTables](https://sst.dev/docs/component/aws/vpc#nodes-publicroutetables)

**Type** `Output``<``[]``>`
The Amazon EC2 route table for the public subnet.

#### [nodes.publicSubnets](https://sst.dev/docs/component/aws/vpc#nodes-publicsubnets)

**Type** `Output``<``[]``>`
The Amazon EC2 public subnet.

#### [nodes.securityGroup](https://sst.dev/docs/component/aws/vpc#nodes-securitygroup)

**Type**
The Amazon EC2 Security Group.

#### [nodes.vpc](https://sst.dev/docs/component/aws/vpc#nodes-vpc)

**Type**
The Amazon EC2 VPC.

### [privateSubnets](https://sst.dev/docs/component/aws/vpc#privatesubnets)

**Type** `Output``<``Output``<``string``>``[]``>`
A list of private subnet IDs in the VPC.

### [publicSubnets](https://sst.dev/docs/component/aws/vpc#publicsubnets)

**Type** `Output``<``Output``<``string``>``[]``>`
A list of public subnet IDs in the VPC.

### [securityGroups](https://sst.dev/docs/component/aws/vpc#securitygroups)

**Type** `Output``<``Output``<``string``>``[]``>`
A list of VPC security group IDs.

## [SDK](https://sst.dev/docs/component/aws/vpc#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/vpc#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `bastion` `undefined`` | ``string`
The bastion instance ID.

## [Methods](https://sst.dev/docs/component/aws/vpc#methods)

### [static get](https://sst.dev/docs/component/aws/vpc#static-get)

```

Vpc.get(name, vpcId, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/vpc#parameters-1)

* `name` `string`
The name of the component.
* `vpcId` `Input``<``string``>`
The ID of the existing VPC.
* `opts?`

**Returns** [`Vpc`](https://sst.dev/docs/component/aws/)
Reference an existing VPC with the given ID. This is useful when you create a VPC in one stage and want to share it in another stage. It avoids having to create a new VPC in the other stage.
You can use the `static get` method to share VPCs across stages.
Imagine you create a VPC in the `dev` stage. And in your personal stage `frank`, instead of creating a new VPC, you want to share the VPC from `dev`.
sst.config.ts

```typescript


const vpc = $app.stage === "frank"




? sst.aws.Vpc.get("MyVPC", "vpc-0be8fa4de860618bb")




:new sst.aws.Vpc("MyVPC");


```

Here `vpc-0be8fa4de860618bb` is the ID of the VPC created in the `dev` stage. You can find this by outputting the VPC ID in the `dev` stage.
sst.config.ts

```typescript

return {

vpc: vpc.id

};

```

[Skip to content](https://sst.dev/docs/component/cloudflare/dns#_top)

# Cloudflare DNS Adapter

The Cloudflare DNS Adapter is used to create DNS records to manage domains hosted on
You need to [add the Cloudflare provider](https://sst.dev/docs/providers/#install) to use this adapter.
This needs the Cloudflare provider. To add it run:
Terminal window```

sstaddcloudflare

```

This adapter is passed in as `domain.dns` when setting a custom domain, where `example.com` is hosted on Cloudflare.

```

{

domain: {

name: "example.com",

dns: sst.cloudflare.dns()

}

}

```

Specify the zone ID.

```

{

domain: {

name: "example.com",

dns: sst.cloudflare.dns({

zone: "415e6f4653b6d95b775d350f32119abb"

})

}

}

```

* * *

## [Functions](https://sst.dev/docs/component/cloudflare/dns#functions)

### [dns](https://sst.dev/docs/component/cloudflare/dns#dns)

```

dns(args?)

```

#### [Parameters](https://sst.dev/docs/component/cloudflare/dns#parameters)

* `args?` [`DnsArgs`](https://sst.dev/docs/component/cloudflare/dns#dnsargs)

**Returns** `Object`

## [DnsArgs](https://sst.dev/docs/component/cloudflare/dns#dnsargs)

### [proxy?](https://sst.dev/docs/component/cloudflare/dns#proxy)

**Type** `Input``<``boolean``>`
**Default** `false`
Configure ALIAS DNS records as
Proxied records help prevent DDoS attacks and allow you to use Cloudflare’s global content delivery network (CDN) for caching.

```

{

proxy: true

}

```

### [transform?](https://sst.dev/docs/component/cloudflare/dns#transform)

**Type** `Object`

* [`record?`](https://sst.dev/docs/component/cloudflare/dns#transform-record)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.record?](https://sst.dev/docs/component/cloudflare/dns#transform-record)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Cloudflare record resource.

### [zone?](https://sst.dev/docs/component/cloudflare/dns#zone)

**Type** `Input``<``string``>`
The ID of the Cloudflare zone to create the record in.

```

{

zone: "415e6f4653b6d95b775d350f32119abb"

}

```

[Skip to content](https://sst.dev/docs/component/aws/bucket#_top)

# Bucket

The `Bucket` component lets you add an

#### [Minimal example](https://sst.dev/docs/component/aws/bucket#minimal-example)

sst.config.ts
```typescript

const bucket = newsst.aws.Bucket("MyBucket");

```

#### [Public read access](https://sst.dev/docs/component/aws/bucket#public-read-access)

Enable `public` read access for all the files in the bucket. Useful for hosting public files.
sst.config.ts

```typescript


new sst.aws.Bucket("MyBucket", {




access: "public"



});

```

#### [Add a subscriber](https://sst.dev/docs/component/aws/bucket#add-a-subscriber)

sst.config.ts

```typescript

bucket.notify({

notifications: [

{

name: "MySubscriber",

function: "src/subscriber.handler"

}

]

});

```

#### [Link the bucket to a resource](https://sst.dev/docs/component/aws/bucket#link-the-bucket-to-a-resource)

You can link the bucket to other resources, like a function or your Next.js app.
sst.config.ts

```typescript


new sst.aws.Nextjs("MyWeb", {



link: [bucket]


});

```

Once linked, you can generate a pre-signed URL to upload files in your app.
app/page.tsx```

import { Resource } from"sst";

import { getSignedUrl } from"@aws-sdk/s3-request-presigner";

import { S3Client, PutObjectCommand } from"@aws-sdk/client-s3";

const command = newPutObjectCommand({

Key: "file.txt",

Resource.MyBucket.name

});

awaitgetSignedUrl(newS3Client({}), command);

```

* * *
## [Constructor](https://sst.dev/docs/component/aws/bucket#constructor)
```

newBucket(name, args?, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/bucket#parameters)
  * `name` `string`
  * `args?` [`BucketArgs`](https://sst.dev/docs/component/aws/bucket#bucketargs)
  * `opts?`


## [BucketArgs](https://sst.dev/docs/component/aws/bucket#bucketargs)
### [access?](https://sst.dev/docs/component/aws/bucket#access)
**Type** `Input``<``“``public``”`` | ``“``cloudfront``”``>`
Enable public read access for all the files in the bucket. By default, no access is granted.
If you are using the `Router` to serve files from this bucket, you need to allow `cloudfront` access the bucket.
This adds a statement to the bucket policy that either allows `public` access or just `cloudfront` access.
```

{

access: "public"

}

```

### [cors?](https://sst.dev/docs/component/aws/bucket#cors)
**Type** `Input``<``false`` | ``Object``>`
  * [`allowHeaders?`](https://sst.dev/docs/component/aws/bucket#cors-allowheaders)
  * [`allowMethods?`](https://sst.dev/docs/component/aws/bucket#cors-allowmethods)
  * [`allowOrigins?`](https://sst.dev/docs/component/aws/bucket#cors-alloworigins)
  * [`exposeHeaders?`](https://sst.dev/docs/component/aws/bucket#cors-exposeheaders)
  * [`maxAge?`](https://sst.dev/docs/component/aws/bucket#cors-maxage)


**Default** `true`
The CORS configuration for the bucket. Defaults to `true`, which is the same as:
```

{

cors: {

allowHeaders: ["*"],

allowOrigins: ["*"],

allowMethods: ["DELETE", "GET", "HEAD", "POST", "PUT"],

exposeHeaders: [],

maxAge: "0 seconds"

}

}

```

####  [cors.allowHeaders?](https://sst.dev/docs/component/aws/bucket#cors-allowheaders)
**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `[”*”]`
The HTTP headers that origins can include in requests to the bucket.
```

{

cors: {

allowHeaders: ["date", "keep-alive", "x-custom-header"]

}

}

```

####  [cors.allowMethods?](https://sst.dev/docs/component/aws/bucket#cors-allowmethods)
**Type** `Input``<``Input``<``“``GET``”`` | ``“``POST``”`` | ``“``PUT``”`` | ``“``DELETE``”`` | ``“``HEAD``”``>``[]``>`
**Default** `[“DELETE” | “GET” | “HEAD” | “POST” | “PUT”]`
The HTTP methods that are allowed when calling the bucket.
```

{

cors: {

allowMethods: ["GET", "POST", "DELETE"]

}

}

```

####  [cors.allowOrigins?](https://sst.dev/docs/component/aws/bucket#cors-alloworigins)
**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `[”*”]`
The origins that can access the bucket.
```

{

cors: {

allowOrigins: ["https://www.example.com", "http://localhost:60905"]

}

}

```

Or the wildcard for all origins.
```

{

cors: {

allowOrigins: ["*"]

}

}

```

####  [cors.exposeHeaders?](https://sst.dev/docs/component/aws/bucket#cors-exposeheaders)
**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `[]`
The HTTP headers you want to expose to an origin that calls the bucket.
```

{

cors: {

exposeHeaders: ["date", "keep-alive", "x-custom-header"]

}

}

```

####  [cors.maxAge?](https://sst.dev/docs/component/aws/bucket#cors-maxage)
**Type** `Input``<``“``${number} minute``”`` | ``“``${number} minutes``”`` | ``“``${number} hour``”`` | ``“``${number} hours``”`` | ``“``${number} second``”`` | ``“``${number} seconds``”`` | ``“``${number} day``”`` | ``“``${number} days``”``>`
**Default** `“0 seconds”`
The maximum amount of time the browser can cache results of a preflight request. By default the browser doesn’t cache the results. The maximum value is `86400 seconds` or `1 day`.
```

{

cors: {

maxAge: "1 day"

}

}

```

### [enforceHttps?](https://sst.dev/docs/component/aws/bucket#enforcehttps)
**Type** `Input``<``boolean``>`
**Default** true
Enforce HTTPS for all requests to the bucket.
By default, the bucket policy will automatically block any HTTP requests. This is done using the `aws:SecureTransport` condition key.
```

{

enforceHttps: false

}

```

### [policy?](https://sst.dev/docs/component/aws/bucket#policy)
**Type** `Input``<``Input``<``Object``>``[]``>`
  * [`actions`](https://sst.dev/docs/component/aws/bucket#policy-actions)
  * [`conditions?`](https://sst.dev/docs/component/aws/bucket#policy-conditions) `Input``<``Input``<``Object``>``[]``>`
    * [`test`](https://sst.dev/docs/component/aws/bucket#policy-conditions-test)
    * [`values`](https://sst.dev/docs/component/aws/bucket#policy-conditions-values)
    * [`variable`](https://sst.dev/docs/component/aws/bucket#policy-conditions-variable)
  * [`effect?`](https://sst.dev/docs/component/aws/bucket#policy-effect)
  * [`paths?`](https://sst.dev/docs/component/aws/bucket#policy-paths)
  * [`principals`](https://sst.dev/docs/component/aws/bucket#policy-principals) `Input``<``“``*``”`` | ``Input``<``Object``>``[]``>`
    * [`identifiers`](https://sst.dev/docs/component/aws/bucket#policy-principals-identifiers)
    * [`type`](https://sst.dev/docs/component/aws/bucket#policy-principals-type)


Configure the policy for the bucket.
Restrict Access to Specific IP Addresses
```

{

policy: [{

actions: ["s3:*"],

principals: "*",

conditions: [

{

test: "IpAddress",

variable: "aws:SourceIp",

values: ["10.0.0.0/16"]

}

]

}]

}

```

Allow Specific IAM User Access
```

{

policy: [{

actions: ["s3:*"],

principals: [{

type: "aws",

identifiers: ["arn:aws:iam::123456789012:user/specific-user"]

}],

}]

}

```

Cross-Account Access
```

{

policy: [{

actions: ["s3:GetObject", "s3:ListBucket"],

principals: [{

type: "aws",

identifiers: ["123456789012"]

}],

}]

}

```

####  [policy[].actions](https://sst.dev/docs/component/aws/bucket#policy-actions)
**Type** `Input``<``Input``<``string``>``[]``>`
The 
```

{

actions: ["s3:*"]

}

```

####  [policy[].conditions?](https://sst.dev/docs/component/aws/bucket#policy-conditions)
**Type** `Input``<``Input``<``Object``>``[]``>`
Configure specific conditions for when the policy is in effect.
```

{

conditions: [

{

test: "StringEquals",

variable: "s3:x-amz-server-side-encryption",

values: ["AES256"]

}

]

}

```

#####  [policy[].conditions[].test](https://sst.dev/docs/component/aws/bucket#policy-conditions-test)
**Type** `Input``<``string``>`
Name of the 
#####  [policy[].conditions[].values](https://sst.dev/docs/component/aws/bucket#policy-conditions-values)
**Type** `Input``<``Input``<``string``>``[]``>`
The values to evaluate the condition against. If multiple values are provided, the condition matches if at least one of them applies. That is, AWS evaluates multiple values as though using an “OR” boolean operation.
#####  [policy[].conditions[].variable](https://sst.dev/docs/component/aws/bucket#policy-conditions-variable)
**Type** `Input``<``string``>`
Name of a `aws:` or service-specific variables prefixed with the service name.
####  [policy[].effect?](https://sst.dev/docs/component/aws/bucket#policy-effect)
**Type** `Input``<``“``allow``”`` | ``“``deny``”``>`
**Default** `“allow”`
Configures whether the permission is allowed or denied.
```

{

effect: "deny"

}

```

####  [policy[].paths?](https://sst.dev/docs/component/aws/bucket#policy-paths)
**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `["", ”*”]`
The S3 file paths that the policy is applied to. The paths are specified using the 
Apply the policy to the bucket itself.
```

{

paths: [""]

}

```

Apply to all files in the bucket.
```

{

paths: ["*"]

}

```

Apply to all files in the `images/` folder.
```

{

paths: ["images/*"]

}

```

####  [policy[].principals](https://sst.dev/docs/component/aws/bucket#policy-principals)
**Type** `Input``<``“``*``”`` | ``Input``<``Object``>``[]``>`
The principals that can perform the actions.
Allow anyone to perform the actions.
```

{

principals: "*"

}

```

Allow anyone within an AWS account.
```

{

principals: [{ type: "aws", identifiers: ["123456789012"] }]

}

```

Allow specific IAM roles.
```

{

principals: [{

type: "aws",

identifiers: [

"arn:aws:iam::123456789012:role/MyRole",

"arn:aws:iam::123456789012:role/MyOtherRole"

]

}]

}

```

Allow AWS CloudFront.
```

{

principals: [{ type: "service", identifiers: ["cloudfront.amazonaws.com"] }]

}

```

Allow OIDC federated users.
```

{

principals: [{

type: "federated",

identifiers: ["accounts.google.com"]

}]

}

```

Allow SAML federated users.
```

{

principals: [{

type: "federated",

identifiers: ["arn:aws:iam::123456789012:saml-provider/provider-name"]

}]

}

```

Allow Canonical User IDs.
```

{

principals: [{

type: "canonical",

identifiers: ["79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be"]

}]

}

```

Allow specific IAM users.
#####  [policy[].principals[].identifiers](https://sst.dev/docs/component/aws/bucket#policy-principals-identifiers)
**Type** `Input``<``Input``<``string``>``[]``>`
#####  [policy[].principals[].type](https://sst.dev/docs/component/aws/bucket#policy-principals-type)
**Type** `Input``<``“``aws``”`` | ``“``service``”`` | ``“``federated``”`` | ``“``canonical``”``>`
### [transform?](https://sst.dev/docs/component/aws/bucket#transform)
**Type** `Object`
  * [`bucket?`](https://sst.dev/docs/component/aws/bucket#transform-bucket)
  * [`cors?`](https://sst.dev/docs/component/aws/bucket#transform-cors)
  * [`policy?`](https://sst.dev/docs/component/aws/bucket#transform-policy)
  * [`publicAccessBlock?`](https://sst.dev/docs/component/aws/bucket#transform-publicaccessblock)
  * [`versioning?`](https://sst.dev/docs/component/aws/bucket#transform-versioning)


[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.
####  [transform.bucket?](https://sst.dev/docs/component/aws/bucket#transform-bucket)
**Type** ` | ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the S3 Bucket resource.
####  [transform.cors?](https://sst.dev/docs/component/aws/bucket#transform-cors)
**Type** ` | ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the S3 Bucket CORS configuration resource.
####  [transform.policy?](https://sst.dev/docs/component/aws/bucket#transform-policy)
**Type** ` | ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the S3 Bucket Policy resource.
####  [transform.publicAccessBlock?](https://sst.dev/docs/component/aws/bucket#transform-publicaccessblock)
**Type** `false`` | `` | ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the public access block resource that’s attached to the Bucket.
Returns `false` if the public access block resource should not be created.
####  [transform.versioning?](https://sst.dev/docs/component/aws/bucket#transform-versioning)
**Type** ` | ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the S3 Bucket versioning resource.
### [versioning?](https://sst.dev/docs/component/aws/bucket#versioning)
**Type** `Input``<``boolean``>`
**Default** `false`
Enable versioning for the bucket.
Bucket versioning enables you to store multiple versions of an object, protecting against accidental deletion or overwriting.
```

{

versioning: true

}

```

## [Properties](https://sst.dev/docs/component/aws/bucket#properties)
### [arn](https://sst.dev/docs/component/aws/bucket#arn)
**Type** `Output``<``string``>`
The ARN of the S3 Bucket.
### [domain](https://sst.dev/docs/component/aws/bucket#domain)
**Type** `Output``<``string``>`
The domain name of the bucket. Has the format `${bucketName}.s3.amazonaws.com`.
### [name](https://sst.dev/docs/component/aws/bucket#name)
**Type** `Output``<``string``>`
The generated name of the S3 Bucket.
### [nodes](https://sst.dev/docs/component/aws/bucket#nodes)
**Type** `Object`
  * [`bucket`](https://sst.dev/docs/component/aws/bucket#nodes-bucket)


The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.
####  [nodes.bucket](https://sst.dev/docs/component/aws/bucket#nodes-bucket)
**Type** `Output``<``>`
The Amazon S3 bucket.
## [SDK](https://sst.dev/docs/component/aws/bucket#sdk)
Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *
### [Links](https://sst.dev/docs/component/aws/bucket#links)
This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).
  * `name` `string`
The generated name of the S3 Bucket.


## [Methods](https://sst.dev/docs/component/aws/bucket#methods)
### [notify](https://sst.dev/docs/component/aws/bucket#notify)
```

notify(args)

```

#### [Parameters](https://sst.dev/docs/component/aws/bucket#parameters-1)
  * `args` [`BucketNotificationsArgs`](https://sst.dev/docs/component/aws/bucket#bucketnotificationsargs)
The config for the event notifications.


**Returns** [`BucketNotification`](https://sst.dev/docs/component/aws/bucket-notification)
Subscribe to event notifications from this bucket. You can subscribe to these notifications with a function, a queue, or a topic.
For exmaple, to notify a function:
sst.config.ts
```typescript


bucket.notify({



notifications: [


{



name: "MySubscriber",




function: "src/subscriber.handler"



}


]


});

```

Or let’s say you have a queue.
sst.config.ts

```typescript

const myQueue = newsst.aws.Queue("MyQueue");

```

You can notify it by passing in the queue.
sst.config.ts

```typescript


bucket.notify({



notifications: [


{



name: "MySubscriber",




queue: myQueue



}


]


});

```

Or let’s say you have a topic.
sst.config.ts

```typescript

const myTopic = newsst.aws.SnsTopic("MyTopic");

```

You can notify it by passing in the topic.
sst.config.ts

```typescript


bucket.notify({



notifications: [


{



name: "MySubscriber",




topic: myTopic



}


]


});

```

You can also set it to only send notifications for specific S3 events.

```


bucket.notify({



notifications: [


{



name: "MySubscriber",




function: "src/subscriber.handler",




events: ["s3:ObjectCreated:*", "s3:ObjectRemoved:*"]



}


]


});

```

And you can add filters to be only notified from specific files in the bucket.

```


bucket.notify({



notifications: [


{



name: "MySubscriber",




function: "src/subscriber.handler",




filterPrefix: "images/"



}


]


});

```

### [static get](https://sst.dev/docs/component/aws/bucket#static-get)

```


Bucket.get(name, bucketName, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/bucket#parameters-2)

* `name` `string`
The name of the component.
* `bucketName` `string`
The name of the existing S3 Bucket.
* `opts?`

**Returns** [`Bucket`](https://sst.dev/docs/component/aws/)
Reference an existing bucket with the given bucket name. This is useful when you create a bucket in one stage and want to share it in another stage. It avoids having to create a new bucket in the other stage.
You can use the `static get` method to share buckets across stages.
Imagine you create a bucket in the `dev` stage. And in your personal stage `frank`, instead of creating a new bucket, you want to share the bucket from `dev`.
sst.config.ts

```typescript

const bucket = $app.stage === "frank"

? sst.aws.Bucket.get("MyBucket", "app-dev-mybucket-12345678")

:new sst.aws.Bucket("MyBucket");

```

Here `app-dev-mybucket-12345678` is the auto-generated bucket name for the bucket created in the `dev` stage. You can find this by outputting the bucket name in the `dev` stage.
sst.config.ts

```typescript


return {




bucket: bucket.name



};

```

## [BucketNotificationsArgs](https://sst.dev/docs/component/aws/bucket#bucketnotificationsargs)

### [notifications](https://sst.dev/docs/component/aws/bucket#notifications)

**Type** `Input``<``Input``<``Object``>``[]``>`

* [`events?`](https://sst.dev/docs/component/aws/bucket#notifications-events)
* [`filterPrefix?`](https://sst.dev/docs/component/aws/bucket#notifications-filterprefix)
* [`filterSuffix?`](https://sst.dev/docs/component/aws/bucket#notifications-filtersuffix)
* [`function?`](https://sst.dev/docs/component/aws/bucket#notifications-function)
* [`name`](https://sst.dev/docs/component/aws/bucket#notifications-name)
* [`queue?`](https://sst.dev/docs/component/aws/bucket#notifications-queue)
* [`topic?`](https://sst.dev/docs/component/aws/bucket#notifications-topic)

A list of subscribers that’ll be notified when events happen in the bucket.

#### [notifications[].events?](https://sst.dev/docs/component/aws/bucket#notifications-events)

**Type** `Input``<``Input``<``“``s3:ObjectCreated:*``”`` | ``“``s3:ObjectCreated:Put``”`` | ``“``s3:ObjectCreated:Post``”`` | ``“``s3:ObjectCreated:Copy``”`` | ``“``s3:ObjectCreated:CompleteMultipartUpload``”`` | ``“``s3:ObjectRemoved:*``”`` | ``“``s3:ObjectRemoved:Delete``”`` | ``“``s3:ObjectRemoved:DeleteMarkerCreated``”`` | ``“``s3:ObjectRestore:*``”`` | ``“``s3:ObjectRestore:Post``”`` | ``“``s3:ObjectRestore:Completed``”`` | ``“``s3:ObjectRestore:Delete``”`` | ``“``s3:ReducedRedundancyLostObject``”`` | ``“``s3:Replication:*``”`` | ``“``s3:Replication:OperationFailedReplication``”`` | ``“``s3:Replication:OperationMissedThreshold``”`` | ``“``s3:Replication:OperationReplicatedAfterThreshold``”`` | ``“``s3:Replication:OperationNotTracked``”`` | ``“``s3:LifecycleExpiration:*``”`` | ``“``s3:LifecycleExpiration:Delete``”`` | ``“``s3:LifecycleExpiration:DeleteMarkerCreated``”`` | ``“``s3:LifecycleTransition``”`` | ``“``s3:IntelligentTiering``”`` | ``“``s3:ObjectTagging:*``”`` | ``“``s3:ObjectTagging:Put``”`` | ``“``s3:ObjectTagging:Delete``”`` | ``“``s3:ObjectAcl:Put``”``>``[]``>`
**Default** All S3 events
A list of S3 event types that’ll trigger a notification.

```

{



events: ["s3:ObjectCreated:*", "s3:ObjectRemoved:*"]



}

```

#### [notifications[].filterPrefix?](https://sst.dev/docs/component/aws/bucket#notifications-filterprefix)

**Type** `Input``<``string``>`
An S3 object key prefix that will trigger a notification.
To be notified for all the objects in the `images/` folder.

```

{



filterPrefix: "images/"



}

```

#### [notifications[].filterSuffix?](https://sst.dev/docs/component/aws/bucket#notifications-filtersuffix)

**Type** `Input``<``string``>`
An S3 object key suffix that will trigger the notification.
To be notified for all the objects with the `.jpg` suffix.

```

{



filterSuffix: ".jpg"



}

```

#### [notifications[].function?](https://sst.dev/docs/component/aws/bucket#notifications-function)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
The function that’ll be notified.

```

{



name: "MySubscriber",




function: "src/subscriber.handler"



}

```

Customize the subscriber function. The `link` ensures the subscriber can access the bucket through the [SDK](https://sst.dev/docs/reference/sdk/).

```

{



name: "MySubscriber",




function: {




handler: "src/subscriber.handler",




timeout: "60 seconds",




link: [bucket]



}


}

```

Or pass in the ARN of an existing Lambda function.

```

{



name: "MySubscriber",




function: "arn:aws:lambda:us-east-1:123456789012:function:my-function"



}

```

#### [notifications[].name](https://sst.dev/docs/component/aws/bucket#notifications-name)

**Type** `Input``<``string``>`
The name of the subscriber.

#### [notifications[].queue?](https://sst.dev/docs/component/aws/bucket#notifications-queue)

**Type** `Input``<``string`` |`[`Queue`](https://sst.dev/docs/component/aws/queue)`>`
The Queue that’ll be notified.
For example, let’s say you have a queue.
sst.config.ts

```typescript

const myQueue = newsst.aws.Queue("MyQueue");

```

You can subscribe to this bucket with it.

```

{

name: "MySubscriber",

queue: myQueue

}

```

Or pass in the ARN of an existing SQS queue.

```

{

name: "MySubscriber",

queue: "arn:aws:sqs:us-east-1:123456789012:my-queue"

}

```

#### [notifications[].topic?](https://sst.dev/docs/component/aws/bucket#notifications-topic)

**Type** `Input``<``string`` |`[`SnsTopic`](https://sst.dev/docs/component/aws/sns-topic)`>`
The SNS topic that’ll be notified.
For example, let’s say you have a topic.
sst.config.ts

```typescript


const myTopic = newsst.aws.SnsTopic("MyTopic");


```

You can subscribe to this bucket with it.

```

{



name: "MySubscriber",




topic: myTopic



}

```

Or pass in the ARN of an existing SNS topic.

```

{



name: "MySubscriber",




topic: "arn:aws:sns:us-east-1:123456789012:my-topic"



}

```

### [transform?](https://sst.dev/docs/component/aws/bucket#transform-1)

**Type** `Object`

* [`notification?`](https://sst.dev/docs/component/aws/bucket#transform-notification)

[Transform](https://sst.dev/docs/components#transform) how this notification creates its underlying resources.

#### [transform.notification?](https://sst.dev/docs/component/aws/bucket#transform-notification)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the S3 Bucket Notification resource.

[Skip to content](https://sst.dev/docs/iam-credentials#_top)

# IAM Credentials

SST deploys your AWS resources using your AWS credentials. In this guide we’ll look at how to set these credentials, the basic set of permissions it needs, and how to customize it.
* * *

## [Credentials](https://sst.dev/docs/iam-credentials#credentials)

There are a couple of different ways to set the credentials that your app will use. The simplest is using a credentials file.
However, if you’re still figuring out how to configure your AWS account, we recommend [following our guide on it](https://sst.dev/docs/aws-accounts).
* * *

#### [From a file](https://sst.dev/docs/iam-credentials#from-a-file)

By default, your AWS credentials are in a file:

* `~/.aws/credentials` on Linux, Unix, macOS
* `C:\Users\USER_NAME\.aws\credentials` on Windows

If the credentials file does not exist on your machine.

  1. Follow this to [create an IAM user](https://sst.dev/chapters/create-an-iam-user.html)
  2. And then use this to [configure the credentials](https://sst.dev/chapters/configure-the-aws-cli.html)

Below we’ll look at how to customize the permissions that are granted to this user.
* * *
Your credentials file might look like:
~/.aws/credentials```

[default]

aws_access_key_id=<YOUR_ACCESS_KEY_ID>

aws_secret_access_key=<YOUR_SECRET_ACCESS_KEY>

```

Where `default` is the name of the credentials profile.
And if you have multiple credentials, it might look like:
~/.aws/credentials```

[default]



aws_access_key_id=<DEFAULT_ACCESS_KEY_ID>




aws_secret_access_key=<DEFAULT_SECRET_ACCESS_KEY>



[staging]



aws_access_key_id=<STAGING_ACCESS_KEY_ID>




aws_secret_access_key=<STAGING_SECRET_ACCESS_KEY>



[production]



aws_access_key_id=<PRODUCTION_ACCESS_KEY_ID>




aws_secret_access_key=<PRODUCTION_SECRET_ACCESS_KEY>


```

By default, SST uses the credentials for the `default` profile. To use one of the other profiles, set the `profile` in your `sst.config.ts`.
sst.config.ts

```typescript

{

providers: {

aws: {

profile: "staging"

}

}

}

```

You can customize this for the stage your app is being deployed to.
sst.config.ts

```typescript


app(input) {




return {



// ...


providers: {


aws: {



profile: input?.stage==="staging"?"staging":"default"



}


}


};


},

```

If you’ve configured AWS credentials previously through the `AWS_PROFILE` environment variable or through a `.env` file, it will override the profile set in your `sst.config.ts`. So make sure to remove any references to `AWS_PROFILE`.
* * *

#### [From environment variables](https://sst.dev/docs/iam-credentials#from-environment-variables)

SST can also detect AWS credentials in your environment and use them to deploy.

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`

If you are using temporary credentials, you can also set the `AWS_SESSION_TOKEN`.
This is useful when you are deploying through a CI environment and there are no credential files around.
* * *

### [Precedence](https://sst.dev/docs/iam-credentials#precedence)

If you have AWS credentials set in multiple places, SST will first look at:

  1. Environment variables
This includes `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or `AWS_SESSION_TOKEN`, and `AWS_PROFILE`. This also includes environment variables set in a `.env` file.
  2. SST config
Then it’ll check for the credentials or `profile` in your `sst.config.ts`.
  3. AWS config
It’ll then check for the `[default]` profile in your `~/.aws/config` or `C:\Users\USER_NAME\.aws\config`.
  4. Credential files
Finally, it’ll look for any static credentials in your `~/.aws/credentials` or `C:\Users\USER_NAME\.aws\credentials`.

* * *

## [IAM permissions](https://sst.dev/docs/iam-credentials#iam-permissions)

The credentials above are for an IAM user and it comes with an IAM policy. This defines what resources the given user has access to. By default, we are using `AdministratorAccess`. This gives your user complete access.
However, if you are using SST at your company, you want to secure these permissions. Here we’ll look at exactly what SST needs and how you can go about customizing it.
* * *
Let’s start with an IAM policy you can _copy and paste_.
**Copy IAM Policy**
iam-policy.json```

{

"Version": "2012-10-17",

"Statement": [

{

"Sid": "ManageBootstrapStateBucket",

"Effect": "Allow",

"Action": [

"s3:CreateBucket",

"s3:PutBucketVersioning",

"s3:PutBucketNotification",

"s3:PutBucketPolicy",

"s3:DeleteObject",

"s3:GetObject",

"s3:ListBucket",

"s3:PutObject"

],

"Resource": [

"arn:aws:s3:::sst-state-*"

]

},

{

"Sid": "ManageBootstrapAssetBucket",

"Effect": "Allow",

"Action": [

"s3:CreateBucket",

"s3:PutBucketVersioning",

"s3:PutBucketNotification",

"s3:PutBucketPolicy",

"s3:DeleteObject",

"s3:GetObject",

"s3:ListBucket",

"s3:PutObject"

],

"Resource": [

"arn:aws:s3:::sst-asset-*"

]

},

{

"Sid": "ManageBootstrapECRRepo",

"Effect": "Allow",

"Action": [

"ecr:CreateRepository",

"ecr:DescribeRepositories"

],

"Resource": [

"arn:aws:ecr:REGION:ACCOUNT:repository/sst-asset"

]

},

{

"Sid": "ManageBootstrapSSMParameter",

"Effect": "Allow",

"Action": [

"ssm:GetParameters",

"ssm:PutParameter"

],

"Resource": [

"arn:aws:ssm:REGION:ACCOUNT:parameter/sst/passphrase/*",

"arn:aws:ssm:REGION:ACCOUNT:parameter/sst/bootstrap"

]

},

{

"Sid": "Deployments",

"Effect": "Allow",

"Action": [

"*"

],

"Resource": [

"*"

]

},

{

"Sid": "ManageSecrets",

"Effect": "Allow",

"Action": [

"ssm:DeleteParameter",

"ssm:GetParameter",

"ssm:GetParameters",

"ssm:GetParametersByPath",

"ssm:PutParameter"

],

"Resource": [

"arn:aws:ssm:REGION:ACCOUNT:parameter/sst/*"

]

},

{

"Sid": "LiveLambdaSocketConnection",

"Effect": "Allow",

"Action": [

"appsync:EventSubscribe",

"appsync:EventPublish",

"appsync:EventConnect"

],

"Resource": [

"*"

]

}

]

}

```

This list roughly breaks down into the following:
  1. Permissions needed to bootstrap SST in your AWS account
  2. Permissions needed to deploy your app
  3. Permissions needed by the CLI


Let’s look at them in detail.
* * *
### [Bootstrap](https://sst.dev/docs/iam-credentials#bootstrap)
SST needs to [bootstrap](https://sst.dev/docs/state/#bootstrap) each AWS account, in each region, once. This happens automatically when you run `sst deploy` or `sst dev`.
There are a couple of different things being bootstrapped and these are the permissions they need:
  * Permissions to create the bootstrap bucket for storing state.
```

{

"Sid": "ManageBootstrapStateBucket",

"Effect": "Allow",

"Action": [

"s3:CreateBucket",

"s3:PutBucketVersioning",

"s3:PutBucketNotification",

"s3:DeleteObject",

"s3:GetObject",

"s3:ListBucket",

"s3:PutObject"

],

"Resource": [

"arn:aws:s3:::sst-state-*"

]

}

```

  * Permissions to create the bootstrap bucket for storing the assets in your app. These include the Lambda function bundles and static assets in your frontends.
```

{

"Sid": "ManageBootstrapAssetBucket",

"Effect": "Allow",

"Action": [

"s3:CreateBucket",

"s3:PutBucketVersioning",

"s3:DeleteObject",

"s3:GetObject",

"s3:ListBucket",

"s3:PutObject"

],

"Resource": [

"arn:aws:s3:::sst-asset-*"

]

}

```

  * Permissions to create the bootstrap ECR repository for hosting the Docker images in your app.
```

{

"Sid": "ManageBootstrapECRRepo",

"Effect": "Allow",

"Action": [

"ecr:CreateRepository",

"ecr:DescribeRepositories"

],

"Resource": [

"arn:aws:ecr:REGION:ACCOUNT:repository/sst-asset"

]

}

```

  * Permissions to create the bootstrap SSM parameter. This parameter stores information about the deployed bootstrap resources.
```

{

"Sid": "ManageBootstrapSSMParameter",

"Effect": "Allow",

"Action": [

"ssm:GetParameters",

"ssm:PutParameter"

],

"Resource": [

"arn:aws:ssm:REGION:ACCOUNT:parameter/sst/passphrase/*",

"arn:aws:ssm:REGION:ACCOUNT:parameter/sst/bootstrap"

]

}

```



* * *
### [Deploy](https://sst.dev/docs/iam-credentials#deploy)
The permissions that SST needs to deploy the resources in your app, depends on what you have in your app.
The following block is placed as a template in the IAM policy above for you to customize.
```

{

"Sid": "Deployments",

"Effect": "Allow",

"Action": [

"*"

],

"Resource": [

"*"

]

}

```

Below we’ll look at how you can try customizing this.
* * *
### [CLI](https://sst.dev/docs/iam-credentials#cli)
The SST CLI also makes some AWS SDK calls to your account. Here are the IAM permissions it needs.
  * Permissions to manage your [secrets](https://sst.dev/docs/component/secret).
```

{

"Sid": "ManageSecrets",

"Effect": "Allow",

"Action": [

"ssm:DeleteParameter",

"ssm:GetParameter",

"ssm:GetParameters",

"ssm:GetParametersByPath",

"ssm:PutParameter"

],

"Resource": [

"arn:aws:ssm:us-east-1:112233445566:parameter/sst/*"

]

}

```

  * And permissions to connect to the IoT endpoint in `sst dev` to run your functions [_Live_](https://sst.dev/docs/live).
```

{

"Sid": "LiveLambdaSocketConnection",

"Effect": "Allow",

"Action": [

"iot:DescribeEndpoint",

"iot:Connect",

"iot:Subscribe",

"iot:Publish",

"iot:Receive"

],

"Resource": [

"*"

]

}

```



* * *
## [Minimize permissions](https://sst.dev/docs/iam-credentials#minimize-permissions)
Editing the above policy based on the resources you are adding to your app can be tedious. Here’s an approach to consider.
  * Sandbox accounts
Start by creating separate AWS accounts for your teammates for their dev usage. In these sandbox accounts, you can grant `AdministratorAccess`. This avoids having to modify their permissions every time they make some changes.
  * IAM Access Analyzer
For your staging accounts, you can start by granting a broad permissions policy. Then after deploying your app and allowing it to run for a period of time. You can use your CloudTrail events to identify the actions and services used by that IAM user. The 
You can now use this for your production accounts. Learn more about how to use the 


In general, you want to make sure you audit the IAM permissions you are granting on a regular basis.


[Skip to content](https://sst.dev/docs/reference/global#_top)
# Global
The Global library is a collection of `$` functions and variables that are available in the `run` function, of your [`sst.config.ts`](https://sst.dev/docs/reference/config/).
You don’t need to import the Global library. It’s available in the `run` function of your `sst.config.ts`.
The Global library is only available in the `run` function of your `sst.config.ts`.
For example, you can get the name of your app in your app config using `$app.name`.
sst.config.ts
```typescript


exportdefault$config({



// ...



asyncrun() {




console.log($app.name);



}


});

```

The **variables** contain the context of the app that’s being run. While the **functions** help you work with the [Outputs of components](https://sst.dev/docs/components##inputs--outputs).
* * *

## [Variables](https://sst.dev/docs/reference/global#variables)

### [$app](https://sst.dev/docs/reference/global#app)

**Type** `Object`

* [`name`](https://sst.dev/docs/reference/global#app-name)
* [`protect`](https://sst.dev/docs/reference/global#app-protect)
* [`providers`](https://sst.dev/docs/reference/global#app-providers)
* [`removal`](https://sst.dev/docs/reference/global#app-removal)
* [`stage`](https://sst.dev/docs/reference/global#app-stage)

Context about the app being run.

#### [$app.name](https://sst.dev/docs/reference/global#app-name)

**Type** `string`
The name of the current app.

#### [$app.protect](https://sst.dev/docs/reference/global#app-protect)

**Type** `boolean`
If true, prevents `sst remove` from being executed on this stage

#### [$app.providers](https://sst.dev/docs/reference/global#app-providers)

**Type** `undefined`` | ``Record``<``string`, `any``>`
The providers currently being used in the app.

#### [$app.removal](https://sst.dev/docs/reference/global#app-removal)

**Type** `“``remove``”`` | ``“``retain``”`` | ``“``retain-all``”`
The removal policy for the current stage. If `removal` was not set in the `sst.config.ts`, this will be return its default value, `retain`.

#### [$app.stage](https://sst.dev/docs/reference/global#app-stage)

**Type** `string`
The stage currently being run. You can use this to conditionally deploy resources based on the stage.
For example, to deploy a bucket only in the `dev` stage:
sst.config.ts

```typescript

if ($app.stage==="dev") {

new sst.aws.Bucket("MyBucket");

}

```

### [$dev](https://sst.dev/docs/reference/global#dev)

**Type** `boolean`
Returns `true` if the app is running in `sst dev`.

### [$util](https://sst.dev/docs/reference/global#util)

**Type**
A convenience reference to the the
This is useful for working with components. You can use these without importing or installing the Pulumi SDK. For example, to create a new asset, you can:
sst.config.ts

```typescript


const myFiles = new$util.asset.FileArchive("./path/to/files");


```

This is equivalent to doing:
sst.config.ts

```typescript

import*as pulumi from"@pulumi/pulumi";

const myFiles = newpulumi.asset.FileArchive("./path/to/files");

```

## [Functions](https://sst.dev/docs/reference/global#functions)

### [$asset](https://sst.dev/docs/reference/global#asset)

```

$asset(assetPath)

```

#### [Parameters](https://sst.dev/docs/reference/global#parameters)

* `assetPath` `string`

**Returns** ` | `
Packages a file or directory into a Pulumi asset. This can be used for Pulumi resources that take an asset as input.
When the given path is a file, it returns a
This automatically resolves paths relative to the root of the app.
Relative paths are resolved relative to the root of the app. While, absolute paths are used as is.
If you have a file inside the `images` directory at the root of your app, you can upload it to S3 on deploy.
sst.config.ts

```typescript


const bucket = newaws.s3.Bucket("MyBucket");




new aws.s3.BucketObjectv2("MyImage", {




bucket: bucket.name,




key: "public/spongebob.svg",




contentType: "image/svg+xml",




source: $asset("images/spongebob.svg"),



});

```

You can also use this to zip up the files in the `files/` directory and upload it to S3.
sst.config.ts

```typescript

new aws.s3.BucketObjectv2("MyZip", {

bucket: bucket.name,

key: "public/spongebob.zip",

contentType: "application/zip",

source: $asset("files"),

});

```

### [$concat](https://sst.dev/docs/reference/global#concat)

```

$concat(params)

```

#### [Parameters](https://sst.dev/docs/reference/global#parameters-1)

* `params` `any``[]`

**Returns** `Output``<``string``>`
Takes a sequence of Output values or plain JavaScript values, stringifies each, and concatenates them into one final string.
This is takes care of resolving the Output values for you. Say you had a bucket:
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket");


```

Instead of having to resolve the bucket name first::
sst.config.ts

```typescript

const description = bucket.name.apply(name =>

"This is a bucket named ".concat(name)

);

```

You can directly do this:
sst.config.ts

```typescript


const description = $concat("This is a bucket named ", bucket.name);


```

### [$interpolate](https://sst.dev/docs/reference/global#interpolate)

```


$interpolate(literals, placeholders)


```

#### [Parameters](https://sst.dev/docs/reference/global#parameters-2)

* `literals` `TemplateStringsArray``<``>`
* `placeholders` `any``[]`

**Returns** `Output``<``string``>`
Use string interpolation on Output values.
This is takes care of resolving the Output values for you. Say you had a bucket:
sst.config.ts

```typescript

const bucket = newsst.aws.Bucket("MyBucket");

```

Instead of resolving the bucket name first:
sst.config.ts

```typescript


const description = bucket.name.apply(name => `This is a bucket named ${name}`);


```

You can directly do this:
sst.config.ts

```typescript

const description = $interpolate`This is a bucket named ${bucket.name}`;

```

### [$jsonParse](https://sst.dev/docs/reference/global#jsonparse)

```

$jsonParse(text, reviver?)

```

#### [Parameters](https://sst.dev/docs/reference/global#parameters-3)

* `text` `Input``<``string``>`
* `reviver?`

**Returns** `Output``<``any``>`
Takes an Output value or plain JavaScript value, uses `JSON.parse` on the resolved JSON string to turn it into a JSON object.
So for example, instead of doing of resolving the value first:
sst.config.ts

```typescript


const policy = policyStr.apply((policy) =>




JSON.parse(policy)



);

```

You can directly do this:
sst.config.ts

```typescript

const policy = $jsonParse(policyStr);

```

### [$jsonStringify](https://sst.dev/docs/reference/global#jsonstringify)

```

$jsonStringify(obj, replacer?, space?)

```

#### [Parameters](https://sst.dev/docs/reference/global#parameters-4)

* `obj` `any`
* `replacer?`
* `space?` `string`` | ``number`

**Returns** `Output``<``string``>`
Takes an Output value or plain JSON object, uses `JSON.stringify` on the resolved JSON object to turn it into a JSON string.
So for example, instead of doing of resolving the value first:
sst.config.ts

```typescript


const policy = policyObj.apply((policy) =>




JSON.stringify(policy)



);

```

You can directly do this:
sst.config.ts

```typescript

const policy = $jsonStringify(policyObj);

```

### [$resolve](https://sst.dev/docs/reference/global#resolve)

```

$resolve(val)

```

#### [Parameters](https://sst.dev/docs/reference/global#parameters-5)

* `val` `Record``<``string`, `Input``<``T``>``>`

**Returns** `Output``<``Record``<``string`, `T``>``>`
Wait for a list of Output values to be resolved, and then apply a function to their resolved values.
Say you had a couple of S3 Buckets:
sst.config.ts

```typescript


const bucket1 = newsst.aws.Bucket("MyBucket1");




const bucket2 = newsst.aws.Bucket("MyBucket2");


```

You can run a function after both of them are resolved:
sst.config.ts

```typescript

$resolve([bucket1.name, bucket2.name]).apply(([value1, value2])=>

console.log({ value1, value2 })

);

```

### [$transform](https://sst.dev/docs/reference/global#transform)

```

$transform(resource, cb)

```

#### [Parameters](https://sst.dev/docs/reference/global#parameters-6)

* `resource` `Component Class`
* `cb` `(args, opts, name) => void`

**Returns** `void`
Register a function that’ll be called when a component of the given type is about to be created. This is useful for setting global defaults for your components.
This function is only called for components that are created **after** the function is registered.
The function takes the arguments and options that are being passed to the component, and can modify them.
For example, to set a default runtime for all function components.
sst.config.ts

```typescript


$transform(sst.aws.Function, (args, opts, name)=> {



// Set the default if it's not set by the component



args.runtime??="nodejs20.x";



});

```

Here, `args`, `opts` and `name` are what you’d pass to the `Function` component. Recall the signature of the `Function` component:
sst.config.ts

```typescript

new sst.aws.Function(name: string, args: FunctionArgs, opts?: pulumi.ComponentResourceOptions)

```

## [AWS](https://sst.dev/docs/reference/global#aws)

### [iamEdit](https://sst.dev/docs/reference/global#iamedit)

```

iamEdit(policy, cb)

```

#### [Parameters](https://sst.dev/docs/reference/global#parameters-7)

* `policy` `Input``<``string`` | ``>`
* `cb` `(doc:`Object`) =>`void``

**Returns** `Output``<``string``>`
A helper to modify the AWS IAM policy.
The IAM policy document is normally in the form of a JSON string. This helper decodes the string into a JSON object and passes it to the callback. Allowing you to modify the policy document in a type-safe way.
For example, this comes in handy when you are transforming the policy of a component.
sst.config.ts

```typescript


new sst.aws.Bucket("MyBucket", {



transform: {



policy: (args)=> {




args.policy=sst.aws.iamEdit(args.policy, (policy)=> {




policy.Statement.push({




Effect: "Allow",




Action: "s3:PutObject",




Principal: { Service: "ses.amazonaws.com" },




Resource: $interpolate`arn:aws:s3:::${args.bucket}/*`,



});


});


},


},


});

```

[Skip to content](https://sst.dev/docs/share-across-stages#_top)

# Share Across Stages

You define all the resources in your app in your `sst.config.ts`. These resources then get created for each stage that you deploy to.
However, there might be some cases where you don’t want to recreate certain resources for every stage.
* * *

## [Why share](https://sst.dev/docs/share-across-stages#why-share)

You typically want to share for cases where:

* Resources that are expensive and their pricing is not truly pay-per-use, like your Postgres cluster.
* Or, if they contain data that these new stages need to reuse. For example, your PR stages might just be for testing against your staging data and don’t need to recreate some resources.

While it might be tempting to share more resources across stages, we only recommend doing it for the above cases.
* * *

## [How to share](https://sst.dev/docs/share-across-stages#how-to-share)

To help with this some SST components come with a `static get` method. These components are typically ones that people want to be able to share. Here are some components that have this:

* [`Vpc`](https://sst.dev/docs/component/aws/vpc/)
* [`Email`](https://sst.dev/docs/component/aws/email/)
* [`Bucket`](https://sst.dev/docs/component/aws/bucket/)
* [`Postgres`](https://sst.dev/docs/component/aws/postgres/)
* [`CognitoUserPool`](https://sst.dev/docs/component/aws/cognito-user-pool/)
* [`CognitoIdentityPool`](https://sst.dev/docs/component/aws/cognito-identity-pool/)

If you’d like us to add to this list, feel free to open a GitHub issue.
It’s worth noting that complex components like our frontends, `Nextjs`, or `StaticSite`, are not likely to be supported. Both because they are made up of a large number of resources. But also because they really aren’t worth sharing across stages.
Let’s look at an example.
* * *

### [Example](https://sst.dev/docs/share-across-stages#example)

The [`static get`](https://sst.dev/docs/component/aws/bucket/#static-get) in the `Bucket` component has the following signature. It takes the name of the component and the name of the existing bucket.

```


get(name: string, bucketName: string)


```

Imagine you create a bucket in the `dev` stage. And in your personal stage `frank`, instead of creating a new bucket, you want to share the bucket from `dev`.
sst.config.ts

```typescript

const bucket = $app.stage === "frank"

? sst.aws.Bucket.get("MyBucket", "app-dev-mybucket-12345678")

:new sst.aws.Bucket("MyBucket");

```

We are using [`$app.stage`](https://sst.dev/docs/reference/global/#app-stage), a global to get the current stage the CLI is running on. It allows us to conditionally create the bucket.
Here `app-dev-mybucket-12345678` is the auto-generated bucket name for the bucket created in the `dev` stage. You can find this by outputting the bucket name in the `dev` stage.
sst.config.ts

```typescript


return {




bucket: bucket.name



};

```

And it’ll print it out on `sst deploy`.

```


bucket:app-dev-mybucket-12345678


```

You can read more about outputs in the [`run`](https://sst.dev/docs/reference/config/#run) function.

[Skip to content](https://sst.dev/docs/component/linkable#_top)

# Linkable

The `Linkable` component and the `Linkable.wrap` method lets you link any resources in your app; not just the built-in SST components. It also lets you modify the links SST creates.

#### [Linking any value](https://sst.dev/docs/component/linkable#linking-any-value)

The `Linkable` component takes a list of properties that you want to link. These can be outputs from other resources or constants.
sst.config.ts

```typescript

new sst.Linkable("MyLinkable", {

properties: { foo: "bar" }

});

```

You can also use this to combine multiple resources into a single linkable resource. And optionally include permissions or bindings for the linked resource.
sst.config.ts

```typescript


const bucketA = newsst.aws.Bucket("MyBucketA");




const bucketB = newsst.aws.Bucket("MyBucketB");




const storage = newsst.Linkable("MyStorage", {



properties: {



foo: "bar",




bucketA: bucketA.name,




bucketB: bucketB.name



},



include: [




sst.aws.permission({




actions: ["s3:*"],




resources: [bucketA.arn, bucketB.arn]



})


]



});


```

You can now link this resource to your frontend or a function.
sst.config.ts

```typescript

new sst.aws.Function("MyApi", {

handler: "src/lambda.handler",

link: [storage]

});

```

Then use the [SDK](https://sst.dev/docs/reference/sdk/) to access it at runtime.
src/lambda.ts

```typescript


import { Resource } from"sst";




console.log(Resource.MyStorage.bucketA);


```

#### [Linking any resource](https://sst.dev/docs/component/linkable#linking-any-resource)

You can also wrap any Pulumi Resource class to make it linkable.
sst.config.ts

```typescript

sst.Linkable.wrap(aws.dynamodb.Table, (table)=> ({

properties: { tableName: table.name },

include: [

sst.aws.permission({

actions: ["dynamodb:*"],

resources: [table.arn]

})

]

}));

```

Now you create an instance of `aws.dynamodb.Table` and link it in your app like any other SST component.
sst.config.ts

```typescript


const table = newaws.dynamodb.Table("MyTable", {




attributes: [{ name: "id", type: "S" }],




hashKey: "id"




});




new sst.aws.Nextjs("MyWeb", {



link: [table]


});

```

And use the [SDK](https://sst.dev/docs/reference/sdk/) to access it at runtime.
app/page.tsx```

import { Resource } from"sst";

console.log(Resource.MyTable.tableName);

```

Your function will also have the permissions defined above.
#### [Modify built-in links](https://sst.dev/docs/component/linkable#modify-built-in-links)
You can also modify how SST creates links. For example, you might want to change the permissions of a linkable resource.
sst.config.ts
```typescript


sst.Linkable.wrap(sst.aws.Bucket, (bucket)=> ({




properties: { name: bucket.name },



include: [



sst.aws.permission({




actions: ["s3:GetObject"],




resources: [bucket.arn]



})


]


}));

```

This overrides the built-in link and lets you create your own.
* * *

## [Constructor](https://sst.dev/docs/component/linkable#constructor)

```


newLinkable(name, definition)


```

#### [Parameters](https://sst.dev/docs/component/linkable#parameters)

* `name` `string`
* `definition` [`Definition`](https://sst.dev/docs/component/linkable#definition)

## [Properties](https://sst.dev/docs/component/linkable#properties)

### [name](https://sst.dev/docs/component/linkable#name)

**Type** `Output``<``string``>`

### [properties](https://sst.dev/docs/component/linkable#properties-1)

**Type** `Record``<``string`, `any``>`

## [Methods](https://sst.dev/docs/component/linkable#methods)

### [static wrap](https://sst.dev/docs/component/linkable#static-wrap)

```


Linkable.wrap(cls, cb)


```

#### [Parameters](https://sst.dev/docs/component/linkable#parameters-1)

* `cls` `Constructor`
The resource class to wrap.
* `cb` `(resource:`Resource`) => [`Definition`](https://sst.dev/docs/component/linkable#definition)`
A callback that returns the definition for the linkable resource.

**Returns** `void`
Wrap any resource class to make it linkable. Behind the scenes this modifies the prototype of the given class.
Use `Linkable.wrap` to make any resource linkable.
Here we are wrapping the
sst.config.ts

```typescript

Linkable.wrap(aws.dynamodb.Table, (table)=> ({

properties: { tableName: table.name },

include: [

sst.aws.permission({

actions: ["dynamodb:*"],

resources: [table.arn]

})

]

}));

```

It’s defining the properties that we want made accessible at runtime and the permissions that the linked resource should have.
Now you can link any `aws.dynamodb.Table` instances in your app just like any other SST component.
sst.config.ts

```typescript


const table = newaws.dynamodb.Table("MyTable", {




attributes: [{ name: "id", type: "S" }],




hashKey: "id",




});




new sst.aws.Nextjs("MyWeb", {



link: [table]


});

```

Since this applies to any resource, you can also use it to wrap SST components and modify how they are linked.
sst.config.ts

```typescript

sst.Linkable.wrap(sst.aws.Bucket, (bucket)=> ({

properties: { name: bucket.name },

include: [

sst.aws.permission({

actions: ["s3:GetObject"],

resources: [bucket.arn]

})

]

}));

```

This overrides the built-in link and lets you create your own.
You can modify the permissions granted by a linked resource.
In the above example, we’re modifying the permissions to access a linked `sst.aws.Bucket` in our app.

## [Definition](https://sst.dev/docs/component/linkable#definition)

### [include?](https://sst.dev/docs/component/linkable#include)

**Type** `(`[`sst.aws.permission`](https://sst.dev/docs/component/aws/permission/)` | `[`sst.cloudflare.binding`](https://sst.dev/docs/component/cloudflare/binding/)`)[]`
Include AWS permissions or Cloudflare bindings for the linkable resource. The linked resource will have these permissions or bindings.
Include AWS permissions.

```

{

include: [

sst.aws.permission({

actions: ["lambda:InvokeFunction"],

resources: ["*"]

})

]

}

```

Include Cloudflare bindings.

```

{

include: [

sst.cloudflare.binding({

type: "r2BucketBindings",

properties: {

bucketName: "my-bucket"

}

})

]

}

```

### [properties](https://sst.dev/docs/component/linkable#properties-2)

**Type** `Record``<``string`, `any``>`
Define values that the linked resource can access at runtime. These can be outputs from other resources or constants.

```

{

properties: { foo: "bar" }

}

```

[Skip to content](https://sst.dev/docs/reference/config#_top)

# Config

The `sst.config.ts` file is used to configure your SST app and its resources.

```

$config(input: Config): Config

```

You specify it using the `$config` function. This takes an object of type [`Config`](https://sst.dev/docs/reference/config#config).
sst.config.ts

```typescript


/// <referencepath="./.sst/platform/config.d.ts" />




exportdefault$config({



// Your app's config



app(input) {




return {




name: "my-sst-app",




home: "aws"



};


},


// Your app's resources



asyncrun() {




constbucket = newsst.aws.Bucket("MyBucket");



// Your app's outputs



return {




bucket: bucket.name



};


},


// Optionally, your app's Console config


console: {


autodeploy: {



runner: { compute: "large" }



}


}


});

```

The `Config` object takes:

  1. [`app`](https://sst.dev/docs/reference/config#app-2) — Your config
  2. [`run`](https://sst.dev/docs/reference/config#run) — Your resources
  3. [`console`](https://sst.dev/docs/reference/config#console) — Optionally, your app’s Console config

The `app` function is evaluated right when your app loads. It’s used to define the app config and its providers.
You need TypeScript 5 to see the types in your config.
You can add Pulumi code in the `run` function not the `app` function. While the `run` function is where you define your resources using SST or Pulumi’s components.
The run function also has access to a list of [Global](https://sst.dev/docs/reference/global/) `$` variables and functions. These serve as the context for your app config.
Do not `import` the provider packages in your `sst.config.ts`.
Since SST manages importing your provider packages, it’s recommended not to add any imports in your `sst.config.ts`.
* * *

#### [.env](https://sst.dev/docs/reference/config#env)

Your `.env` and `.env.<stage>` files are loaded as environment variables in your config. They need to be in the same directory as your `sst.config.ts`.
.env```

MY_ENV_VAR=hello

```

And are available as `process.env` in both your `app` and `run` functions.
sst.config.ts
```typescript


process.env.MY_ENV_VAR


```

The `.env` file takes precedence over `.env.<stage>`. So if you have a `.env` and a `.env.dev` file, the values in the `.env` file will be used.
You need to restart `sst dev` for changes in your `.env` files to take effect.
Make sure the stage name in your `.env.<stage>` matches the stage your app is running on.
* * *

## [Config](https://sst.dev/docs/reference/config#config)

### [console?](https://sst.dev/docs/reference/config#console)

**Type** `Object`

* [`autodeploy`](https://sst.dev/docs/reference/config#console-autodeploy) `Object`
  * [`runner?`](https://sst.dev/docs/reference/config#console-autodeploy-runner)
  * [`target?`](https://sst.dev/docs/reference/config#console-autodeploy-target)
  * [`workflow?`](https://sst.dev/docs/reference/config#console-autodeploy-workflow)

Configure how your app works with the SST Console.

#### [console.autodeploy](https://sst.dev/docs/reference/config#console-autodeploy)

**Type** `Object`
**Default** Auto-deploys branches and PRs.
Auto-deploys your app when you _git push_ to your repo. Uses
To get started, first [make sure to set up Autodeploy](https://sst.dev/docs/console#setup). Specifically, you need to configure an environment with the stage and AWS account you want to auto-deploy to.
Now when you _git push_ to a branch, pull request, or tag, the following happens:

  1. The stage name is generated based on the `autodeploy.target` callback.
    1. If there is no callback, the stage name is a sanitized version of the branch or tag.
    2. If there is a callback but no stage is returned, the deploy is skipped.
  2. The runner config is generated based on the `autodeploy.runner`. Or the defaults are used.
  3. The stage is matched against the environments in the Console to get the AWS account and any environment variables for the deploy.
  4. The deploy is run based on the above config.

This only applies only to git events. If you trigger a deploy through the Console, you are asked to sepcify the stage you want to deploy to. So in this case, it skips step 1 from above and does not call `autodeploy.target`.
You can further configure Autodeploy through the `autodeploy` prop.
sst.config.ts

```typescript

console: {

autodeploy: {

target(event) {}, // Customize the target stage

runner(stage) {}, // Customize the runner

async workflow({ $, input }) {} // Customize the workflow

}

}

```

Here, `target`, `runner`, and `workflow` are all optional and come with defaults, so you don’t need to configure anything. But you can customize them.

```

{

autodeploy: {

target(event) {

if (

event.type==="branch"&&

event.branch==="main"&&

event.action==="pushed"

) {

return { stage: "production" };

}

},

runner(stage) {

if (stage ==="production") return { timeout: "3 hours" };

}

}

}

```

For example, here we are only auto-deploying to the `production` stage when you git push to the `main` branch. We are also setting the timeout to 3 hours for the `production` stage. You can read more about the `target` and `runner` props below.
Finally, if you want to configure exactly what happens in the build, you can pass in a `workflow` function.

```

{

autodeploy: {

async workflow({ $, event }) {

await$`npm i -g pnpm`;

await$`pnpm i`;

event.action==="removed"

?await$`pnpm sst remove`

:await$`pnpm sst deploy`;

}

}

}

```

You can read more the `workflow` prop below.

##### [console.autodeploy.runner?](https://sst.dev/docs/reference/config#console-autodeploy-runner)

**Type** [`Runner`](https://sst.dev/docs/reference/config#runner)`| ``(input: [`RunnerInput`](https://sst.dev/docs/reference/config#runnerinput)) => [`Runner`](https://sst.dev/docs/reference/config#runner)`
Configure the runner that will run the build. By default it uses the following config:

```

{

runner: {

engine: "codebuild",

architecture: "x86_64",

compute: "medium",

timeout: "1 hour"

}

}

```

Most of these are optional and come with defaults. But you can configure them.

```

{

runner: { timeout: "3 hours" }

}

```

You can also configure it based on the stage that’s being deployed. Let’s say you want to use the defaults for all stages except for `production`.

```

{

runner(stage) {

if (stage ==="production") return { timeout: "3 hours" };

}

}

```

Aside from the above, you can also have the deploys run inside a VPC.

```

{

runner: {

vpc: {

id: "vpc-0be8fa4de860618bb",

securityGroups: ["sg-0399348378a4c256c"],

subnets: ["subnet-0b6a2b73896dc8c4c", "subnet-021389ebee680c2f0"]

}

}

}

```

Or configure files or directories to be cached.

```

{

runner: {

cache: {

paths: ["node_modules", "/path/to/cache"]

}

}

}

```

A _runner_ is a **your account**.
Once a runner is created, it can be used to run multiple builds of the same machine config concurrently. Runners are also shared across all apps in the same account and region.
You are only charged for the number of build minutes that you use.
If a runner with a given config has been been previously created, it’ll be reused. The Console will also automatically remove runners that have not been used for more than 7 days.
You are not charged for the number of runners you have, only for the number of build minutes that you use. The pricing is based on the machine config used.

##### [console.autodeploy.target?](https://sst.dev/docs/reference/config#console-autodeploy-target)

```

target(input)

```

**Parameters**

* `input` [`BranchEvent`](https://sst.dev/docs/reference/config#branchevent)` | `[`TagEvent`](https://sst.dev/docs/reference/config#tagevent)` | `[`PullRequestEvent`](https://sst.dev/docs/reference/config#pullrequestevent)

**Returns** `undefined`` |`[`Target`](https://sst.dev/docs/reference/config#target)
Defines the stage or a list of stages the app will be auto-deployed to.
When a git event is received, Autodeploy will run the `target` function with the git event. This function should return the stage or a list of stages the app will be deployed to. Or `undefined` if the deploy should be skipped.
Return `undefined` to skip the deploy.
The stage that is returned is then compared to the environments set in the [app settings in the Console](https://sst.dev/docs/console/#setup). If the stage matches an environment, the stage will be deployed to that environment. If no matching environment is found, the deploy will be skipped.
You need to configure an environment in the Console to be able to deploy to it.
Currently, only git events for **branches** , **pull requests** , and **tags** are supported.
This is not called when you manually trigger a deploy through the Console.
This config only applies to git events. If you trigger a deploy through the Console, you are asked to sepcify the stage you want to deploy to. In this case, and when you redeploy a manual deploy, the `target` function is not called.
By default, this is what the `target` function looks like:

```

{

target(event) {

if (event.type==="branch"&& event.action==="pushed") {

return {

stage: event.branch

.replace(/[^a-zA-Z0-9-]/g, "-")

.replace(/-+/g, "-")

.replace(/^-/g, "")

.replace(/-$/g, "")

};

}

if (event.type==="pull_request") {

return { stage: `pr-${event.number}` };

}

}

}

```

So for a:

* **branch** : The stage name is a sanitized version of the branch name. When a branch is removed, the stage is **not removed**.
* **pull request** : The stage name is `pr-<number>`. When a pull request is closed, the stage **is removed**.

Git events to tags are not auto-deployed by default.
Git events to tags are not auto-deployed by default. You can change this by adding it to your config.

```

{

target(event) {

if (event.type==="tag"&& event.action==="pushed") {

return {

stage: "tag-"+ event.tag

.replace(/[^a-zA-Z0-9-]/g, "-")

.replace(/-+/g, "-")

.replace(/^-/g, "")

.replace(/-$/g, "")

};

}

}

}

```

Here, similar to the branch event, we are sanitizing the tag name to generate the stage. Just make sure to configure the environment for these tag stages in the Console.
If you don’t want to auto-deploy for a given event, you can return `undefined`. For example, to skip any deploys to the `staging` stage.

```

{

target(event) {

if (event.type==="branch"&& event.branch==="staging") return;

if (

event.type==="branch"&&

event.branch==="main"&&

event.action==="pushed"

) {

return { stage: "production" };

}

}

}

```

##### [console.autodeploy.workflow?](https://sst.dev/docs/reference/config#console-autodeploy-workflow)

```

workflow(input)

```

**Parameters**

* `input` [`WorkflowInput`](https://sst.dev/docs/reference/config#workflowinput)

**Returns** `Promise``<``void``>`
Customize the commands that are run during the build process. This is useful for running tests, or completely customizing the build process.
The default workflow automatically figures out the package manager you are using, installs the dependencies, and runs `sst deploy` or `sst remove` based on the event.
For example, if you are using pnpm, the following is equivalent to the default workflow.

```

{

async workflow({ $, event }) {

await$`npm i -g pnpm`;

await$`pnpm i`;

event.action==="removed"

?await$`pnpm sst remove`

:await$`pnpm sst deploy`;

}

}

```

The workflow function is run inside a Bun process. It passes in `$` as the _bash-like_ scripting easier.
Use the Bun Shell to make running commands easier.
For example, here’s how you can run tests before deploying.

```

{

async workflow({ $, event }) {

await$`npm i -g pnpm`;

await$`pnpm i`;

await$`pnpm test`;

event.action==="removed"

?await$`pnpm sst remove`

:await$`pnpm sst deploy`;

}

}

```

When you pass in a `workflow`, you are effectively taking control of what runs in your build.
If you don’t run `sst deploy`, your app won’t be deployed.
This means that if you don’t run `sst deploy`, your app won’t be deployed.
Throwing an error will fail the build and display the error in the Console.
If you throw an error in the workflow, the deploy will fail and the error will be displayed in the Autodeploy logs.
Here’s a more detailed example of using the Bun Shell to handle failures.

```

{

async workflow({ $, event }) {

await$`npm i -g pnpm`;

await$`pnpm i`;

const { exitCode } = await $`pnpm test`.nothrow();

if (exitCode !==0) {

// Process the test report and then fail the build

thrownewError("Failed to run tests");

}

event.action==="removed"

?await$`pnpm sst remove`

:await$`pnpm sst deploy`;

}

}

```

You’ll notice we are not passing in `--stage` to the SST commands. This is because the `SST_STAGE` environment variable is already set in the build process.
You don’t need to pass in `--stage` to the SST commands.
The build process is run inside an `architecture` used.

### [app](https://sst.dev/docs/reference/config#app)

```

app(input)

```

#### [Parameters](https://sst.dev/docs/reference/config#parameters)

* `input` [`AppInput`](https://sst.dev/docs/reference/config#appinput)

**Returns** [`App`](https://sst.dev/docs/reference/config#app)`| ``Promise``<`[`App`](https://sst.dev/docs/reference/config#app)`>`
The config for your app. It needs to return an object of type [`App`](https://sst.dev/docs/reference/config#app-1). The `app` function is evaluated when your app loads.
You cannot define any components or resources in the `app` function.
Here’s an example of a simple `app` function.
sst.config.ts

```typescript


app(input) {




return {




name: "my-sst-app",




home: "aws",



providers: {



aws: true,



cloudflare: {



accountId: "6fef9ed9089bb15de3e4198618385de2"



}


},



removal: input.stage==="production"?"retain":"remove"



};


},

```

### [run](https://sst.dev/docs/reference/config#run)

```


run()


```

**Returns** `Promise``<``void`` | ``Record``<``string`, `any``>``>`
An async function that lets you define the resources in your app.
You can use SST and Pulumi components only in the `run` function.
You can optionally return an object that’ll be displayed as the output in the CLI.
For example, here we return the name of the bucket we created.
sst.config.ts

```typescript

async run() {

const bucket = newsst.aws.Bucket("MyBucket");

return {

bucket: bucket.name

};

}

```

This will display the following in the CLI on `sst deploy` and `sst dev`.

```

bucket:bucket-jOaikGu4rla

```

These outputs are also written to a `.sst/outputs.json` file after every successful deploy. It contains the above outputs in JSON.
.sst/outputs.json```

{"bucket": "bucket-jOaikGu4rla"}

```

## [App](https://sst.dev/docs/reference/config#app-1)

### [home](https://sst.dev/docs/reference/config#home)

**Type** `“``aws``”`` | ``“``cloudflare``”`` | ``“``local``”`
The provider SST will use to store the state for your app. The state keeps track of all your resources and secrets. The state is generated locally and backed up in your cloud provider.
Currently supports AWS, Cloudflare and local.
SST uses the `home` provider to store the state for your app. If you use the local provider it will be saved on your machine. You can see where by running `sst version`.
If you want to configure the aws or cloudflare home provider, you can:

```

{

home: "aws",

providers: {

aws: {

region: "us-west-2"

}

}

}

```

### [name](https://sst.dev/docs/reference/config#name)

**Type** `string`
The name of the app. This is used to prefix the names of the resources in your app.
If you change the name of your app, it’ll redeploy your app with new resources. The old resources will be orphaned.
This means that you don’t want to change the name of your app without removing the old resources first.

```

{

name: "my-sst-app"

}

```

### [protect?](https://sst.dev/docs/reference/config#protect)

**Type** `boolean`
If set to `true`, the `sst remove` CLI will not run and will error out.
This is useful for preventing cases where you run `sst remove --stage <stage>` for the wrong stage.
Protect your production stages from being accidentally removed.
For example, prevent the _production_ stage from being removed.

```

{

protect: input.stage==="production"

}

```

However, this only applies to `sst remove` for stages.
If you accidentally remove a resource from the `sst.config.ts` and run `sst deploy` or `sst dev`, it’ll still get removed. To avoid this, check out the `removal` prop.

### [providers?](https://sst.dev/docs/reference/config#providers)

**Type** `Record``<``string`, `any``>`
**Default** The `home` provider.
The providers that are being used in this app. This allows you to use the resources from these providers in your app.

```

{

providers: {

aws: "6.27.0",

cloudflare: "5.37.1"

}

}

```

Check out the full list in the [Directory](https://sst.dev/docs/all-providers#directory).
You’ll need to run `sst install` after you update the `providers` in your config.
If you don’t set a `provider` it uses your `home` provider with the default config. So if you set `home` to `aws`, it’s the same as doing:

```

{

home: "aws",

providers: {

aws: "6.27.0"

}

}

```

You can also configure the provider props. Here’s the config for some common providers:
For example, to change the region for AWS.

```

{

providers: {

aws: {

region: "us-west-2"

}

}

}

```

### [removal?](https://sst.dev/docs/reference/config#removal)

**Type** `“``remove``”`` | ``“``retain``”`` | ``“``retain-all``”`
**Default** `“retain”`
Configure how your resources are handled when they have to be removed.

* `remove`: Removes the underlying resource.
* `retain`: Retains resources like S3 buckets and DynamoDB tables. Removes everything else.
* `retain-all`: Retains all resources.

If you change your removal policy, you’ll need to deploy your app once for it to take effect.
For example, retain resources if it’s the _production_ stage, otherwise remove all resources.

```

{

removal: input.stage==="production"?"retain":"remove"

}

```

This applies to not just the `sst remove` command but also cases where you remove a resource from the `sst.config.ts` and run `sst dev` or `sst deploy`.
To control how a stage is handled on `sst remove`, check out the `protect` prop.

### [version?](https://sst.dev/docs/reference/config#version)

**Type** `string`
**Default** The latest version of SST.
The version of SST supported by the app. The CLI will fail any commands if the version does not match.
Useful in CI where you don’t want it to automatically deploy with a new version of SST.
Takes a specific version.

```

version: "3.2.49"

```

Also supports semver ranges.

```

version: ">= 3.2.49"

```

## [AppInput](https://sst.dev/docs/reference/config#appinput)

### [stage](https://sst.dev/docs/reference/config#stage)

**Type** `string`
The stage this app is running on. This is a string that can be passed in through the CLI.
Changing the stage will redeploy your app to a new stage with new resources. The old resources will still be around in the old stage.
If not passed in, it’ll use the username of your local machine, or prompt you for it.

## [BranchEvent](https://sst.dev/docs/reference/config#branchevent)

A git event for when a branch is updated or deleted. For example:

```

{

type: "branch",

action: "pushed",

repo: {

id: 1296269,

owner: "octocat",

repo: "Hello-World"

},

branch: "main",

commit: {

id: "b7e7c4c559e0e5b4bc6f8d98e0e5e5e5e5e5e5e5",

message: "Update the README with new information"

},

sender: {

id: 1,

username: "octocat"

}

}

```

### [action](https://sst.dev/docs/reference/config#action)

**Type** `“``pushed``”`` | ``“``removed``”`
The type of the git action.

* `pushed` is when you git push to a branch
* `removed` is when a branch is removed

### [branch](https://sst.dev/docs/reference/config#branch)

**Type** `string`
The name of the branch the event is coming from.

### [commit](https://sst.dev/docs/reference/config#commit)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#commit-id)
* [`message`](https://sst.dev/docs/reference/config#commit-message)

Info about the commit in the event. This might look like:

```

{

id: "b7e7c4c559e0e5b4bc6f8d98e0e5e5e5e5e5e5e5",

message: "Update the README with new information"

}

```

#### [commit.id](https://sst.dev/docs/reference/config#commit-id)

**Type** `string`
The ID of the commit.

#### [commit.message](https://sst.dev/docs/reference/config#commit-message)

**Type** `string`
The commit message.

### [repo](https://sst.dev/docs/reference/config#repo)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#repo-id)
* [`owner`](https://sst.dev/docs/reference/config#repo-owner)
* [`repo`](https://sst.dev/docs/reference/config#repo-repo)

The Git repository the event is coming from. This might look like:

```

{

id: 1296269,

owner: "octocat",

repo: "Hello-World"

}

```

#### [repo.id](https://sst.dev/docs/reference/config#repo-id)

**Type** `number`
The ID of the repo. This is usually a number.

#### [repo.owner](https://sst.dev/docs/reference/config#repo-owner)

**Type** `string`
The name of the owner or org the repo to belongs to.

#### [repo.repo](https://sst.dev/docs/reference/config#repo-repo)

**Type** `string`
The name of the repo.

### [sender](https://sst.dev/docs/reference/config#sender)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#sender-id)
* [`username`](https://sst.dev/docs/reference/config#sender-username)

The user that generated the event. For example:

```

{

id: 1,

username: "octocat"

}

```

#### [sender.id](https://sst.dev/docs/reference/config#sender-id)

**Type** `number`
The ID of the user.

#### [sender.username](https://sst.dev/docs/reference/config#sender-username)

**Type** `string`
The username of the user.

### [type](https://sst.dev/docs/reference/config#type)

**Type** `“``branch``”`
The git event type, for the `BranchEvent` it’s `branch`.

## [PullRequestEvent](https://sst.dev/docs/reference/config#pullrequestevent)

A git event for when a pull request is updated or deleted. For example:

```

{

type: "pull_request",

action: "pushed",

repo: {

id: 1296269,

owner: "octocat",

repo: "Hello-World"

},

number: 1347,

base: "main",

head: "feature",

commit: {

id: "b7e7c4c559e0e5b4bc6f8d98e0e5e5e5e5e5e5e5",

message: "Update the README with new information"

},

sender: {

id: 1,

username: "octocat"

}

}

```

### [action](https://sst.dev/docs/reference/config#action-1)

**Type** `“``pushed``”`` | ``“``removed``”`
The type of the git action.

* `pushed` is when you git push to the base branch of the PR
* `removed` is when the PR is closed or merged

### [base](https://sst.dev/docs/reference/config#base)

**Type** `string`
The base branch of the PR. This is the branch the code is being merged into.

### [commit](https://sst.dev/docs/reference/config#commit-1)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#commit-id-1)
* [`message`](https://sst.dev/docs/reference/config#commit-message-1)

Info about the commit in the event. This might look like:

```

{

id: "b7e7c4c559e0e5b4bc6f8d98e0e5e5e5e5e5e5e5",

message: "Update the README with new information"

}

```

#### [commit.id](https://sst.dev/docs/reference/config#commit-id-1)

**Type** `string`
The ID of the commit.

#### [commit.message](https://sst.dev/docs/reference/config#commit-message-1)

**Type** `string`
The commit message.

### [head](https://sst.dev/docs/reference/config#head)

**Type** `string`
The head branch of the PR. This is the branch the code is coming from.

### [number](https://sst.dev/docs/reference/config#number)

**Type** `number`
The pull request number.

### [repo](https://sst.dev/docs/reference/config#repo-1)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#repo-id-1)
* [`owner`](https://sst.dev/docs/reference/config#repo-owner-1)
* [`repo`](https://sst.dev/docs/reference/config#repo-repo-1)

The Git repository the event is coming from. This might look like:

```

{

id: 1296269,

owner: "octocat",

repo: "Hello-World"

}

```

#### [repo.id](https://sst.dev/docs/reference/config#repo-id-1)

**Type** `number`
The ID of the repo. This is usually a number.

#### [repo.owner](https://sst.dev/docs/reference/config#repo-owner-1)

**Type** `string`
The name of the owner or org the repo to belongs to.

#### [repo.repo](https://sst.dev/docs/reference/config#repo-repo-1)

**Type** `string`
The name of the repo.

### [sender](https://sst.dev/docs/reference/config#sender-1)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#sender-id-1)
* [`username`](https://sst.dev/docs/reference/config#sender-username-1)

The user that generated the event. For example:

```

{

id: 1,

username: "octocat"

}

```

#### [sender.id](https://sst.dev/docs/reference/config#sender-id-1)

**Type** `number`
The ID of the user.

#### [sender.username](https://sst.dev/docs/reference/config#sender-username-1)

**Type** `string`
The username of the user.

### [title](https://sst.dev/docs/reference/config#title)

**Type** `string`
The title of the pull request.

### [type](https://sst.dev/docs/reference/config#type-1)

**Type** `“``pull_request``”`
The git event type, for the `PullRequestEvent` it’s `pull_request`.

## [Runner](https://sst.dev/docs/reference/config#runner)

### [architecture?](https://sst.dev/docs/reference/config#architecture)

**Type** `“``x86_64``”`` | ``“``arm64``”`
**Default** `x86_64`
The architecture of the build machine.
The `x86_64` machine uses the `arm64` uses the
You can also configure what’s used in the image:

* **Node**
To specify the version of Node you want to use in your build, you can use the `.node-version`, `.nvmrc`, or use the `engine` field in your `package.json`.
  * [package.json](https://sst.dev/docs/reference/config#tab-panel-97)
  * [node-version](https://sst.dev/docs/reference/config#tab-panel-98)
  * [nvmrc](https://sst.dev/docs/reference/config#tab-panel-99)
package.json```

{

engine: {

node: "20.15.1"

}

}

```

.node-version```

20.15.1

```

.nvmrc```

20.15.1

```

* **Package manager**
To specify the package manager you want to use you can configure it through your `package.json`.
  * [pnpm](https://sst.dev/docs/reference/config#tab-panel-100)
  * [bun](https://sst.dev/docs/reference/config#tab-panel-101)
package.json```

{

packageManager: "pnpm@8.6.3"

}

```

package.json```

{

packageManager: "bun@1.2.0"

}

```

Feel free to get in touch if you want to use your own build image or configure what’s used in the build image.

### [cache?](https://sst.dev/docs/reference/config#cache)

**Type** `Object`

* [`paths`](https://sst.dev/docs/reference/config#cache-paths)

Paths to cache as a part of the build. By default the `.git` directory is cached.
The given list of files and directories will be saved to the cache at the end of the build. And they will be restored at the start of the build process.

```

{

cache: {

paths: ["node_modules", "/path/to/cache"]

}

}

```

The relative paths are for caching files inside your repo. While the absolute path is for any global caches.
To clear the cache, you can trigger a new deploy using the **Force** deploy option in the Console.

#### [cache.paths](https://sst.dev/docs/reference/config#cache-paths)

**Type** `string``[]`
The paths to cache. These are relative to the root of the repository.
By default, the `.git` directory is always cached.

### [compute?](https://sst.dev/docs/reference/config#compute)

**Type** `“``small``”`` | ``“``medium``”`` | ``“``large``”`` | ``“``xlarge``”`` | ``“``2xlarge``”`
**Default** `medium`
The compute size of the build environment.
For `x86_64`, the following compute sizes are supported:

* `small`: 3 GB, 2 vCPUs
* `medium`: 7 GB, 4 vCPUs
* `large`: 15 GB, 8 vCPUs
* `xlarge`: 70 GB, 36 vCPUs
* `2xlarge`: 145 GB, 72 vCPUs

For `arm64` architecture, the following compute sizes are supported:

* `small`: 4 GB, 2 vCPUs
* `medium`: 8 GB, 4 vCPUs
* `large`: 16 GB, 8 vCPUs
* `xlarge`: 64 GB, 32 vCPUs
* `2xlarge`: 96 GB, 48 vCPUs

To increase the memory used by your Node.js process in the build environment, you’ll want to set the `NODE_OPTIONS` environment variable to `--max-old-space-size=xyz`. Where `xyz` is the memory size in MB. By default, this is set to 1.5 GB.
Read more about the

### [engine](https://sst.dev/docs/reference/config#engine)

**Type** `“``codebuild``”`
The service used to run the build. Currently, only AWS CodeBuild is supported.

### [timeout?](https://sst.dev/docs/reference/config#timeout)

**Type** `“``${number} minute``”`` | ``“``${number} minutes``”`` | ``“``${number} hour``”`` | ``“``${number} hours``”`
**Default** `1 hour`
The timeout for the build. It can be from `5 minutes` to `36 hours`.

### [vpc?](https://sst.dev/docs/reference/config#vpc)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#vpc-id)
* [`securityGroups`](https://sst.dev/docs/reference/config#vpc-securitygroups)
* [`subnets`](https://sst.dev/docs/reference/config#vpc-subnets)

The VPC to run the build in. If provided, the build environment will have access to resources in the VPC.
This is useful for building Next.js apps that might make queries to your database as a part of the build process.
You can get these from the outputs of the `Vpc` component your are using or from the [Console](https://sst.dev/docs/console/#resources).

```

{

vpc: {

id: "vpc-0be8fa4de860618bb",

subnets: ["subnet-0be8fa4de860618bb"],

securityGroups: ["sg-0be8fa4de860618bb"]

}

}

```

#### [vpc.id](https://sst.dev/docs/reference/config#vpc-id)

**Type** `string`
The ID of the VPC.

#### [vpc.securityGroups](https://sst.dev/docs/reference/config#vpc-securitygroups)

**Type** `string``[]`
The security groups to run the build in.

#### [vpc.subnets](https://sst.dev/docs/reference/config#vpc-subnets)

**Type** `string``[]`
The subnets to run the build in.

## [RunnerInput](https://sst.dev/docs/reference/config#runnerinput)

### [stage](https://sst.dev/docs/reference/config#stage-1)

**Type** `string`
The stage the deployment will be run in.

## [TagEvent](https://sst.dev/docs/reference/config#tagevent)

A git event for when a tag is created or deleted. For example:

```

{

type: "tag",

action: "pushed",

repo: {

id: 1296269,

owner: "octocat",

repo: "Hello-World"

},

tag: "v1.5.2",

commit: {

id: "b7e7c4c559e0e5b4bc6f8d98e0e5e5e5e5e5e5e5",

message: "Update the README with new information"

},

sender: {

id: 1,

username: "octocat"

}

}

```

### [action](https://sst.dev/docs/reference/config#action-2)

**Type** `“``pushed``”`` | ``“``removed``”`
The type of the git action.

* `pushed` is when you create a tag
* `removed` is when a tag is removed

### [commit](https://sst.dev/docs/reference/config#commit-2)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#commit-id-2)
* [`message`](https://sst.dev/docs/reference/config#commit-message-2)

Info about the commit in the event. This might look like:

```

{

id: "b7e7c4c559e0e5b4bc6f8d98e0e5e5e5e5e5e5e5",

message: "Update the README with new information"

}

```

#### [commit.id](https://sst.dev/docs/reference/config#commit-id-2)

**Type** `string`
The ID of the commit.

#### [commit.message](https://sst.dev/docs/reference/config#commit-message-2)

**Type** `string`
The commit message.

### [repo](https://sst.dev/docs/reference/config#repo-2)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#repo-id-2)
* [`owner`](https://sst.dev/docs/reference/config#repo-owner-2)
* [`repo`](https://sst.dev/docs/reference/config#repo-repo-2)

The Git repository the event is coming from. This might look like:

```

{

id: 1296269,

owner: "octocat",

repo: "Hello-World"

}

```

#### [repo.id](https://sst.dev/docs/reference/config#repo-id-2)

**Type** `number`
The ID of the repo. This is usually a number.

#### [repo.owner](https://sst.dev/docs/reference/config#repo-owner-2)

**Type** `string`
The name of the owner or org the repo to belongs to.

#### [repo.repo](https://sst.dev/docs/reference/config#repo-repo-2)

**Type** `string`
The name of the repo.

### [sender](https://sst.dev/docs/reference/config#sender-2)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#sender-id-2)
* [`username`](https://sst.dev/docs/reference/config#sender-username-2)

The user that generated the event. For example:

```

{

id: 1,

username: "octocat"

}

```

#### [sender.id](https://sst.dev/docs/reference/config#sender-id-2)

**Type** `number`
The ID of the user.

#### [sender.username](https://sst.dev/docs/reference/config#sender-username-2)

**Type** `string`
The username of the user.

### [tag](https://sst.dev/docs/reference/config#tag)

**Type** `string`
The name of the tag. For example, `v1.5.2`.

### [type](https://sst.dev/docs/reference/config#type-2)

**Type** `“``tag``”`
The git event type, for the `TagEvent` it’s `tag`.

## [Target](https://sst.dev/docs/reference/config#target)

### [stage](https://sst.dev/docs/reference/config#stage-2)

**Type** `string`` | ``string``[]`
The stage or a list of stages the app will be deployed to.

## [UserEvent](https://sst.dev/docs/reference/config#userevent)

A user event for when the user manually triggers a deploy. For example:

```

{

type: "user",

action: "deploy",

repo: {

id: 1296269,

owner: "octocat",

repo: "Hello-World"

},

ref: "main",

commit: {

id: "b7e7c4c559e0e5b4bc6f8d98e0e5e5e5e5e5e5e5",

message: "Update the README with new information"

}

}

```

### [action](https://sst.dev/docs/reference/config#action-3)

**Type** `“``remove``”`` | ``“``deploy``”`
The type of the user action.

* `deploy` is when you manually trigger a deploy
* `remove` is when you manually remove a stage

### [commit](https://sst.dev/docs/reference/config#commit-3)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#commit-id-3)
* [`message`](https://sst.dev/docs/reference/config#commit-message-3)

Info about the commit in the event. This might look like:

```

{

id: "b7e7c4c559e0e5b4bc6f8d98e0e5e5e5e5e5e5e5",

message: "Update the README with new information"

}

```

#### [commit.id](https://sst.dev/docs/reference/config#commit-id-3)

**Type** `string`
The ID of the commit.

#### [commit.message](https://sst.dev/docs/reference/config#commit-message-3)

**Type** `string`
The commit message.

### [ref](https://sst.dev/docs/reference/config#ref)

**Type** `string`
The reference to the Git commit. This can be the branch, tag, or commit hash.

### [repo](https://sst.dev/docs/reference/config#repo-3)

**Type** `Object`

* [`id`](https://sst.dev/docs/reference/config#repo-id-3)
* [`owner`](https://sst.dev/docs/reference/config#repo-owner-3)
* [`repo`](https://sst.dev/docs/reference/config#repo-repo-3)

The Git repository the event is coming from. This might look like:

```

{

id: 1296269,

owner: "octocat",

repo: "Hello-World"

}

```

#### [repo.id](https://sst.dev/docs/reference/config#repo-id-3)

**Type** `number`
The ID of the repo. This is usually a number.

#### [repo.owner](https://sst.dev/docs/reference/config#repo-owner-3)

**Type** `string`
The name of the owner or org the repo to belongs to.

#### [repo.repo](https://sst.dev/docs/reference/config#repo-repo-3)

**Type** `string`
The name of the repo.

### [type](https://sst.dev/docs/reference/config#type-3)

**Type** `“``user``”`
The user event type.

## [WorkflowInput](https://sst.dev/docs/reference/config#workflowinput)

### $

**Type**
The _bash-like_ shell for scripting with JavaScript and TypeScript.

### [event](https://sst.dev/docs/reference/config#event)

**Type** [`BranchEvent`](https://sst.dev/docs/reference/config#branchevent)` | `[`TagEvent`](https://sst.dev/docs/reference/config#tagevent)` | `[`PullRequestEvent`](https://sst.dev/docs/reference/config#pullrequestevent)` | `[`UserEvent`](https://sst.dev/docs/reference/config#userevent)
The event that triggered the workflow.
This includes git branch, pull request, or tag events. And it also includes a user event for manual deploys that are triggered through the Console.

[Skip to content](https://sst.dev/docs/component/aws/function#_top)

# Function

The `Function` component lets you add serverless functions to your app. It uses

#### [Supported runtimes](https://sst.dev/docs/component/aws/function#supported-runtimes)

Currently supports **Node.js** and **Golang** functions. **Python** and **Rust** are community supported. Other runtimes are on the roadmap.

#### [Minimal example](https://sst.dev/docs/component/aws/function#minimal-example)

* [Node](https://sst.dev/docs/component/aws/function#tab-panel-102)
* [Python](https://sst.dev/docs/component/aws/function#tab-panel-103)
* [Go](https://sst.dev/docs/component/aws/function#tab-panel-104)
* [Rust](https://sst.dev/docs/component/aws/function#tab-panel-105)

Pass in the path to your handler function.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




handler: "src/lambda.handler"



});

```

[Learn more below](https://sst.dev/docs/component/aws/function#handler).
Pass in the path to your handler function.
sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

runtime: "python3.11",

handler: "functions/src/functions/api.handler"

});

```

You need to have uv installed and your handler function needs to be in a uv workspace. [Learn more below](https://sst.dev/docs/component/aws/function#handler).
Pass in the directory to your Go module.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




runtime: "go",




handler: "./src"



});

```

[Learn more below](https://sst.dev/docs/component/aws/function#handler).
Pass in the directory where your Cargo.toml lives.
sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

runtime: "rust",

handler: "./crates/api/"

});

```

[Learn more below](https://sst.dev/docs/component/aws/function#handler).

#### [Set additional config](https://sst.dev/docs/component/aws/function#set-additional-config)

Pass in additional Lambda config.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




handler: "src/lambda.handler",




timeout: "3 minutes",




memory: "1024 MB"



});

```

#### [Link resources](https://sst.dev/docs/component/aws/function#link-resources)

[Link resources](https://sst.dev/docs/linking/) to the function. This will grant permissions to the resources and allow you to access it in your handler.
sst.config.ts

```typescript

const bucket = newsst.aws.Bucket("MyBucket");

new sst.aws.Function("MyFunction", {

handler: "src/lambda.handler",

link: [bucket]

});

```

You can use the [SDK](https://sst.dev/docs/reference/sdk/) to access the linked resources in your handler.

* [Node](https://sst.dev/docs/component/aws/function#tab-panel-106)
* [Python](https://sst.dev/docs/component/aws/function#tab-panel-107)
* [Go](https://sst.dev/docs/component/aws/function#tab-panel-108)
* [Rust](https://sst.dev/docs/component/aws/function#tab-panel-109)

src/lambda.ts

```typescript


import { Resource } from"sst";




console.log(Resource.MyBucket.name);


```

functions/src/functions/api.py```

from sst import Resource

def handler(event, context):

print(Resource.MyBucket.name)

```

Where the `sst` package can be added to your `pyproject.toml`.
functions/pyproject.toml```

[tool.uv.sources]



sst = { git = "https://github.com/sst/sst.git", subdirectory = "sdk/python", branch = "dev" }


```

src/main.go```

import (

"github.com/sst/sst/v3/sdk/golang/resource"

)

resource.Get("MyBucket", "name")

```

src/main.rs```


use sst_sdk::Resource;




#[derive(serde::Deserialize, Debug)]




struct Bucket {




name: String,



}



letresource= Resource::init().unwrap();




let Bucket { name } =resource.get("Bucket").unwrap();


```

#### [Set environment variables](https://sst.dev/docs/component/aws/function#set-environment-variables)

Set environment variables that you can read in your function. For example, using `process.env` in your Node.js functions.
sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

handler: "src/lambda.handler",

environment: {

DEBUG: "true"

}

});

```

#### [Enable function URLs](https://sst.dev/docs/component/aws/function#enable-function-urls)

Enable function URLs to invoke the function over HTTP.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




handler: "src/lambda.handler",




url: true



});

```

#### [Bundling](https://sst.dev/docs/component/aws/function#bundling)

Customize how SST uses `nodejs` property.
sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

handler: "src/lambda.handler",

nodejs: {

install: ["pg"]

}

});

```

Or override it entirely by passing in your own function `bundle`.
* * *

## [Constructor](https://sst.dev/docs/component/aws/function#constructor)

```

newFunction(name, args, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/function#parameters)

* `name` `string`
* `args` [`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)
* `opts?`

## [FunctionArgs](https://sst.dev/docs/component/aws/function#functionargs)

### [architecture?](https://sst.dev/docs/component/aws/function#architecture)

**Type** `Input``<``“``x86_64``”`` | ``“``arm64``”``>`
**Default** `“x86_64”`
The

```

{

architecture: "arm64"

}

```

### [bundle?](https://sst.dev/docs/component/aws/function#bundle)

**Type** `Input``<``string``>`
Path to the source code directory for the function. By default, the handler is bundled with `bundle` to skip bundling.
Use `bundle` only when you want to bundle the function yourself.
If the `bundle` option is specified, the `handler` needs to be in the root of the bundle.
Here, the entire `packages/functions/src` directory is zipped. And the handler is in the `src` directory.

```

{

bundle: "packages/functions/src",

handler: "index.handler"

}

```

### [concurrency?](https://sst.dev/docs/component/aws/function#concurrency)

**Type** `Input``<``Object``>`

* [`provisioned?`](https://sst.dev/docs/component/aws/function#concurrency-provisioned)
* [`reserved?`](https://sst.dev/docs/component/aws/function#concurrency-reserved)

**Default** No concurrency settings set
Configure the concurrency settings for the function.

```

{

concurrency: {

provisioned: 10,

reserved: 50

}

}

```

#### [concurrency.provisioned?](https://sst.dev/docs/component/aws/function#concurrency-provisioned)

**Type** `Input``<``number``>`
**Default** No provisioned concurrency
Provisioned concurrency ensures a specific number of Lambda instances are always ready to handle requests, reducing cold start times. Enabling this will incur extra charges.
Enabling provisioned concurrency will incur extra charges.
Note that `versioning` needs to be enabled for provisioned concurrency.

```

{

concurrency: {

provisioned: 10

}

}

```

#### [concurrency.reserved?](https://sst.dev/docs/component/aws/function#concurrency-reserved)

**Type** `Input``<``number``>`
**Default** No reserved concurrency
Reserved concurrency limits the maximum number of concurrent executions for a function, ensuring critical functions always have capacity. It does not incur extra charges.
Setting this to `0` will disable the function from being triggered.

```

{

concurrency: {

reserved: 50

}

}

```

### [copyFiles?](https://sst.dev/docs/component/aws/function#copyfiles)

**Type** `Input``<``Object``[]``>`

* [`from`](https://sst.dev/docs/component/aws/function#copyfiles-from)
* [`to?`](https://sst.dev/docs/component/aws/function#copyfiles-to)

Add additional files to copy into the function package. Takes a list of objects with `from` and `to` paths. These will be copied over before the function package is zipped up.
Copying over a single file from the `src` directory to the `src/` directory of the function package.

```

{

copyFiles: [{ from: "src/index.js" }]

}

```

Copying over a single file from the `src` directory to the `core/src` directory in the function package.

```

{

copyFiles: [{ from: "src/index.js", to: "core/src/index.js" }]

}

```

Copying over a couple of files.

```

{

copyFiles: [

{ from: "src/this.js", to: "core/src/this.js" },

{ from: "src/that.js", to: "core/src/that.js" }

]

}

```

#### [copyFiles[].from](https://sst.dev/docs/component/aws/function#copyfiles-from)

**Type** `Input``<``string``>`
Source path relative to the `sst.config.ts`.

#### [copyFiles[].to?](https://sst.dev/docs/component/aws/function#copyfiles-to)

**Type** `Input``<``string``>`
**Default** The `from` path in the function package
Destination path relative to function root in the package. By default, it creates the same directory structure as the `from` path and copies the file.

### [description?](https://sst.dev/docs/component/aws/function#description)

**Type** `Input``<``string``>`
A description for the function. This is displayed in the AWS Console.

```

{

description: "Handler function for my nightly cron job."

}

```

### [dev?](https://sst.dev/docs/component/aws/function#dev)

**Type** `Input``<``false``>`
**Default** `true`
Disable running this function [_Live_](https://sst.dev/docs/live/) in `sst dev`.
By default, the functions in your app are run locally in `sst dev`. To do this, a _stub_ version of your function is deployed, instead of the real function.
In `sst dev` a _stub_ version of your function is deployed.
This shows under the **Functions** tab in the multiplexer sidebar where your invocations are logged. You can turn this off by setting `dev` to `false`.
Read more about [Live](https://sst.dev/docs/live/) and [`sst dev`](https://sst.dev/docs/reference/cli/#dev).

```

{

dev: false

}

```

### [environment?](https://sst.dev/docs/component/aws/function#environment)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Key-value pairs of values that are set as

* Start with a letter
* Be at least 2 characters long
* Contain only letters, numbers, or underscores

They can be accessed in your function using `process.env.<key>`.
The total size of the environment variables cannot exceed 4 KB.

```

{

environment: {

DEBUG: "true"

}

}

```

### [handler](https://sst.dev/docs/component/aws/function#handler)

**Type** `Input``<``string``>`
Path to the handler for the function.

* For Node.js this is in the format `{path}/{file}.{method}`.
* For Python this is also `{path}/{file}.{method}`.
* For Golang this is `{path}` to the Go module.
* For Rust this is `{path}` to the Rust crate.

##### [Node.js](https://sst.dev/docs/component/aws/function#nodejs)

For example with Node.js you might have.

```

{

handler: "packages/functions/src/main.handler"

}

```

Where `packages/functions/src` is the path. And `main` is the file, where you might have a `main.ts` or `main.js`. And `handler` is the method exported in that file.
You don’t need to specify the file extension.
If `bundle` is specified, the handler needs to be in the root of the bundle directory.

```

{

bundle: "packages/functions/src",

handler: "index.handler"

}

```

##### [Python](https://sst.dev/docs/component/aws/function#python)

For Python,
You need uv installed for Python functions.
The functions need to be in a

```

{

handler: "functions/src/functions/api.handler"

}

```

The project structure might look something like this. Where there is a `pyproject.toml` file in the root and the `functions/` directory is a uv workspace with its own `pyproject.toml`.

```

├── sst.config.ts

├── pyproject.toml

└── functions

├── pyproject.toml

└── src

└── functions

├── **init**.py

└── api.py

```

To make sure that the right runtime is used in `sst dev`, make sure to set the version of Python in your `pyproject.toml` to match the runtime you are using.
functions/pyproject.toml```

requires-python = "==3.11.*"

```

You can refer to [this example of deploying a Python function](https://sst.dev/docs/examples/#aws-lambda-python).

##### [Golang](https://sst.dev/docs/component/aws/function#golang)

For Golang the handler looks like.

```

{

handler: "packages/functions/go/some_module"

}

```

Where `packages/functions/go/some_module` is the path to the Go module. This includes the name of the module in your `go.mod`. So in this case your `go.mod` might be in `packages/functions/go` and `some_module` is the name of the module.
You can refer to [this example of deploying a Go function](https://sst.dev/docs/examples/#aws-lambda-go).

##### [Rust](https://sst.dev/docs/component/aws/function#rust)

For Rust, the handler looks like.

```

{

handler: "crates/api"

}

```

Where `crates/api` is the path to the Rust crate. This means there is a `Cargo.toml` file in `crates/api`, and the main() function handles the lambda.

### [hook?](https://sst.dev/docs/component/aws/function#hook)

**Type** `Object`

* [`postbuild`](https://sst.dev/docs/component/aws/function#hook-postbuild)

Hook into the Lambda function build process.

#### [hook.postbuild](https://sst.dev/docs/component/aws/function#hook-postbuild)

```

postbuild(dir)

```

**Parameters**

* `dir` `string`
The directory where the function code is generated.

**Returns** `Promise``<``void``>`
Specify a callback that’ll be run after the Lambda function is built.
This is not called in `sst dev`.
Useful for modifying the generated Lambda function code before it’s deployed to AWS. It can also be used for uploading the generated sourcemaps to a service like Sentry.

### [layers?](https://sst.dev/docs/component/aws/function#layers)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of Lambda layer ARNs to add to the function.
Layers are only added when the function is deployed.
These are only added when the function is deployed. In `sst dev`, your functions are run locally, so the layers are not used. Instead you should use a local version of what’s in the layer.

```

{

layers: ["arn:aws:lambda:us-east-1:123456789012:layer:my-layer:1"]

}

```

### [link?](https://sst.dev/docs/component/aws/function#link)

**Type** `Input``<``any``[]``>`
[Link resources](https://sst.dev/docs/linking/) to your function. This will:

  1. Grant the permissions needed to access the resources.
  2. Allow you to access it in your function using the [SDK](https://sst.dev/docs/reference/sdk/).

Takes a list of components to link to the function.

```

{

link: [bucket, stripeKey]

}

```

### [logging?](https://sst.dev/docs/component/aws/function#logging)

**Type** `Input``<``false`` | ``Object``>`

* [`format?`](https://sst.dev/docs/component/aws/function#logging-format)
* [`logGroup?`](https://sst.dev/docs/component/aws/function#logging-loggroup)
* [`retention?`](https://sst.dev/docs/component/aws/function#logging-retention)

**Default** `{retention: “1 month”, format: “text”}`
Configure the function logs in CloudWatch. Or pass in `false` to disable writing logs.

```

{

logging: false

}

```

When set to `false`, the function is not given permissions to write to CloudWatch. Logs.

#### [logging.format?](https://sst.dev/docs/component/aws/function#logging-format)

**Type** `Input``<``“``json``”`` | ``“``text``”``>`
**Default** `“text”`
The

```

{

logging: {

format: "json"

}

}

```

#### [logging.logGroup?](https://sst.dev/docs/component/aws/function#logging-loggroup)

**Type** `Input``<``string``>`
**Default** Creates a log group
Assigns the given CloudWatch log group name to the function. This allows you to pass in a previously created log group.
By default, the function creates a new log group when it’s created.

```

{

logging: {

logGroup: "/existing/log-group"

}

}

```

#### [logging.retention?](https://sst.dev/docs/component/aws/function#logging-retention)

**Type** `Input``<``“``1 day``”`` | ``“``3 days``”`` | ``“``5 days``”`` | ``“``1 week``”`` | ``“``2 weeks``”`` | ``“``1 month``”`` | ``“``2 months``”`` | ``“``3 months``”`` | ``“``4 months``”`` | ``“``5 months``”`` | ``“``6 months``”`` | ``“``1 year``”`` | ``“``13 months``”`` | ``“``18 months``”`` | ``“``2 years``”`` | ``“``3 years``”`` | ``“``5 years``”`` | ``“``6 years``”`` | ``“``7 years``”`` | ``“``8 years``”`` | ``“``9 years``”`` | ``“``10 years``”`` | ``“``forever``”``>`
**Default** `1 month`
The duration the function logs are kept in CloudWatch.
Not application when an existing log group is provided.

```

{

logging: {

retention: "forever"

}

}

```

### [memory?](https://sst.dev/docs/component/aws/function#memory)

**Type** `Input``<``“``${number} MB``”`` | ``“``${number} GB``”``>`
**Default** `“1024 MB”`
The amount of memory allocated for the function. Takes values between 128 MB and 10240 MB in 1 MB increments. The amount of memory affects the amount of virtual CPU available to the function.
While functions with less memory are cheaper, larger functions can process faster. And might end up being more

```

{

memory: "10240 MB"

}

```

### [name?](https://sst.dev/docs/component/aws/function#name)

**Type** `Input``<``string``>`
The name for the function.
By default, the name is generated from the app name, stage name, and component name. This is displayed in the AWS Console for this function.
To avoid the name from thrashing, you want to make sure that it includes the app and stage name.
If you are going to set the name, you need to make sure:

  1. It’s unique across your app.
  2. Uses the app and stage name, so it doesn’t thrash when you deploy to different stages.

Also, changing the name after your’ve deployed it once will create a new function and delete the old one.

```

{

name: `${$app.name}-${$app.stage}-my-function`

}

```

### [nodejs?](https://sst.dev/docs/component/aws/function#nodejs-1)

**Type** `Input``<``Object``>`

* [`banner?`](https://sst.dev/docs/component/aws/function#nodejs-banner)
* [`esbuild?`](https://sst.dev/docs/component/aws/function#nodejs-esbuild)
* [`format?`](https://sst.dev/docs/component/aws/function#nodejs-format)
* [`install?`](https://sst.dev/docs/component/aws/function#nodejs-install)
* [`loader?`](https://sst.dev/docs/component/aws/function#nodejs-loader)
* [`minify?`](https://sst.dev/docs/component/aws/function#nodejs-minify)
* [`sourcemap?`](https://sst.dev/docs/component/aws/function#nodejs-sourcemap)
* [`splitting?`](https://sst.dev/docs/component/aws/function#nodejs-splitting)

Configure how your function is bundled.
By default, SST will bundle your function code using

#### [nodejs.banner?](https://sst.dev/docs/component/aws/function#nodejs-banner)

**Type** `Input``<``string``>`
Use this to insert a string at the beginning of the generated JS file.

```

{

nodejs: {

banner: "console.log('Function starting')"

}

}

```

#### [nodejs.esbuild?](https://sst.dev/docs/component/aws/function#nodejs-esbuild)

**Type** `Input``<``>`
This allows you to customize esbuild config that is used.
Check out the _JS tab_ in the code snippets in the esbuild docs for the

#### [nodejs.format?](https://sst.dev/docs/component/aws/function#nodejs-format)

**Type** `Input``<``“``cjs``”`` | ``“``esm``”``>`
**Default** `“esm”`
Configure the format of the generated JS code; ESM or CommonJS.

```

{

nodejs: {

format: "cjs"

}

}

```

#### [nodejs.install?](https://sst.dev/docs/component/aws/function#nodejs-install)

**Type** `Input``<``string``[]``>`
Dependencies that need to be excluded from the function package.
Certain npm packages cannot be bundled using esbuild. This allows you to exclude them from the bundle. Instead they’ll be moved into a `node_modules/` directory in the function package.
If esbuild is giving you an error about a package, try adding it to the `install` list.
This will allow your functions to be able to use these dependencies when deployed. They just won’t be tree shaken. You however still need to have them in your `package.json`.
Packages listed here still need to be in your `package.json`.
Esbuild will ignore them while traversing the imports in your code. So these are the **package names as seen in the imports**. It also works on packages that are not directly imported by your code.

```

{

nodejs: {

install: ["pg"]

}

}

```

#### [nodejs.loader?](https://sst.dev/docs/component/aws/function#nodejs-loader)

**Type** `Input``<``Record``<``string`, `>``>`
Configure additional esbuild loaders for other file extensions. This is useful when your code is importing non-JS files like `.png`, `.css`, etc.

```

{

nodejs: {

loader: {

".png": "file"

}

}

}

```

#### [nodejs.minify?](https://sst.dev/docs/component/aws/function#nodejs-minify)

**Type** `Input``<``boolean``>`
**Default** `true`
Disable if the function code is minified when bundled.

```

{

nodejs: {

minify: false

}

}

```

#### [nodejs.sourcemap?](https://sst.dev/docs/component/aws/function#nodejs-sourcemap)

**Type** `Input``<``boolean``>`
**Default** `false`
Configure if source maps are added to the function bundle when **deployed**. Since they increase payload size and potentially cold starts, they are not added by default. However, they are always generated during `sst dev`.
For the [Console](https://sst.dev/docs/console/), source maps are always generated and uploaded to your bootstrap bucket. These are then downloaded and used to display Issues in the console.

```

{

nodejs: {

sourcemap: true

}

}

```

#### [nodejs.splitting?](https://sst.dev/docs/component/aws/function#nodejs-splitting)

**Type** `Input``<``boolean``>`
**Default** `false`
If enabled, modules that are dynamically imported will be bundled in their own files with common dependencies placed in shared chunks. This can help reduce cold starts as your function grows in size.

```

{

nodejs: {

splitting: true

}

}

```

### [permissions?](https://sst.dev/docs/component/aws/function#permissions)

**Type** `Input``<``Object``[]``>`

* [`actions`](https://sst.dev/docs/component/aws/function#permissions-actions)
* [`effect?`](https://sst.dev/docs/component/aws/function#permissions-effect)
* [`resources`](https://sst.dev/docs/component/aws/function#permissions-resources)

Permissions and the resources that the function needs to access. These permissions are used to create the function’s IAM role.
If you `link` the function to a resource, the permissions to access it are automatically added.
Allow the function to read and write to an S3 bucket called `my-bucket`.

```

{

permissions: [

{

actions: ["s3:GetObject", "s3:PutObject"],

resources: ["arn:aws:s3:::my-bucket/*"]

}

]

}

```

Allow the function to perform all actions on an S3 bucket called `my-bucket`.

```

{

permissions: [

{

actions: ["s3:*"],

resources: ["arn:aws:s3:::my-bucket/*"]

}

]

}

```

Granting the function permissions to access all resources.

```

{

permissions: [

{

actions: ["*"],

resources: ["*"]

}

]

}

```

#### [permissions[].actions](https://sst.dev/docs/component/aws/function#permissions-actions)

**Type** `string``[]`
The

```

{

actions: ["s3:*"]

}

```

#### [permissions[].effect?](https://sst.dev/docs/component/aws/function#permissions-effect)

**Type** `“``allow``”`` | ``“``deny``”`
**Default** `“allow”`
Configures whether the permission is allowed or denied.

```

{

effect: "deny"

}

```

#### [permissions[].resources](https://sst.dev/docs/component/aws/function#permissions-resources)

**Type** `Input``<``Input``<``string``>``[]``>`
The resourcess specified using the

```

{

resources: ["arn:aws:s3:::my-bucket/*"]

}

```

### [policies?](https://sst.dev/docs/component/aws/function#policies)

**Type** `Input``<``string``[]``>`
Policies to attach to the function. These policies will be added to the function’s IAM role.
Attaching policies lets you grant a set of predefined permissions to the function without having to specify the permissions in the `permissions` prop.
For example, allow the function to have read-only access to all resources.

```

{

policies: ["arn:aws:iam::aws:policy/ReadOnlyAccess"]

}

```

### [python?](https://sst.dev/docs/component/aws/function#python-1)

**Type** `Input``<``Object``>`

* [`container?`](https://sst.dev/docs/component/aws/function#python-container)

Configure how your Python function is packaged.

#### [python.container?](https://sst.dev/docs/component/aws/function#python-container)

**Type** `Input``<``boolean``>`
**Default** `false`
Set this to `true` if you want to deploy this function as a container image. There are a couple of reasons why you might want to do this.

  1. The Lambda package size has an unzipped limit of 250MB. Whereas the container image size has a limit of 10GB.
  2. Even if you are below the 250MB limit, larger Lambda function packages have longer cold starts when compared to container image.
  3. You might want to use a custom Dockerfile to handle complex builds.

```

{

python: {

container: true

}

}

```

When you run `sst deploy`, it uses a built-in Dockerfile. It also needs the Docker daemon to be running.
This needs the Docker daemon to be running.
To use a custom Dockerfile, add one to the rooot of the uv workspace of the function.

```

├── sst.config.ts

├── pyproject.toml

└── function

├── pyproject.toml

├── Dockerfile

└── src

└── function

└── api.py

```

You can refer to [this example of using a container image](https://sst.dev/docs/examples/#aws-lambda-python-container).

### [retries?](https://sst.dev/docs/component/aws/function#retries)

**Type** `Input``<``number``>`
**Default** `2`
Configure the maximum number of retry attempts for this function when invoked asynchronously.
This only affects asynchronous invocations of the function, ie. when subscribed to Topics, EventBuses, or Buckets. And not when directly invoking the function.
Valid values are between 0 and 2.

```

{

retries: 0

}

```

### [role?](https://sst.dev/docs/component/aws/function#role)

**Type** `Input``<``string``>`
**Default** Creates a new role
Assigns the given IAM role ARN to the function. This allows you to pass in a previously created role.
When you pass in a role, the function will not update it if you add `permissions` or `link` resources.
By default, the function creates a new IAM role when it’s created. It’ll update this role if you add `permissions` or `link` resources.
However, if you pass in a role, you’ll need to update it manually if you add `permissions` or `link` resources.

```

{

role: "arn:aws:iam::123456789012:role/my-role"

}

```

### [runtime?](https://sst.dev/docs/component/aws/function#runtime)

**Type** `Input``<``“``nodejs18.x``”`` | ``“``nodejs20.x``”`` | ``“``nodejs22.x``”`` | ``“``go``”`` | ``“``rust``”`` | ``“``provided.al2023``”`` | ``“``python3.9``”`` | ``“``python3.10``”`` | ``“``python3.11``”`` | ``“``python3.12``”``>`
**Default** `“nodejs20.x”`
The language runtime for the function.
Node.js and Golang are officially supported. While, Python and Rust are community supported. Support for other runtimes are on the roadmap.

```

{

runtime: "nodejs22.x"

}

```

### [storage?](https://sst.dev/docs/component/aws/function#storage)

**Type** `Input``<``“``${number} MB``”`` | ``“``${number} GB``”``>`
**Default** `“512 MB”`
The amount of ephemeral storage allocated for the function. This sets the ephemeral storage of the lambda function (/tmp). Must be between “512 MB” and “10240 MB” (“10 GB”) in 1 MB increments.

```

{

storage: "5 GB"

}

```

### [streaming?](https://sst.dev/docs/component/aws/function#streaming)

**Type** `Input``<``boolean``>`
**Default** `false`
Enable streaming for the function.
Streaming is only supported when using the function `url` is enabled and not when using it with API Gateway.
You’ll also need to `awslambda.streamifyResponse` to enable streaming.
Streaming is currently not supported in `sst dev`.
While `sst dev` doesn’t support streaming, you can use the
Check out the [AWS Lambda streaming example](https://sst.dev/docs/examples/#aws-lambda-streaming) for more details.

```

{

streaming: true

}

```

### [tags?](https://sst.dev/docs/component/aws/function#tags)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
A list of tags to add to the function.

```

{

tags: {

"my-tag": "my-value"

}

}

```

### [timeout?](https://sst.dev/docs/component/aws/function#timeout)

**Type** `Input``<``“``${number} minute``”`` | ``“``${number} minutes``”`` | ``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“20 seconds”`
The maximum amount of time the function can run. The minimum timeout is 1 second and the maximum is 900 seconds or 15 minutes.
If a function is connected to another service, the request will time out based on the service’s limits.
While the maximum timeout is 15 minutes, if a function is connected to other services, it’ll time out based on those limits.

* API Gateway has a timeout of 30 seconds. So even if the function has a timeout of 15 minutes, the API request will time out after 30 seconds.
* CloudFront has a default timeout of 60 seconds. You can have this limit increased by

```

{

timeout: "900 seconds"

}

```

### [transform?](https://sst.dev/docs/component/aws/function#transform)

**Type** `Object`

* [`eventInvokeConfig?`](https://sst.dev/docs/component/aws/function#transform-eventinvokeconfig)
* [`function?`](https://sst.dev/docs/component/aws/function#transform-function)
* [`logGroup?`](https://sst.dev/docs/component/aws/function#transform-loggroup)
* [`role?`](https://sst.dev/docs/component/aws/function#transform-role)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.eventInvokeConfig?](https://sst.dev/docs/component/aws/function#transform-eventinvokeconfig)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Function Event Invoke Config resource. This is only created when the `retries` property is set.

#### [transform.function?](https://sst.dev/docs/component/aws/function#transform-function)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Lambda Function resource.

#### [transform.logGroup?](https://sst.dev/docs/component/aws/function#transform-loggroup)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the CloudWatch LogGroup resource.

#### [transform.role?](https://sst.dev/docs/component/aws/function#transform-role)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the IAM Role resource.

### [url?](https://sst.dev/docs/component/aws/function#url)

**Type** `Input``<``boolean`` | ``Object``>`

* [`authorization?`](https://sst.dev/docs/component/aws/function#url-authorization)
* [`cors?`](https://sst.dev/docs/component/aws/function#url-cors) `Input``<``boolean`` | ``Object``>`
  * [`allowCredentials?`](https://sst.dev/docs/component/aws/function#url-cors-allowcredentials)
  * [`allowHeaders?`](https://sst.dev/docs/component/aws/function#url-cors-allowheaders)
  * [`allowMethods?`](https://sst.dev/docs/component/aws/function#url-cors-allowmethods)
  * [`allowOrigins?`](https://sst.dev/docs/component/aws/function#url-cors-alloworigins)
  * [`exposeHeaders?`](https://sst.dev/docs/component/aws/function#url-cors-exposeheaders)
  * [`maxAge?`](https://sst.dev/docs/component/aws/function#url-cors-maxage)
* [`router?`](https://sst.dev/docs/component/aws/function#url-router) `Object`
  * [`domain?`](https://sst.dev/docs/component/aws/function#url-router-domain)
  * [`instance`](https://sst.dev/docs/component/aws/function#url-router-instance)
  * [`path?`](https://sst.dev/docs/component/aws/function#url-router-path)

**Default** `false`
Enable
Enable it with the default options.

```

{

url: true

}

```

Configure the authorization and CORS settings for the endpoint.

```

{

url: {

authorization: "iam",

cors: {

allowOrigins: ['https://example.com']

}

}

}

```

#### [url.authorization?](https://sst.dev/docs/component/aws/function#url-authorization)

**Type** `Input``<``“``none``”`` | ``“``iam``”``>`
**Default** `“none”`
The authorization used for the function URL. Supports

```

{

url: {

authorization: "iam"

}

}

```

#### [url.cors?](https://sst.dev/docs/component/aws/function#url-cors)

**Type** `Input``<``boolean`` | ``Object``>`
**Default** `true`
Customize the CORS (Cross-origin resource sharing) settings for the function URL.
Disable CORS.

```

{

url: {

cors: false

}

}

```

Only enable the `GET` and `POST` methods for `https://example.com`.

```

{

url: {

cors: {

allowMethods: ["GET", "POST"],

allowOrigins: ["https://example.com"]

}

}

}

```

##### [url.cors.allowCredentials?](https://sst.dev/docs/component/aws/function#url-cors-allowcredentials)

**Type** `Input``<``boolean``>`
**Default** `false`
Allow cookies or other credentials in requests to the function URL.

```

{

url: {

cors: {

allowCredentials: true

}

}

}

```

##### [url.cors.allowHeaders?](https://sst.dev/docs/component/aws/function#url-cors-allowheaders)

**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `[”*”]`
The HTTP headers that origins can include in requests to the function URL.

```

{

url: {

cors: {

allowHeaders: ["date", "keep-alive", "x-custom-header"]

}

}

}

```

##### [url.cors.allowMethods?](https://sst.dev/docs/component/aws/function#url-cors-allowmethods)

**Type** `Input``<``Input``<``“``GET``”`` | ``“``POST``”`` | ``“``PUT``”`` | ``“``DELETE``”`` | ``“``HEAD``”`` | ``“``OPTIONS``”`` | ``“``PATCH``”`` | ``“``*``”``>``[]``>`
**Default** `[”*”]`
The HTTP methods that are allowed when calling the function URL.

```

{

url: {

cors: {

allowMethods: ["GET", "POST", "DELETE"]

}

}

}

```

Or the wildcard for all methods.

```

{

url: {

cors: {

allowMethods: ["*"]

}

}

}

```

##### [url.cors.allowOrigins?](https://sst.dev/docs/component/aws/function#url-cors-alloworigins)

**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `[”*”]`
The origins that can access the function URL.

```

{

url: {

cors: {

allowOrigins: ["https://www.example.com", "http://localhost:60905"]

}

}

}

```

Or the wildcard for all origins.

```

{

url: {

cors: {

allowOrigins: ["*"]

}

}

}

```

##### [url.cors.exposeHeaders?](https://sst.dev/docs/component/aws/function#url-cors-exposeheaders)

**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `[]`
The HTTP headers you want to expose in your function to an origin that calls the function URL.

```

{

url: {

cors: {

exposeHeaders: ["date", "keep-alive", "x-custom-header"]

}

}

}

```

##### [url.cors.maxAge?](https://sst.dev/docs/component/aws/function#url-cors-maxage)

**Type** `Input``<``“``${number} minute``”`` | ``“``${number} minutes``”`` | ``“``${number} hour``”`` | ``“``${number} hours``”`` | ``“``${number} second``”`` | ``“``${number} seconds``”`` | ``“``${number} day``”`` | ``“``${number} days``”``>`
**Default** `“0 seconds”`
The maximum amount of time the browser can cache results of a preflight request. By default the browser doesn’t cache the results. The maximum value is `86400 seconds` or `1 day`.

```

{

url: {

cors: {

maxAge: "1 day"

}

}

}

```

#### [url.router?](https://sst.dev/docs/component/aws/function#url-router)

**Type** `Object`
Serve your function URL through a `Router` instead of a standalone Function URL.
By default, this component creates a direct function URL endpoint. But you might want to serve it through the distribution of your `Router` as a:

* A path like `/api/users`
* A subdomain like `api.example.com`
* Or a combined pattern like `dev.example.com/api`

To serve your function **from a path** , you’ll need to configure the root domain in your `Router` component.
sst.config.ts
```typescript

const router = newsst.aws.Router("Router", {

"example.com"

});

```

Now set the `router` and the `path` in the `url` prop.

```

{

url: {

router: {

instance: router,

path: "/api/users"

}

}

}

```

To serve your function **from a subdomain** , you’ll need to configure the domain in your `Router` component to match both the root and the subdomain.
sst.config.ts

```typescript


const router = newsst.aws.Router("Router", {



domain: {



"example.com",




 ["*.example.com"]



}



});


```

Now set the `domain` in the `router` prop.

```

{


url: {


router: {


instance: router,



domain: "api.example.com"



}


}


}

```

Finally, to serve your function **from a combined pattern** like `dev.example.com/api`, you’ll need to configure the domain in your `Router` to match the subdomain.
sst.config.ts

```typescript

const router = newsst.aws.Router("Router", {

domain: {

"example.com",

 ["*.example.com"]

}

});

```

And set the `domain` and the `path`.

```

{

url: {

router: {

instance: router,

domain: "dev.example.com",

path: "/api/users"

}

}

}

```

##### [url.router.domain?](https://sst.dev/docs/component/aws/function#url-router-domain)

**Type** `Input``<``string``>`
Route requests matching a specific domain pattern.
You can serve your resource from a subdomain. For example, if you want to make it available at `https://dev.example.com`, set the `Router` to match the domain or a wildcard.
sst.config.ts

```typescript


const router = newsst.aws.Router("MyRouter", {




"*.example.com"




});


```

Then set the domain pattern.

```

router: {


instance: router,



domain: "dev.example.com"



}

```

While `dev.example.com` matches `*.example.com`. Something like `docs.dev.example.com` will not match `*.example.com`.
Nested wildcards domain patterns are not supported.
You’ll need to add `*.dev.example.com` as an alias.

##### [url.router.instance](https://sst.dev/docs/component/aws/function#url-router-instance)

**Type** `Input``<`[`Router`](https://sst.dev/docs/component/aws/router)`>`
The `Router` component to use for routing requests.
Let’s say you have a Router component.
sst.config.ts

```typescript

const router = newsst.aws.Router("MyRouter", {

domain: "example.com"

});

```

You can attach it to the Router, instead of creating a standalone CloudFront distribution.

```

router: {

instance: router

}

```

##### [url.router.path?](https://sst.dev/docs/component/aws/function#url-router-path)

**Type** `Input``<``string``>`
**Default** `”/”`
Route requests matching a specific path prefix.

```

router: {

instance: router,

path: "/docs"

}

```

### [versioning?](https://sst.dev/docs/component/aws/function#versioning)

**Type** `Input``<``boolean``>`
**Default** `false`
Enable versioning for the function.

```

{

versioning: true

}

```

### [volume?](https://sst.dev/docs/component/aws/function#volume)

**Type** `Input``<``Object``>`

* [`efs`](https://sst.dev/docs/component/aws/function#volume-efs)
* [`path?`](https://sst.dev/docs/component/aws/function#volume-path)

Mount an EFS file system to the function.
Create an EFS file system.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc");




const fileSystem = newsst.aws.Efs("MyFileSystem", { vpc });


```

And pass it in.

```

{


volume: {



efs: fileSystem



}


}

```

By default, the file system will be mounted to `/mnt/efs`. You can change this by passing in the `path` property.

```

{


volume: {



efs: fileSystem,




path: "/mnt/my-files"



}


}

```

To use an existing EFS, you can pass in an EFS access point ARN.

```

{


volume: {



efs: "arn:aws:elasticfilesystem:us-east-1:123456789012:access-point/fsap-12345678",



}


}

```

#### [volume.efs](https://sst.dev/docs/component/aws/function#volume-efs)

**Type** `Input``<``string`` |`[`Efs`](https://sst.dev/docs/component/aws/efs)`>`
The EFS file system to mount. Or an EFS access point ARN.

#### [volume.path?](https://sst.dev/docs/component/aws/function#volume-path)

**Type** `Input``<``string``>`
**Default** `“/mnt/efs”`
The path to mount the volume.

### [vpc?](https://sst.dev/docs/component/aws/function#vpc)

**Type** [`Vpc`](https://sst.dev/docs/component/aws/vpc)`| ``Input``<``Object``>`

* [`privateSubnets`](https://sst.dev/docs/component/aws/function#vpc-privatesubnets)
* [`securityGroups`](https://sst.dev/docs/component/aws/function#vpc-securitygroups)

Configure the function to connect to private subnets in a virtual private cloud or VPC. This allows your function to access private resources.
Create a `Vpc` component.
sst.config.ts

```typescript

const myVpc = newsst.aws.Vpc("MyVpc");

```

Or reference an existing VPC.
sst.config.ts

```typescript


const myVpc = sst.aws.Vpc.get("MyVpc", {




id: "vpc-12345678901234567"




});


```

And pass it in.

```

{



vpc: myVpc



}

```

#### [vpc.privateSubnets](https://sst.dev/docs/component/aws/function#vpc-privatesubnets)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of VPC subnet IDs.

#### [vpc.securityGroups](https://sst.dev/docs/component/aws/function#vpc-securitygroups)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of VPC security group IDs.

## [Properties](https://sst.dev/docs/component/aws/function#properties)

### [arn](https://sst.dev/docs/component/aws/function#arn)

**Type** `Output``<``string``>`
The ARN of the Lambda function.

### [name](https://sst.dev/docs/component/aws/function#name-1)

**Type** `Output``<``string``>`
The name of the Lambda function.

### [nodes](https://sst.dev/docs/component/aws/function#nodes)

**Type** `Object`

* [`eventInvokeConfig`](https://sst.dev/docs/component/aws/function#nodes-eventinvokeconfig)
* [`function`](https://sst.dev/docs/component/aws/function#nodes-function)
* [`logGroup`](https://sst.dev/docs/component/aws/function#nodes-loggroup)
* [`role`](https://sst.dev/docs/component/aws/function#nodes-role)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.eventInvokeConfig](https://sst.dev/docs/component/aws/function#nodes-eventinvokeconfig)

**Type** `undefined`` |`
The Function Event Invoke Config resource if retries are configured.

#### [nodes.function](https://sst.dev/docs/component/aws/function#nodes-function)

**Type** `Output``<``>`
The AWS Lambda function.

#### [nodes.logGroup](https://sst.dev/docs/component/aws/function#nodes-loggroup)

**Type** `Output``<``undefined`` | ``>`
The CloudWatch Log Group the function logs are stored.

#### [nodes.role](https://sst.dev/docs/component/aws/function#nodes-role)

**Type**
The IAM Role the function will use.

### [url](https://sst.dev/docs/component/aws/function#url-1)

**Type** `Output``<``string``>`
The Lambda function URL if `url` is enabled.

## [SDK](https://sst.dev/docs/component/aws/function#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/function#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `name` `string`
The name of the Lambda function.
* `url` `undefined`` | ``string`
The Lambda function URL if `url` is enabled.

## [Methods](https://sst.dev/docs/component/aws/function#methods)

### [addEnvironment](https://sst.dev/docs/component/aws/function#addenvironment)

```


addEnvironment(environment)


```

#### [Parameters](https://sst.dev/docs/component/aws/function#parameters-1)

* `environment` `Input``<``Record``<``string`, `Input``<``string``>``>``>`
The environment variables to add to the function.

**Returns** [`FunctionEnvironmentUpdate`](https://sst.dev/docs/component/aws/providers/function-environment-update)
Add environment variables lazily to the function after the function is created.
This is useful for adding environment variables that are only available after the function is created, like the function URL.
Add the function URL as an environment variable.
sst.config.ts

```typescript

const fn = newsst.aws.Function("MyFunction", {

handler: "src/handler.handler",

url: true,

});

fn.addEnvironment({

URL: fn.url,

});

```

[Skip to content](https://sst.dev/docs/examples#_top)

# Examples

Below is a collection of example SST apps. These are available in the
This doc is best viewed through the site search or through the _AI_.
The descriptions for these examples are generated using the comments in the `sst.config.ts` of the app.

#### [Contributing](https://sst.dev/docs/examples#contributing)

To contribute an example or to edit one, submit a PR to the `sst.config.ts` in your example.
* * *

## [API Gateway auth](https://sst.dev/docs/examples#api-gateway-auth)

Enable IAM and JWT authorizers for API Gateway routes.
sst.config.ts

```typescript


const api = newsst.aws.ApiGatewayV2("MyApi", {



domain: {



name: "api.ion.sst.sh",




path: "v1",



},



});




api.route("GET /", {




handler: "route.handler",



});



api.route("GET /foo", "route.handler", { auth: { iam: true } });




api.route("GET /bar", "route.handler", {



auth: {


jwt: {


issuer:



"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_Rq4d8zILG",




audiences: ["user@example.com"],



},


},


});



api.route("$default", "route.handler");




return {




api: api.url,



};

```

View the
* * *

## [AWS Astro container with Redis](https://sst.dev/docs/examples#aws-astro-container-with-redis)

Creates a hit counter app with Astro and Redis.
This deploys Astro as a Fargate service to ECS and it’s linked to Redis.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

cluster,

link: [redis],

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "npm run dev",

},

});

```

Since our Redis cluster is in a VPC, we’ll need a tunnel to connect to it from our local machine.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
To start your app locally run.
Terminal window```

npxsstdev

```

Now if you go to `http://localhost:4321` you’ll see a counter update as you refresh the page.
Finally, you can deploy it by adding the `Dockerfile` that’s included in this example and running `npx sst deploy --stage production`.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });




const redis = newsst.aws.Redis("MyRedis", { vpc });




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


link: [redis],


loadBalancer: {



ports: [{ listen: "80/http", forward: "4321/http" }],



},


dev: {



command: "npm run dev",



},


});

```

View the
* * *

## [AWS Astro streaming](https://sst.dev/docs/examples#aws-astro-streaming)

Follows the
The `responseMode` in the
astro.config.mjs```

adapter: aws({

responseMode: "stream"

})

```

Now any components that return promises will be streamed.
src/components/Friends.astro```

---



importtype { Character } from"./character";




const friends:Character[] = await newPromise((resolve) => setTimeout(() => {




setTimeout(() => {




resolve(



[



{ name: "Patrick Star", image: "patrick.png" },




{ name: "Sandy Cheeks", image: "sandy.png" },




{ name: "Squidward Tentacles", image: "squidward.png" },




{ name: "Mr. Krabs", image: "mr-krabs.png" },



]



);




}, 3000);




}));



---



<divclass="grid">




{friends.map((friend)=> (




<divclass="card">




<imgclass="img"src={friend.image}alt={friend.name} />




<p>{friend.name}</p>



</div>



))}



</div>

```

You should see the _friends_ section load after a 3 second delay.
Safari handles streaming differently than other browsers.
Safari uses a _enough_ initial HTML to trigger streaming. This is typically only a problem for demo apps.
There’s nothing to configure for streaming in the `Astro` component.
sst.config.ts

```typescript

new sst.aws.Astro("MyWeb");

```

View the
* * *

## [AWS Aurora local](https://sst.dev/docs/examples#aws-aurora-local)

In this example, we connect to a locally running Postgres instance for dev. While on deploy, we use RDS Aurora.
We use the
Terminal window```

dockerrun\

--rm\

-p5432:5432\

-v $(pwd)/.sst/storage/postgres:/var/lib/postgresql/data\

-ePOSTGRES_USER=postgres\

-ePOSTGRES_PASSWORD=password\

-ePOSTGRES_DB=local\

postgres:16.4

```

The data is saved to the `.sst/storage` directory. So if you restart the dev server, the data will still be there.
We then configure the `dev` property of the `Aurora` component with the settings for the local Postgres instance.
sst.config.ts
```typescript

dev: {

username: "postgres",

password: "password",

database: "local",

port: 5432,

}

```

By providing the `dev` prop for Postgres, SST will use the local Postgres instance and not deploy a new RDS database when running `sst dev`.
It also allows us to access the database through a Resource `link` without having to conditionally check if we are running locally.
index.ts

```typescript


const pool = newPool({




host: Resource.MyPostgres.host,




port: Resource.MyPostgres.port,




user: Resource.MyPostgres.username,




password: Resource.MyPostgres.password,




database: Resource.MyPostgres.database,




});


```

The above will work in both `sst dev` and `sst deploy`.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc", { nat: "ec2" });

const database = newsst.aws.Aurora("MyPostgres", {

engine: "postgres",

dev: {

username: "postgres",

password: "password",

database: "local",

host: "localhost",

port: 5432,

},

vpc,

});

new sst.aws.Function("MyFunction", {

vpc,

url: true,

link: [database],

handler: "index.handler",

});

```

View the
* * *

## [AWS Aurora MySQL](https://sst.dev/docs/examples#aws-aurora-mysql)

In this example, we deploy a Aurora MySQL database.
sst.config.ts

```typescript


const mysql = newsst.aws.Aurora("MyDatabase", {




engine: "mysql",




vpc,




});


```

And link it to a Lambda function.
sst.config.ts

```typescript

new sst.aws.Function("MyApp", {

handler: "index.handler",

link: [mysql],

url: true,

vpc,

});

```

Now in the function we can access the database.
index.ts

```typescript


const connection = await mysql.createConnection({




database: Resource.MyDatabase.database,




host: Resource.MyDatabase.host,




port: Resource.MyDatabase.port,




user: Resource.MyDatabase.username,




password: Resource.MyDatabase.password,




});


```

We also enable the `bastion` option for the VPC. This allows us to connect to the database from our local machine with the `sst tunnel` CLI.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
Now you can run `npx sst dev` and you can connect to the database from your local machine.
sst.config.ts
```typescript


const vpc = newsst.aws.Vpc("MyVpc", {




nat: "ec2",




bastion: true,




});




const mysql = newsst.aws.Aurora("MyDatabase", {




engine: "mysql",




vpc,




});




new sst.aws.Function("MyApp", {




handler: "index.handler",



link: [mysql],



url: true,



vpc,


});



return {




host: mysql.host,




port: mysql.port,




username: mysql.username,




password: mysql.password,




database: mysql.database,



};

```

View the
* * *

## [AWS Aurora Postgres](https://sst.dev/docs/examples#aws-aurora-postgres)

In this example, we deploy a Aurora Postgres database.
sst.config.ts

```typescript

const postgres = newsst.aws.Aurora("MyDatabase", {

engine: "postgres",

vpc,

});

```

And link it to a Lambda function.
sst.config.ts

```typescript


new sst.aws.Function("MyApp", {




handler: "index.handler",



link: [postgres],



url: true,



vpc,


});

```

In the function we use the
index.ts

```typescript

import postgres from"postgres";

import { Resource } from"sst";

const sql = postgres({

username: Resource.MyDatabase.username,

password: Resource.MyDatabase.password,

database: Resource.MyDatabase.database,

host: Resource.MyDatabase.host,

port: Resource.MyDatabase.port,

});

```

We also enable the `bastion` option for the VPC. This allows us to connect to the database from our local machine with the `sst tunnel` CLI.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
Now you can run `npx sst dev` and you can connect to the database from your local machine.
sst.config.ts
```typescript

const vpc = newsst.aws.Vpc("MyVpc", {

nat: "ec2",

bastion: true,

});

const postgres = newsst.aws.Aurora("MyDatabase", {

engine: "postgres",

vpc,

});

new sst.aws.Function("MyApp", {

handler: "index.handler",

link: [postgres],

url: true,

vpc,

});

return {

host: postgres.host,

port: postgres.port,

username: postgres.username,

password: postgres.password,

database: postgres.database,

};

```

View the
* * *

## [AWS OpenAuth React SPA](https://sst.dev/docs/examples#aws-openauth-react-spa)

This is a full-stack monorepo app shows the OpenAuth flow for a single-page app and an authenticated API. It has:

* React SPA built with Vite and the `StaticSite` component in the `packages/web` directory.
infra/web.ts

```typescript


export const web = newsst.aws.StaticSite("MyWeb", {




path: "packages/web",



build: {



output: "dist",




command: "npm run build",



},


environment: {



VITE_API_URL: api.url,




VITE_AUTH_URL: auth.url,



},



});


```

* API with Hono and the `Function` component in `packages/functions/src/api.ts`.
infra/api.ts

```typescript

export const api = newsst.aws.Function("MyApi", {

url: true,

link: [auth],

handler: "packages/functions/src/api.handler",

});

```

* OpenAuth with the `Auth` component in `packages/functions/src/auth.ts`.
infra/auth.ts

```typescript


export const auth = newsst.aws.Auth("MyAuth", {




issuer: "packages/functions/src/auth.handler",




});


```

The React frontend uses a `AuthContext` provider to manage the auth flow.
packages/web/src/AuthContext.tsx```

<AuthContext.Provider

value={{

login,

logout,

userId,

loaded,

loggedIn,

getToken,

}}

>

{children}

</AuthContext.Provider>

```

Now in `App.tsx`, we can use the `useAuth` hook.
packages/web/src/App.tsx```


const auth = useAuth();




return!auth.loaded? (




<div>Loading...</div>




) : (



<div>



{auth.loggedIn? (



<div>


<p>



<span>Logged in</span>




{auth.userId&&<span> as {auth.userId}</span>}



</p>


</div>



) : (




<buttononClick={auth.login}>Login with OAuth</button>




)}



</div>


);

```

Once authenticated, we can call our authenticated API by passing in the access token.
packages/web/src/App.tsx```

awaitfetch(`${import.meta.env.VITE_API_URL}me`, {

headers: {

Authorization: `Bearer ${awaitauth.getToken()}`,

},

});

```

The API uses the OpenAuth client to verify the token.
packages/functions/src/api.ts
```typescript


const authHeader = c.req.header("Authorization");




const token = authHeader.split("")[1];




const verified = await client.verify(subjects, token);


```

The `sst.config.ts` dynamically imports all the `infra/` files.
sst.config.ts

```typescript

awaitimport("./infra/auth");

awaitimport("./infra/api");

awaitimport("./infra/web");

```

View the
* * *

## [Bucket policy](https://sst.dev/docs/examples#bucket-policy)

Create an S3 bucket and transform its bucket policy.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket", {



transform: {



policy: (args) => {



// use sst.aws.iamEdit helper function to manipulate IAM policy


// containing Output values from components



args.policy = sst.aws.iamEdit(args.policy, (policy) => {




policy.Statement.push({




Effect: "Allow",




Principal: { Service: "ses.amazonaws.com" },




Action: "s3:PutObject",




Resource: $interpolate`arn:aws:s3:::${args.bucket}/*`,




});




});



},


},



});




return {




bucket: bucket.name,



};

```

View the
* * *

## [Bucket queue notifications](https://sst.dev/docs/examples#bucket-queue-notifications)

Create an S3 bucket and subscribe to its events with an SQS queue.
sst.config.ts

```typescript

const queue = newsst.aws.Queue("MyQueue");

queue.subscribe("subscriber.handler");

const bucket = newsst.aws.Bucket("MyBucket");

bucket.notify({

notifications: [

{

name: "MySubscriber",

queue,

events: ["s3:ObjectCreated:*"],

},

],

});

return {

bucket: bucket.name,

queue: queue.url,

};

```

View the
* * *

## [Bucket notifications](https://sst.dev/docs/examples#bucket-notifications)

Create an S3 bucket and subscribe to its events with a function.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket");




bucket.notify({



notifications: [


{



name: "MySubscriber",




function: "subscriber.handler",




events: ["s3:ObjectCreated:*"],



},


],


});



return {




bucket: bucket.name,



};

```

View the
* * *

## [Bucket topic notifications](https://sst.dev/docs/examples#bucket-topic-notifications)

Create an S3 bucket and subscribe to its events with an SNS topic.
sst.config.ts

```typescript

const topic = newsst.aws.SnsTopic("MyTopic");

topic.subscribe("MySubscriber", "subscriber.handler");

const bucket = newsst.aws.Bucket("MyBucket");

bucket.notify({

notifications: [

{

name: "MySubscriber",

topic,

events: ["s3:ObjectCreated:*"],

},

],

});

return {

bucket: bucket.name,

topic: topic.name,

};

```

View the
* * *

## [AWS Bun Elysia container](https://sst.dev/docs/examples#aws-bun-elysia-container)

Deploys a Bun
You can get started by running.
Terminal window```

buncreateelysiaaws-bun-elysia

cdaws-bun-elysia

bunxsstinit

```

Now you can add a service.
sst.config.ts
```typescript

new sst.aws.Service("MyService", {

cluster,

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "bun dev",

},

});

```

Start your app locally.
Terminal window```

bunsstdev

```

This example lets you upload a file to S3 and then download it.
Terminal window```

curl-Ffile=@elysia.pnghttp://localhost:3000/

curlhttp://localhost:3000/latest

```

Finally, you can deploy it using `bun sst deploy --stage production`.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket");




const vpc = newsst.aws.Vpc("MyVpc");




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


loadBalancer: {



ports: [{ listen: "80/http", forward: "3000/http" }],



},


dev: {



command: "bun dev",



},


link: [bucket],


});

```

View the
* * *

## [AWS Bun Redis](https://sst.dev/docs/examples#aws-bun-redis)

Creates a hit counter app with Bun and Redis.
This deploys Bun as a Fargate service to ECS and it’s linked to Redis.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

cluster,

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "bun dev",

},

link: [redis],

});

```

We also have a couple of scripts. A `dev` script with a watcher and a `build` script that used when we deploy to production.
package.json```

{

"scripts": {

"dev": "bun run --watch index.ts",

"build": "bun build --target bun index.ts"

},

}

```

Since our Redis cluster is in a VPC, we’ll need a tunnel to connect to it from our local machine.
Terminal window```

sudobunssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
To start your app locally run.
Terminal window```

bunsstdev

```

Now if you go to `http://localhost:3000` you’ll see a counter update as you refresh the page.
Finally, you can deploy it using `bun sst deploy --stage production` using a `Dockerfile` that’s included in the example.
sst.config.ts
```typescript

const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });

const redis = newsst.aws.Redis("MyRedis", { vpc });

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

new sst.aws.Service("MyService", {

cluster,

link: [redis],

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "bun dev",

},

});

```

View the
* * *

## [AWS Cluster custom autoscaling](https://sst.dev/docs/examples#aws-cluster-custom-autoscaling)

In this example, we’ll create a cluster that autoscales based on a custom metric. In this case, the number of messages in a queue.
We’ll create a queue, and two functions that’ll seed and purge the queue. We’ll also create two policies.
One that scales it up.
sst.config.ts

```typescript


const scaleUpPolicy = newaws.appautoscaling.Policy("ScaleUpPolicy", {




serviceNamespace: service.nodes.autoScalingTarget.serviceNamespace,




scalableDimension: service.nodes.autoScalingTarget.scalableDimension,




resourceId: service.nodes.autoScalingTarget.resourceId,




policyType: "StepScaling",



stepScalingPolicyConfiguration: {



adjustmentType: "ChangeInCapacity",




cooldown: 5,




stepAdjustments: [



{



metricIntervalLowerBound: "0",




scalingAdjustment: 1,



},



],



},



});


```

And one that scales it down.
sst.config.ts

```typescript

const scaleDownPolicy = newaws.appautoscaling.Policy("ScaleDownPolicy", {

serviceNamespace: service.nodes.autoScalingTarget.serviceNamespace,

scalableDimension: service.nodes.autoScalingTarget.scalableDimension,

resourceId: service.nodes.autoScalingTarget.resourceId,

policyType: "StepScaling",

stepScalingPolicyConfiguration: {

adjustmentType: "ChangeInCapacity",

cooldown: 5,

stepAdjustments: [

{

metricIntervalUpperBound: "0",

scalingAdjustment: -1,

},

],

},

});

```

We’ll add a CloudWatch metric alarm that triggers the scaling policies if the queue depth exceeds 3 messages.
sst.config.ts

```typescript


new aws.cloudwatch.MetricAlarm("QueueDepthAlarm", {




comparisonOperator: "GreaterThanThreshold",




evaluationPeriods: 1,




metricName: "ApproximateNumberOfMessagesVisible",




namespace: "AWS/SQS",




period: 10,




statistic: "Average",




threshold: 3,



dimensions: {



QueueName: queue.nodes.queue.name,



},



alarmDescription: "Scale up when queue depth exceeds 3 messages",




alarmActions: [scaleUpPolicy.arn],




okActions: [scaleDownPolicy.arn],



});

```

To test this example, first deploy your app then:

  1. Invoke the `MyQueueSeeder` URL. This will cause the service to scale up to 5 instances in a few minutes.
  2. Then invoke the `MyQueuePurger` URL. This will cause the service to scale down to 1 instance in a few minutes.

sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc");

// Create a queue and two functions to seed and purge the queue

const queue = newsst.aws.Queue("MyQueue");

new sst.aws.Function("MyQueueSeeder", {

handler: "queue.seeder",

link: [queue],

url: true,

});

new sst.aws.Function("MyQueuePurger", {

handler: "queue.purger",

link: [queue],

url: true,

});

// Create a cluster and disable default scaling on CPU and memory utilization

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

const service = newsst.aws.Service("MyService", {

cluster,

loadBalancer: {

ports: [{ listen: "80/http" }],

},

scaling: {

min: 1,

max: 5,

cpuUtilization: false,

memoryUtilization: false,

},

});

// Create a scale up policy that scales up by 1 instance at a time

const scaleUpPolicy = newaws.appautoscaling.Policy("ScaleUpPolicy", {

serviceNamespace: service.nodes.autoScalingTarget.serviceNamespace,

scalableDimension: service.nodes.autoScalingTarget.scalableDimension,

resourceId: service.nodes.autoScalingTarget.resourceId,

policyType: "StepScaling",

stepScalingPolicyConfiguration: {

adjustmentType: "ChangeInCapacity",

cooldown: 5,

stepAdjustments: [

{

metricIntervalLowerBound: "0",

scalingAdjustment: 1,

},

],

},

});

// Create a scale down policy that scales down by 1 instance at a time

const scaleDownPolicy = newaws.appautoscaling.Policy("ScaleDownPolicy", {

serviceNamespace: service.nodes.autoScalingTarget.serviceNamespace,

scalableDimension: service.nodes.autoScalingTarget.scalableDimension,

resourceId: service.nodes.autoScalingTarget.resourceId,

policyType: "StepScaling",

stepScalingPolicyConfiguration: {

adjustmentType: "ChangeInCapacity",

cooldown: 5,

stepAdjustments: [

{

metricIntervalUpperBound: "0",

scalingAdjustment: -1,

},

],

},

});

// Create an alarm that scales up when the queue depth exceeds 3 messages

// and scales down when the queue depth is less than 3 messages

new aws.cloudwatch.MetricAlarm("QueueDepthAlarm", {

comparisonOperator: "GreaterThanThreshold",

evaluationPeriods: 1,

metricName: "ApproximateNumberOfMessagesVisible",

namespace: "AWS/SQS",

period: 10,

statistic: "Average",

threshold: 3,

dimensions: {

QueueName: queue.nodes.queue.name,

},

alarmDescription: "Scale up when queue depth exceeds 3 messages",

alarmActions: [scaleUpPolicy.arn],

okActions: [scaleDownPolicy.arn],

});

```

View the
* * *

## [AWS Cluster private service](https://sst.dev/docs/examples#aws-cluster-private-service)

Adds a private load balancer to a service by setting the `loadBalancer.public` prop to `false`.
This allows you to create internal services that can only be accessed inside a VPC.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


loadBalancer: {



public: false,




ports: [{ listen: "80/http" }],



},


});

```

View the
* * *

## [AWS Cluster Spot capacity](https://sst.dev/docs/examples#aws-cluster-spot-capacity)

This example, shows how to use the Fargate Spot capacity provider for your services.
We have it set to use only Fargate Spot instances for all non-production stages. Learn more about the [`capacity`](https://sst.dev/docs/component/aws/cluster#capacity) prop.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc");

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

new sst.aws.Service("MyService", {

cluster,

loadBalancer: {

ports: [{ listen: "80/http" }],

},

capacity: $app.stage==="production"?undefined:"spot",

});

```

View the
* * *

## [AWS Cluster with API Gateway](https://sst.dev/docs/examples#aws-cluster-with-api-gateway)

Expose a service through API Gateway HTTP API using a VPC link.
This is an alternative to using a load balancer. Since API Gateway is pay per request, it works out a lot cheaper for services that don’t get a lot of traffic.
You need to specify which port in your service will be exposed through API Gateway.
sst.config.ts

```typescript


const service = newsst.aws.Service("MyService", {




cluster,



serviceRegistry: {



80,



},



});


```

A couple of things to note:

  1. Your API Gateway HTTP API also needs to be in the **same VPC** as the service.
  2. You also need to verify that your VPC’s
  3. Run `aws ec2 describe-availability-zones` to get a list of AZs for your account.
  4. Only list the AZ ID’s that support VPC link.
sst.config.ts

```typescript

vpc: {

az: ["eu-west-3a", "eu-west-3c"]

}

```

If the VPC picks an AZ automatically that doesn’t support VPC link, you’ll get the following error:

```

operation error ApiGatewayV2: BadRequestException: Subnet is in Availability

Zone 'euw3-az2' where service is not available

```

sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc", {



// Pick at least two AZs that support VPC link


// az: ["eu-west-3a", "eu-west-3c"],



});




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




const service = newsst.aws.Service("MyService", {




cluster,



serviceRegistry: {



port: 80,



},



});




const api = newsst.aws.ApiGatewayV2("MyApi", { vpc });




api.routePrivate("$default", service.nodes.cloudmapService.arn);


```

View the
* * *

## [Subscribe to queues](https://sst.dev/docs/examples#subscribe-to-queues)

Create an SQS queue, subscribe to it, and publish to it from a function.
sst.config.ts

```typescript

// create dead letter queue

const dlq = newsst.aws.Queue("DeadLetterQueue");

dlq.subscribe("subscriber.dlq");

// create main queue

const queue = newsst.aws.Queue("MyQueue", {

dlq: dlq.arn,

});

queue.subscribe("subscriber.main");

const app = newsst.aws.Function("MyApp", {

handler: "publisher.handler",

link: [queue],

url: true,

});

return {

app: app.url,

queue: queue.url,

dlq: dlq.url,

};

```

View the
* * *

## [AWS Deno Redis](https://sst.dev/docs/examples#aws-deno-redis)

Creates a hit counter app with Deno and Redis.
This deploys Deno as a Fargate service to ECS and it’s linked to Redis.
sst.config.ts

```typescript


new sst.aws.Service("MyService", {



cluster,


link: [redis],


loadBalancer: {



ports: [{ listen: "80/http", forward: "8000/http" }],



},


dev: {



command: "deno task dev",



},


});

```

Since our Redis cluster is in a VPC, we’ll need a tunnel to connect to it from our local machine.
Terminal window```

sudossttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
To start your app locally run.
Terminal window```


sstdev


```

Now if you go to `http://localhost:8000` you’ll see a counter update as you refresh the page.
Finally, you can deploy it using `sst deploy --stage production` using a `Dockerfile` that’s included in the example.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });

const redis = newsst.aws.Redis("MyRedis", { vpc });

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

new sst.aws.Service("MyService", {

cluster,

link: [redis],

loadBalancer: {

ports: [{ listen: "80/http", forward: "8000/http" }],

},

dev: {

command: "deno task dev",

},

});

```

View the
* * *

## [Drizzle migrations in CI/CD](https://sst.dev/docs/examples#drizzle-migrations-in-cicd)

An example on how to run Drizzle migrations as a part of your CI/CD.
Start by creating a function that runs migrations.
sst.config.ts

```typescript


const migrator = newsst.aws.Function("DatabaseMigrator", {




handler: "src/migrator.handler",




link: [rds],




vpc,




copyFiles: [



{



from: "migrations",




to: "./migrations",



},



],




});


```

Where `src/migrator.ts` looks like.
src/migrator.ts

```typescript

import { db } from"./drizzle";

import { migrate } from"drizzle-orm/postgres-js/migrator";

export const handler = async (event:any) => {

await migrate(db, {

migrationsFolder: "./migrations",

});

};

```

And we can set it up to run on every deploy.
sst.config.ts

```typescript


if (!$dev){




new aws.lambda.Invocation("DatabaseMigratorInvocation", {




input: Date.now().toString(),




functionName: migrator.name,



});


}

```

We use the current time to make sure the function runs on every deploy.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc", { bastion: true, nat: "ec2" });

const rds = newsst.aws.Postgres("MyPostgres", { vpc, proxy: true });

new sst.aws.Function("MyApi", {

vpc,

url: true,

link: [rds],

handler: "src/api.handler",

});

const migrator = newsst.aws.Function("DatabaseMigrator", {

handler: "src/migrator.handler",

link: [rds],

vpc,

copyFiles: [

{

from: "migrations",

to: "./migrations",

},

],

});

if (!$dev) {

new aws.lambda.Invocation("DatabaseMigratorInvocation", {

input: Date.now().toString(),

functionName: migrator.name,

});

}

new sst.x.DevCommand("Studio", {

link: [rds],

dev: {

command: "npx drizzle-kit studio",

},

});

```

View the
* * *

## [DynamoDB streams](https://sst.dev/docs/examples#dynamodb-streams)

Create a DynamoDB table, enable streams, and subscribe to it with a function.
sst.config.ts

```typescript


const table = newsst.aws.Dynamo("MyTable", {



fields: {



id: "string",



},



primaryIndex: { hashKey: "id" },




stream: "new-and-old-images",




});




table.subscribe("MySubscriber", "subscriber.handler", {



filters: [


{


dynamodb: {


NewImage: {


message: {



S: ["Hello"],



},


},


},


},


],


});



const app = newsst.aws.Function("MyApp", {




handler: "publisher.handler",




link: [table],




url: true,




});




return {




app: app.url,




table: table.name,



};

```

View the
* * *

## [EC2 with Pulumi](https://sst.dev/docs/examples#ec2-with-pulumi)

Use raw Pulumi resources to create an EC2 instance.
sst.config.ts

```typescript

// Notice you don't need to import pulumi, it is already part of sst.

const securityGroup = newaws.ec2.SecurityGroup("web-secgrp", {

ingress: [

{

protocol: "tcp",

fromPort: 80,

toPort: 80,

cidrBlocks: ["0.0.0.0/0"],

},

],

});

// Find the latest Ubuntu AMI

const ami = aws.ec2.getAmi({

filters: [

{

name: "name",

values: ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"],

},

],

mostRecent: true,

owners: ["099720109477"], // Canonical

});

// User data to set up a simple web server

const userData = `#!/bin/bash

ho "Hello, World!" > index.html

hup python3 -m http.server 80 &`;

// Create an EC2 instance

const server = newaws.ec2.Instance("web-server", {

instanceType: "t2.micro",

ami: ami.then((ami) => ami.id),

userData: userData,

vpcSecurityGroupIds: [securityGroup.id],

associatePublicIpAddress: true,

});

return {

app: server.publicIp,

};

```

View the
* * *

## [AWS EFS with SQLite](https://sst.dev/docs/examples#aws-efs-with-sqlite)

Mount an EFS file system to a function and write to a SQLite database.
index.ts

```typescript


const db = sqlite3("/mnt/efs/mydb.sqlite");


```

The file system is mounted to `/mnt/efs` in the function.
Given the performance of EFS, it’s not recommended to use it for databases.
This example is for demonstration purposes only. It’s not recommended to use EFS for databases in production.
sst.config.ts

```typescript

// NAT Gateways are required for Lambda functions

const vpc = newsst.aws.Vpc("MyVpc", { nat: "managed" });

// Create an EFS file system to store the SQLite database

const efs = newsst.aws.Efs("MyEfs", { vpc });

// Create a Lambda function that queries the database

new sst.aws.Function("MyFunction", {

vpc,

url: true,

volume: {

efs,

path: "/mnt/efs",

},

handler: "index.handler",

nodejs: {

install: ["better-sqlite3"],

},

});

```

View the
* * *

## [AWS EFS with SurrealDB](https://sst.dev/docs/examples#aws-efs-with-surrealdb)

We use the SurrealDB docker image to run a server in a container and use EFS as the file system.
sst.config.ts

```typescript


const server = newsst.aws.Service("MyService", {




cluster,




architecture: "arm64",




image: "surrealdb/surrealdb:v2.0.2",



// ...



volumes: [




{ efs, path: "/data" },




],




});


```

We then connect to the server from a Lambda function.
index.ts

```typescript

const endpoint = `http://${Resource.MyConfig.host}:${Resource.MyConfig.port}`;

const db = newSurreal();

awaitdb.connect(endpoint);

```

This uses the SurrealDB client to connect to the server.
Given the performance of EFS, it’s not recommended to use it for databases.
This example is for demonstration purposes only. It’s not recommended to use EFS for databases in production.
sst.config.ts

```typescript


const { RandomPassword } = await import("@pulumi/random");



// SurrealDB Credentials



const PORT = 8080;




const NAMESPACE = "test";




const DATABASE = "test";




const USERNAME = "root";




const PASSWORD = newRandomPassword("Password", {




length: 32,




}).result;



// NAT Gateways are required for Lambda functions



const vpc = newsst.aws.Vpc("MyVpc", { nat: "managed" });



// Store SurrealDB data in EFS



const efs = newsst.aws.Efs("MyEfs", { vpc });



// Run SurrealDB server in a container



const cluster = newsst.aws.Cluster("MyCluster", { vpc });




const server = newsst.aws.Service("MyService", {




cluster,




architecture: "arm64",




image: "surrealdb/surrealdb:v2.0.2",




command: [




"start",




"--bind",




$interpolate`0.0.0.0:${PORT}`,




"--log",




"info",




"--user",




USERNAME,




"--pass",




PASSWORD,




"surrealkv://data/data.skv",




"--allow-scripting",




],




volumes: [{ efs, path: "/data" }],




});



// Lambda client to connect to SurrealDB



const config = newsst.Linkable("MyConfig", {



properties: {



username: USERNAME,




password: PASSWORD,




namespace: NAMESPACE,




database: DATABASE,




port: PORT,




host: server.service,



},



});




new sst.aws.Function("MyApp", {




handler: "index.handler",



link: [config],



url: true,



vpc,


});

```

View the
* * *

## [AWS EFS](https://sst.dev/docs/examples#aws-efs)

Mount an EFS file system to a function and a container.
This allows both your function and the container to access the same file system. Here they both update a counter that’s stored in the file system.
common.mjs```

awaitwriteFile("/mnt/efs/counter", newValue.toString());

```

The file system is mounted to `/mnt/efs` in both the function and the container.
sst.config.ts
```typescript

// NAT Gateways are required for Lambda functions



const vpc = newsst.aws.Vpc("MyVpc", { nat: "managed" });



// Create an EFS file system to store a counter



const efs = newsst.aws.Efs("MyEfs", { vpc });



// Create a Lambda function that increments the counter



new sst.aws.Function("MyFunction", {




handler: "lambda.handler",




url: true,



vpc,


volume: {


efs,



path: "/mnt/efs",



},


});


// Create a service that increments the same counter



const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


loadBalancer: {



ports: [{ listen: "80/http" }],



},


volumes: [


{


efs,



path: "/mnt/efs",



},


],


});

```

View the
* * *

## [AWS Express Redis](https://sst.dev/docs/examples#aws-express-redis)

Creates a hit counter app with Express and Redis.
This deploys Express as a Fargate service to ECS and it’s linked to Redis.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

cluster,

loadBalancer: {

ports: [{ listen: "80/http" }],

},

dev: {

command: "node --watch index.mjs",

},

link: [redis],

});

```

Since our Redis cluster is in a VPC, we’ll need a tunnel to connect to it from our local machine.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
To start your app locally run.
Terminal window```

npxsstdev

```

Now if you go to `http://localhost:80` you’ll see a counter update as you refresh the page.
Finally, you can deploy it using `npx sst deploy --stage production` using a `Dockerfile` that’s included in the example.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });




const redis = newsst.aws.Redis("MyRedis", { vpc });




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


link: [redis],


loadBalancer: {



ports: [{ listen: "80/http" }],



},


dev: {



command: "node --watch index.mjs",



},


});

```

View the
* * *

## [FFmpeg in Lambda](https://sst.dev/docs/examples#ffmpeg-in-lambda)

Uses `clip.mp4` and grabs a single frame from it.
You don’t need to use a Lambda layer to use FFmpeg.
We use the
index.ts

```typescript

import ffmpeg from"ffmpeg-static";

```

We can use this to spawn a child process and run FFmpeg.
index.ts

```typescript


spawnSync(ffmpeg, ffmpegParams, { stdio: "pipe" });


```

We don’t need a layer when we deploy this because SST will use the right binary for the target Lambda architecture; including `arm64`.
sst.config.ts

```typescript

{

nodejs: { install: ["ffmpeg-static"] }

}

```

All this is handled by [`nodejs.install`](https://sst.dev/docs/component/aws/function#nodejs-install).
sst.config.ts

```typescript


const func = newsst.aws.Function("MyFunction", {




url: true,




memory: "2 GB",




timeout: "15 minutes",




handler: "index.handler",




copyFiles: [{ from: "clip.mp4" }],




nodejs: { install: ["ffmpeg-static"] },




});




return {




url: func.url,



};

```

View the
* * *

## [AWS ApiGatewayV2 Go](https://sst.dev/docs/examples#aws-apigatewayv2-go)

Uses
We use the `aws-lambda-go-api-proxy` package to handle the API Gateway V2 event.
So you write your Go function as you normally would and then use the package to handle the API Gateway V2 event.
main.go```

import (

"github.com/aws/aws-lambda-go/lambda"

"github.com/awslabs/aws-lambda-go-api-proxy/httpadapter"

)

funcrouter() *http.ServeMux {

mux:=http.NewServeMux()

mux.HandleFunc("/", func(w http.ResponseWriter, r*http.Request) {

w.Header().Set("Content-Type", "application/json")

w.WriteHeader(http.StatusOK)

w.Write([]byte(`{"message": "hello world"}`))

})

returnmux

}

funcmain() {

lambda.Start(httpadapter.NewV2(router()).ProxyWithContext)

}

```

sst.config.ts
```typescript


const api = newsst.aws.ApiGatewayV2("GoApi");




api.route("$default", {




handler: "src/",




runtime: "go",



});

```

View the
* * *

## [AWS Lambda Go S3 Presigned](https://sst.dev/docs/examples#aws-lambda-go-s3-presigned)

Generates a presigned URL for the linked S3 bucket in a Go Lambda function.
Configure the S3 Client and the PresignedClient.
main.go```

cfg, err:=config.LoadDefaultConfig(context.TODO())

iferr!=nil {

panic(err)

}

client:=s3.NewFromConfig(cfg)

presignedClient:=s3.NewPresignClient(client)

```

Generate the presigned URL.
main.go```


bucketName, err:=resource.Get("Bucket", "name")




iferr!=nil {




panic(err)



}



url, err:=presignedClient.PresignPutObject(context.TODO(), &s3.PutObjectInput{




Bucket: aws.String(bucket.(string)),




Key:    aws.String(key),



})

```

sst.config.ts

```typescript

const bucket = newsst.aws.Bucket("Bucket");

const api = newsst.aws.ApiGatewayV2("Api");

api.route("GET /upload-url", {

handler: "src/",

runtime: "go",

link: [bucket],

});

```

View the
* * *

## [AWS Lambda Go DynamoDB](https://sst.dev/docs/examples#aws-lambda-go-dynamodb)

An example on how to use a Go runtime Lambda with DynamoDB.
You configure the DynamoDB client.
src/main.go```

import (

"github.com/sst/sst/v3/sdk/golang/resource"

)

funcmain() {

cfg, err:=config.LoadDefaultConfig(context.Background())

iferr!=nil {

panic(err)

}

client:=dynamodb.NewFromConfig(cfg)

tableName, err:=resource.Get("Table", "name")

iferr!=nil {

panic(err)

}

}

```

And make a request to DynamoDB.
src/main.go```

_, err=r.client.PutItem(ctx, &dynamodb.PutItemInput{

TableName: tableName.(string),

Item:      item,

})

```

sst.config.ts

```typescript


const table = newsst.aws.Dynamo("Table", {



fields: {



PK: "string",




SK: "string",



},



primaryIndex: { hashKey: "PK", rangeKey: "SK" },




});




new sst.aws.Function("GoFunction", {




url: true,




runtime: "go",




handler: "./src",



link: [table],


});

```

View the
* * *

## [AWS Hono container with Redis](https://sst.dev/docs/examples#aws-hono-container-with-redis)

Creates a hit counter app with Hono and Redis.
This deploys Hono API as a Fargate service to ECS and it’s linked to Redis.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

cluster,

link: [redis],

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "npm run dev",

},

});

```

Since our Redis cluster is in a VPC, we’ll need a tunnel to connect to it from our local machine.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
To start your app locally run.
Terminal window```

npxsstdev

```

Now if you go to `http://localhost:3000` you’ll see a counter update as you refresh the page.
Finally, you can deploy it by:

  1. Using the `Dockerfile` that’s included in this example.
  2. This compiles our TypeScript file, so we’ll need add the following to the `tsconfig.json`.
tsconfig.json```

{

"compilerOptions": {

// ...

"outDir": "./dist"

},

"exclude": ["node_modules"]

}

```

  3. Install TypeScript.
Terminal window```

npminstalltypescript--save-dev

```

  4. And add a `build` script to our `package.json`.
package.json```

"scripts": {

// ...

"build": "tsc"

}

```

And finally, running `npx sst deploy --stage production`.
sst.config.ts
```typescript

const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });

const redis = newsst.aws.Redis("MyRedis", { vpc });

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

new sst.aws.Service("MyService", {

cluster,

link: [redis],

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "npm run dev",

},

});

```

View the
* * *

## [AWS Hono streaming](https://sst.dev/docs/examples#aws-hono-streaming)

An example on how to enable streaming for Lambda functions using Hono.
While `sst dev` doesn’t support streaming, we can conditionally enable it on deploy.
sst.config.ts

```typescript

{



streaming: $dev ?false:true



}

```

index.ts

```typescript

export const handler = process.env.SST_LIVE ? handle(app) : streamHandle(app);

```

This will return the standard handler for `sst dev`.
Streaming is currently not supported in `sst dev`.
To test this in your terminal, use the `curl` command with the `--no-buffer` option.
Terminal window```

curl--no-bufferhttps://u3dyblk457ghskwbmzrbylpxoi0ayrbb.lambda-url.us-east-1.on.aws

```

Here we are using a Function URL directly because API Gateway doesn’t support streaming.
sst.config.ts
```typescript

const hono = newsst.aws.Function("Hono", {

url: true,

streaming: $dev ? false : true,

timeout: "15 minutes",

handler: "index.handler",

});

return {

api: hono.url,

};

```

View the
* * *

## [IAM permissions boundaries](https://sst.dev/docs/examples#iam-permissions-boundaries)

Use permissions boundaries to set the maximum permissions for all IAM roles that’ll be created in your app.
In this example, the Function has the `s3:ListAllMyBuckets` and `sqs:ListQueues` permissions. However, we create a permissions boundary that only allows `s3:ListAllMyBuckets`. And we apply it to all Roles in the app using the global [`$transform`](https://sst.dev/docs/reference/global/#transform).
As a result, the Function is only allowed to list S3 buckets. If you open the deployed URL, you’ll see that the SQS list call fails.
Learn more about
sst.config.ts

```typescript

// Create a permission boundary



const permissionsBoundary = newaws.iam.Policy("MyPermissionsBoundary", {




policy: aws.iam.getPolicyDocumentOutput({




statements: [



{



actions: ["s3:ListAllMyBuckets"],




resources: ["*"],



},



],




}).json,




});



// Apply the boundary to all roles



$transform(aws.iam.Role, (args)=> {




args.permissionsBoundary= permissionsBoundary;



});


// The boundary automatically applies to this Function's role



const app = newsst.aws.Function("MyApp", {




handler: "index.handler",




permissions: [



{



actions: ["s3:ListAllMyBuckets", "sqs:ListQueues"],




resources: ["*"],



},



],




url: true,




});




return {




app: app.url,



};

```

View the
* * *

## [Current AWS account](https://sst.dev/docs/examples#current-aws-account)

You can use the `aws.getXXXXOutput()` provider functions to get info about the current AWS account. Learn more about [provider functions](https://sst.dev/docs/providers/#functions).
sst.config.ts

```typescript

return {

region: aws.getRegionOutput().name,

account: aws.getCallerIdentityOutput({}).accountId,

};

```

View the
* * *

## [AWS JSX Email](https://sst.dev/docs/examples#aws-jsx-email)

Uses `Email` component to design and send emails.
To test this example, change the `sst.config.ts` to use your own email address.
sst.config.ts

```typescript


sender: "email@example.com"


```

Then run.
Terminal window```

npminstall

npxsstdev

```

You’ll get an email from AWS asking you to confirm your email address. Click the link to verify it.
Next, go to the URL in the `sst dev` CLI output. You should now receive an email rendered using JSX Email.
index.ts
```typescript


import { Template } from"./templates/email";




awaitrender(Template({




email: "spongebob@example.com",




name: "Spongebob Squarepants"



}))

```

Once you are ready to go to production, you can:

* And [use your domain](https://sst.dev/docs/component/aws/email/) to send emails

sst.config.ts

```typescript

const email = newsst.aws.Email("MyEmail", {

sender: "<email@example.com>",

});

const api = newsst.aws.Function("MyApi", {

handler: "index.handler",

link: [email],

url: true,

});

return {

api: api.url,

};

```

View the
* * *

## [Kinesis streams](https://sst.dev/docs/examples#kinesis-streams)

Create a Kinesis stream, and subscribe to it with a function.
sst.config.ts

```typescript


const stream = newsst.aws.KinesisStream("MyStream");



// Create a function subscribing to all events



stream.subscribe("AllSub", "subscriber.all");



// Create a function subscribing to events of `bar` type



stream.subscribe("FilteredSub", "subscriber.filtered", {



filters: [


{


data: {



type: ["bar"],



},


},


],


});



const app = newsst.aws.Function("MyApp", {




handler: "publisher.handler",




link: [stream],




url: true,




});




return {




app: app.url,




stream: stream.name,



};

```

View the
* * *

## [AWS Lambda Go](https://sst.dev/docs/examples#aws-lambda-go)

This example shows how to use the
Our Go function is in the `src` directory and we point to it in our function.
sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

url: true,

runtime: "go",

link: [bucket],

handler: "./src",

});

```

We are also linking it to an S3 bucket. We can reference the bucket in our function.
src/main.go```

funchandler() (string, error) {

bucket, err:=resource.Get("MyBucket", "name")

iferr!=nil {

return"", err

}

returnbucket.(string), nil

}

```

The `resource.Get` function is from the SST Go SDK.
src/main.go```

import (

"github.com/sst/sst/v3/sdk/golang/resource"

)

```

The `sst dev` CLI also supports running your Go function [_Live_](https://sst.dev/docs/live).
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket");




new sst.aws.Function("MyFunction", {




url: true,




runtime: "go",



link: [bucket],



handler: "./src",



});

```

View the
* * *

## [AWS Lambda build hook](https://sst.dev/docs/examples#aws-lambda-build-hook)

In this example we hook into the Lambda function build process with `hook.postbuild`.
This is useful for modifying the generated Lambda function code before it’s uploaded to AWS. It can also be used for uploading the generated sourcemaps to a service like Sentry.
sst.config.ts

```typescript

new sst.aws.Function("MyFunction", {

url: true,

handler: "index.handler",

hook: {

asyncpostbuild(dir) {

console.log(`postbuild ------- ${dir}`);

},

},

});

```

View the
* * *

## [AWS Lambda retry with queues](https://sst.dev/docs/examples#aws-lambda-retry-with-queues)

An example on how to retry Lambda invocations using SQS queues.
Create a SQS retry queue which will be set as the destination for the Lambda function.
src/retry.ts

```typescript


const retryQueue = newsst.aws.Queue("retryQueue");




const bus = newsst.aws.Bus("bus");




const busSubscriber = bus.subscribe("busSubscriber", {




handler: "src/bus-subscriber.handler",



environment: {



RETRIES: "2", // set the number of retries



},



link: [retryQueue], // so the function can send messages to the retry queue




});




new aws.lambda.FunctionEventInvokeConfig("eventConfig", {




functionName: $resolve([busSubscriber.nodes.function.name]).apply(




([name])=> name,



),



maximumRetryAttempts: 2, // default is 2, must be between 0 and 2



destinationConfig: {


onFailure: {



destination: retryQueue.arn,



},


},


});

```

Create a bus subscriber which will publish messages to the bus. Include a DLQ for messages that continue to fail.
sst.config.ts

```typescript

const dlq = newsst.aws.Queue("dlq");

retryQueue.subscribe({

handler: "src/retry.handler",

link: [busSubscriber.nodes.function, retryQueue, dlq],

timeout: "30 seconds",

environment: {

RETRIER_QUEUE_URL: retryQueue.url,

},

permissions: [

{

actions: ["lambda:GetFunction", "lambda:InvokeFunction"],

resources: [

$interpolate`arn:aws:lambda:${aws.getRegionOutput().name}:${

aws.getCallerIdentityOutput().accountId

}:function:*`,

],

},

],

transform: {

function: {

deadLetterConfig: {

targetArn: dlq.arn,

},

},

},

});

```

The Retry function will read mesaages and send back to the queue to be retried with a backoff.
src/retry.ts

```typescript


export const handler:SQSHandler = async (evt) => {




for (const recordofevt.Records) {




const parsed = JSON.parse(record.body);




console.log("body", parsed);




const functionName = parsed.requestContext.functionArn




.replace(":$LATEST", "")




.split(":")




.pop();




if (parsed.responsePayload) {




const attempt = (parsed.requestPayload.attempts || 0) + 1;




const info = await lambda.send(




newGetFunctionCommand({




FunctionName: functionName,




}),




);




const max =




Number.parseInt(




info.Configuration?.Environment?.Variables?.RETRIES || "",




) || 0;




console.log("max retries", max);




if (attempt > max) {




console.log(`giving up after ${attempt} retries`);



// send to dlq



await sqs.send(




newSendMessageCommand({




QueueUrl: Resource.dlq.url,




MessageBody: JSON.stringify({




requestPayload: parsed.requestPayload,




requestContext: parsed.requestContext,




responsePayload: parsed.responsePayload,




}),




}),




);



return;


}



const seconds = Math.min(Math.pow(2, attempt), 900);




console.log(




"delaying retry by ",




seconds,




"seconds for attempt",




attempt,




);




parsed.requestPayload.attempts = attempt;




await sqs.send(




newSendMessageCommand({




QueueUrl: Resource.retryQueue.url,




DelaySeconds: seconds,




MessageBody: JSON.stringify({




requestPayload: parsed.requestPayload,




requestContext: parsed.requestContext,




}),




}),




);



}



if (!parsed.responsePayload) {




console.log("triggering function");



try {



await lambda.send(




newInvokeCommand({




InvocationType: "Event",




Payload: Buffer.from(JSON.stringify(parsed.requestPayload)),




FunctionName: functionName,




}),




);




} catch (e) {




if (e instanceof ResourceNotFoundException) {



return;


}



throw e;



}


}


}



};


```

sst.config.ts

```typescript

const dlq = newsst.aws.Queue("dlq");

const retryQueue = newsst.aws.Queue("retryQueue");

const bus = newsst.aws.Bus("bus");

const busSubscriber = bus.subscribe("busSubscriber", {

handler: "src/bus-subscriber.handler",

environment: {

RETRIES: "2",

},

link: [retryQueue], // so the function can send messages to the queue

});

const publisher = newsst.aws.Function("publisher", {

handler: "src/publisher.handler",

link: [bus],

url: true,

});

new aws.lambda.FunctionEventInvokeConfig("eventConfig", {

functionName: $resolve([busSubscriber.nodes.function.name]).apply(

([name])=> name,

),

maximumRetryAttempts: 1,

destinationConfig: {

onFailure: {

destination: retryQueue.arn,

},

},

});

retryQueue.subscribe({

handler: "src/retry.handler",

link: [busSubscriber.nodes.function, retryQueue, dlq],

timeout: "30 seconds",

environment: {

RETRIER_QUEUE_URL: retryQueue.url,

},

permissions: [

{

actions: ["lambda:GetFunction", "lambda:InvokeFunction"],

resources: [

$interpolate`arn:aws:lambda:${aws.getRegionOutput().name}:${

aws.getCallerIdentityOutput().accountId

}:function:*`,

],

},

],

transform: {

function: {

deadLetterConfig: {

targetArn: dlq.arn,

},

},

},

});

return {

publisher: publisher.url,

dlq: dlq.url,

retryQueue: retryQueue.url,

};

```

View the
* * *

## [AWS Lamda Rust multiple-binaries](https://sst.dev/docs/examples#aws-lamda-rust-multiple-binaries)

This example shows how to deploy multiple binary rust project to AWS Lambda.
SST relies on the work of
What is special about the following file is that we are defining multiple binaries using the `[[bin]]` section in the `Cargo.toml` file.
Cargo.toml```

[package]

name = "aws-lambda-rust-multi-bin"

version = "0.1.0"

edition = "2021"

[dependencies]

lambda_runtime = "0.13.0"

serde = { version = "1.0.217", features = ["derive"] }

serde_json = "1.0.138"

tokio = { version = "1", features = ["macros"] }

# -- please note ommited dependencies --

[[bin]]

name = "push"

path = "src/push.rs"

[[bin]]

name = "pop"

path = "src/pop.rs"

```

We then utilise the . syntax to specify the handler binary
sst.config.ts
```typescript

new sst.aws.Function("push", {

url: true,

runtime: "rust",

link: [bucket],

handler: "./.push",

});

new sst.aws.Function("pop", {

url: true,

runtime: "rust",

link: [bucket],

handler: "./.pop",

});

```

sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("Bucket");




const push = newsst.aws.Function("push", {




runtime: "rust",




handler: "./.push",




url: true,




architecture: "arm64",




link: [bucket],




});




const pop = newsst.aws.Function("pop", {




runtime: "rust",




handler: "./.pop",




url: true,




architecture: "arm64",




link: [bucket],




});




return { push_url: push.url, pop_url: pop.url };


```

View the
* * *

## [AWS Lambda streaming](https://sst.dev/docs/examples#aws-lambda-streaming)

An example on how to enable streaming for Lambda functions.
sst.config.ts

```typescript

{

streaming: true

}

```

While `sst dev` doesn’t support streaming, you can use the
Terminal window```

npminstalllambda-stream

```

Then, you can use the `streamifyResponse` function to wrap your handler:
index.ts
```typescript

import { APIGatewayProxyEventV2 } from"aws-lambda";

import { streamifyResponse, ResponseStream } from"lambda-stream";

export const handler = streamifyResponse(myHandler);

asyncfunctionmyHandler(

_event:APIGatewayProxyEventV2,

responseStream:ResponseStream

):Promise<void> {

returnnewPromise((resolve, _reject)=> {

responseStream.setContentType('text/plain')

responseStream.write('Hello')

setTimeout(()=> {

responseStream.write(' World')

responseStream.end()

resolve()

},3000)

})

}

```

When deployed, this will use the `awslambda.streamifyResponse`.
Streaming is currently not supported in `sst dev`.
To test this in your terminal, use the `curl` command with the `--no-buffer` option.
Terminal window```

curl--no-bufferhttps://u3dyblk457ghskwbmzrbylpxoi0ayrbb.lambda-url.us-east-1.on.aws

```

Here we are using a Function URL directly because API Gateway doesn’t support streaming.
sst.config.ts
```typescript

const fn = newsst.aws.Function("MyFunction", {

url: true,

streaming: true,

timeout: "15 minutes",

handler: "index.handler",

});

return {

url: fn.url,

};

```

View the
* * *

## [AWS Lambda in a VPC](https://sst.dev/docs/examples#aws-lambda-in-a-vpc)

You can use SST to locally work on Lambda functions that are in a VPC. To do so, you’ll need to enable `bastion` and `nat` on the `Vpc` component.
sst.config.ts

```typescript


new sst.aws.Vpc("MyVpc", { bastion: true, nat: "managed" });


```

The NAT gateway is necessary to allow your Lambda function to connect to the internet. While, the bastion host is necessary for your local machine to be able to tunnel to the VPC.
You’ll need to install the tunnel, if you haven’t done this before.
Terminal window```

sudossttunnelinstall

```

This needs _sudo_ to create the network interface on your machine. You’ll only need to do this once.
Now you can run `sst dev`, your function can access resources in the VPC. For example, here we are connecting to a Redis cluster.
index.ts
```typescript


const redis = newCluster(




[{ host: Resource.MyRedis.host, port: Resource.MyRedis.port }],



{



dnsLookup: (address, callback) => callback(null, address),



redisOptions: {


tls: {},



username: Resource.MyRedis.username,




password: Resource.MyRedis.password,



},


}


);

```

The Redis cluster is in the same VPC as the function.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc", { bastion: true, nat: "managed" });

const redis = newsst.aws.Redis("MyRedis", { vpc });

const api = newsst.aws.Function("MyFunction", {

vpc,

url: true,

link: [redis],

handler: "index.handler"

});

return {

url: api.url,

};

```

View the
* * *

## [AWS Load Balancer Web Application Firewall (WAF)](https://sst.dev/docs/examples#aws-load-balancer-web-application-firewall-waf)

Enable WAF for an AWS Load Balancer.
The WAF is configured to enable a rate limit and enables AWS managed rules.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc");




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




const service = cluster.addService("MyAppService", {



image: {



context: "./",




dockerfile: "packages/server/Dockerfile",



},



});




const rateLimitRule = {




name: "RateLimitRule",



statement: {


rateBasedStatement: {



limit: 200,




aggregateKeyType: "IP",



},


},



priority: 1,



action: { block: {} },


visibilityConfig: {



cloudwatchMetricsEnabled: true,




sampledRequestsEnabled: true,




metricName: "MyAppRateLimitRule",



},



};




const awsManagedRules = {




name: "AWSManagedRules",



statement: {


managedRuleGroupStatement: {



name: "AWSManagedRulesCommonRuleSet",




vendorName: "AWS",



},


},



priority: 2,



overrideAction: {


none: {},


},


visibilityConfig: {



cloudwatchMetricsEnabled: true,




sampledRequestsEnabled: true,




metricName: "MyAppAWSManagedRules",



},



};




const webAcl = newaws.wafv2.WebAcl("AppAlbWebAcl", {



defaultAction: { allow: {} },



scope: "REGIONAL",



visibilityConfig: {



cloudwatchMetricsEnabled: true,




sampledRequestsEnabled: true,




metricName: "AppAlbWebAcl",



},



rules: [rateLimitRule, awsManagedRules],




});




service.nodes.loadBalancer.arn.apply((arn)=> {




new aws.wafv2.WebAclAssociation("MyAppAlbWebAclAssociation", {



resourceArn: arn,



webAclArn: webAcl.arn,



});


});



return {};


```

View the
* * *

## [AWS multi-region](https://sst.dev/docs/examples#aws-multi-region)

To deploy resources to multiple AWS regions, you can create a new provider for the region you want to deploy to.
sst.config.ts

```typescript

const provider = newaws.Provider("MyProvider", { region: "us-west-2" });

```

And then pass that in to the resource.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", { handler: "index.handler" }, { provider });


```

If no provider is passed in, the default provider will be used. And if no region is specified, the default region from your credentials will be used.
sst.config.ts

```typescript

const east = newsst.aws.Function("MyEastFunction", {

url: true,

handler: "index.handler",

});

const provider = newaws.Provider("MyWestProvider", { region: "us-west-2" });

const west = newsst.aws.Function(

"MyWestFunction",

{

url: true,

handler: "index.handler",

},

{ provider }

);

return {

east: east.url,

west: west.url,

};

```

View the
* * *

## [AWS MySQL local](https://sst.dev/docs/examples#aws-mysql-local)

In this example, we connect to a locally running MySQL instance for dev. While on deploy, we use RDS.
We use the
Terminal window```

dockerrun\

--rm\

-p3306:3306\

-v $(pwd)/.sst/storage/mysql:/var/lib/mysql/data\

-eMYSQL_ROOT_PASSWORD=password\

-eMYSQL_DATABASE=local\

mysql:8.0

```

The data is saved to the `.sst/storage` directory. So if you restart the dev server, the data will still be there.
We then configure the `dev` property of the `Mysql` component with the settings for the local MySQL instance.
sst.config.ts
```typescript

dev: {

username: "root",

password: "password",

database: "local",

host: "localhost",

port: 3306,

}

```

By providing the `dev` prop for Mysql, SST will use the local MySQL instance and not deploy a new RDS database when running `sst dev`.
It also allows us to access the database through a Resource `link` without having to conditionally check if we are running locally.
index.ts

```typescript


const pool = newPool({




host: Resource.MyDatabase.host,




port: Resource.MyDatabase.port,




user: Resource.MyDatabase.username,




password: Resource.MyDatabase.password,




database: Resource.MyDatabase.database,




});


```

The above will work in both `sst dev` and `sst deploy`.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc", { nat: "ec2" });

const mysql = newsst.aws.Mysql("MyDatabase", {

dev: {

username: "root",

password: "password",

database: "local",

host: "localhost",

port: 3306,

},

vpc,

});

new sst.aws.Function("MyFunction", {

vpc,

url: true,

link: [mysql],

handler: "index.handler",

});

```

View the
* * *

## [AWS MySQL](https://sst.dev/docs/examples#aws-mysql)

In this example, we deploy an RDS MySQL database.
sst.config.ts

```typescript


const mysql = newsst.aws.Mysql("MyDatabase", {




vpc,




});


```

And link it to a Lambda function.
sst.config.ts

```typescript

new sst.aws.Function("MyApp", {

handler: "index.handler",

link: [mysql],

url: true,

vpc,

});

```

Now in the function we can access the database.
index.ts

```typescript


const connection = await mysql.createConnection({




database: Resource.MyDatabase.database,




host: Resource.MyDatabase.host,




port: Resource.MyDatabase.port,




user: Resource.MyDatabase.username,




password: Resource.MyDatabase.password,




});


```

We also enable the `bastion` option for the VPC. This allows us to connect to the database from our local machine with the `sst tunnel` CLI.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
Now you can run `npx sst dev` and you can connect to the database from your local machine.
sst.config.ts
```typescript


const vpc = newsst.aws.Vpc("MyVpc", { nat: "ec2", bastion: true });




const mysql = newsst.aws.Mysql("MyDatabase", {




vpc,




});




const app = newsst.aws.Function("MyApp", {




handler: "index.handler",




link: [mysql],




url: true,




vpc,




});




return {




app: app.url,




host: mysql.host,




port: mysql.port,




username: mysql.username,




password: mysql.password,




database: mysql.database,



};

```

View the
* * *

## [AWS NestJS with Redis](https://sst.dev/docs/examples#aws-nestjs-with-redis)

Creates a hit counter app with NestJS and Redis.
You need Node 22.12 or higher for this example to work.
Also make sure you have Node 22.12. Or set the `--experimental-require-module` flag. This’ll allow NestJS to import the SST SDK.
This deploys NestJS as a Fargate service to ECS and it’s linked to Redis.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

cluster,

link: [redis],

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "npm run start:dev",

},

});

```

Since our Redis cluster is in a VPC, we’ll need a tunnel to connect to it from our local machine.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
To start your app locally run.
Terminal window```

npxsstdev

```

Now if you go to `http://localhost:3000` you’ll see a counter update as you refresh the page.
Finally, you can deploy it using `npx sst deploy --stage production` using a `Dockerfile` that’s included in the example.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc('MyVpc', { bastion: true });




const redis = newsst.aws.Redis('MyRedis', { vpc });




const cluster = newsst.aws.Cluster('MyCluster', { vpc });




new sst.aws.Service('MyService', {



cluster,


link: [redis],


loadBalancer: {



ports: [{ listen: '80/http', forward: '3000/http' }],



},


dev: {



command: 'npm run start:dev',



},


});

```

View the
* * *

## [AWS Next.js add behavior](https://sst.dev/docs/examples#aws-nextjs-add-behavior)

Here’s how to add additional routes or cache behaviors to the CDN of a Next.js app deployed with OpenNext to AWS.
Specify the path pattern that you want to forward to your new origin. For example, to forward all requests to the `/blog` path to a different origin.
sst.config.ts

```typescript

pathPattern: "/blog/*"

```

And then specify the domain of the new origin.
sst.config.ts

```typescript


domainName: "blog.example.com"


```

We use this to `transform` our site’s CDN and add the additional behaviors.
sst.config.ts

```typescript

const blogOrigin = {

// The domain of the new origin

domainName: "blog.example.com",

originId: "blogCustomOrigin",

customOriginConfig: {

httpPort: 80,

httpsPort: 443,

originSslProtocols: ["TLSv1.2"],

// If HTTPS is supported

originProtocolPolicy: "https-only",

},

};

const cacheBehavior = {

// The path to forward to the new origin

pathPattern: "/blog/*",

targetOriginId: blogOrigin.originId,

viewerProtocolPolicy: "redirect-to-https",

allowedMethods: ["GET", "HEAD", "OPTIONS"],

cachedMethods: ["GET", "HEAD"],

forwardedValues: {

queryString: true,

cookies: {

forward: "all",

},

},

};

new sst.aws.Nextjs("MyWeb", {

transform: {

cdn: (options: sst.aws.CdnArgs)=> {

options.origins=$resolve(options.origins).apply(val=> [...val, blogOrigin]);

options.orderedCacheBehaviors=$resolve(

options.orderedCacheBehaviors|| []

).apply(val=> [...val, cacheBehavior]);

},

},

});

```

View the
* * *

## [AWS Next.js basic auth](https://sst.dev/docs/examples#aws-nextjs-basic-auth)

Deploys a simple Next.js app and adds basic auth to it.
This is useful for dev environments where you want to share your app your team but ensure that it’s not publicly accessible.
You can use this for all the SSR sites, like Astro, Remix, SvelteKit, etc.
This works by injecting some code into a CloudFront function that checks the basic auth header and matches it against the `USERNAME` and `PASSWORD` secrets.
sst.config.ts

```typescript

{



injection: $interpolate`



if (


!event.request.headers.authorization



|| event.request.headers.authorization.value !== "Basic ${basicAuth}"



) {


return {


statusCode: 401,


headers: {


"www-authenticate": { value: "Basic" }


}


};



}`,



}

```

To deploy this, you need to first set the `USERNAME` and `PASSWORD` secrets.
Terminal window```

sstsecretsetUSERNAMEmy-username

sstsecretsetPASSWORDmy-password

```

If you are deploying this to preview environments, you might want to set the secrets using the [`--fallback`](https://sst.dev/docs/reference/cli#secret) flag.
sst.config.ts
```typescript


const username = newsst.Secret("USERNAME");




const password = newsst.Secret("PASSWORD");




const basicAuth = $resolve([username.value, password.value]).apply(




([username, password]) =>




Buffer.from(`${username}:${password}`).toString("base64")



);



new sst.aws.Nextjs("MyWeb", {



server: {


// Don't password protect prod



edge: $app.stage!=="production"




? {



viewerRequest: {



injection: $interpolate`



if (


!event.request.headers.authorization



|| event.request.headers.authorization.value !== "Basic ${basicAuth}"



) {


return {


statusCode: 401,


headers: {


"www-authenticate": { value: "Basic" }


}


};



}`,



},


}



:undefined,



},


});

```

View the
* * *

## [AWS Next.js container with Redis](https://sst.dev/docs/examples#aws-nextjs-container-with-redis)

Creates a hit counter app with Next.js and Redis.
This deploys Next.js as a Fargate service to ECS and it’s linked to Redis.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

cluster,

link: [redis],

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "npm run dev",

},

});

```

Since our Redis cluster is in a VPC, we’ll need a tunnel to connect to it from our local machine.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
To start your app locally run.
Terminal window```

npxsstdev

```

Now if you go to `http://localhost:3000` you’ll see a counter update as you refresh the page.
Finally, you can deploy it by:

  1. Setting `output: "standalone"` in your `next.config.mjs` file.
  2. Adding a `Dockerfile` that’s included in this example.
  3. Running `npx sst deploy --stage production`.

sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });




const redis = newsst.aws.Redis("MyRedis", { vpc });




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


link: [redis],


loadBalancer: {



ports: [{ listen: "80/http", forward: "3000/http" }],



},


dev: {



command: "npm run dev",



},


});

```

View the
* * *

## [AWS Next.js streaming](https://sst.dev/docs/examples#aws-nextjs-streaming)

An example of how to use streaming Next.js RSC. Uses `Suspense` to stream an async component.
app/page.tsx```

<Suspensefallback={<div>Loading...</div>}>

<Friends />

</Suspense>

```

For this demo we also need to make sure the route is not statically built.
app/page.tsx```


export const dynamic = "force-dynamic";


```

This is deployed with OpenNext, which needs a config to enable streaming.
open-next.config.ts

```typescript

exportdefault {

default: {

override: {

wrapper: "aws-lambda-streaming"

}

}

};

```

You should see the _friends_ section load after a 3 second delay.
Safari handles streaming differently than other browsers.
Safari uses a _enough_ initial HTML to trigger streaming. This is typically only a problem for demo apps.
sst.config.ts

```typescript


new sst.aws.Nextjs("MyWeb");


```

View the
* * *

## [AWS OpenSearch local](https://sst.dev/docs/examples#aws-opensearch-local)

In this example, we connect to a locally running OpenSearch process for dev. While on deploy, we use AWS’ OpenSearch Service.
We use the
Terminal window```

dockerrun\

--rm\

-p9200:9200\

-v $(pwd)/.sst/storage/opensearch:/usr/share/opensearch/data\

-ediscovery.type=single-node\

-eplugins.security.disabled=true\

-eOPENSEARCH_INITIAL_ADMIN_PASSWORD=^Passw0rd^\

opensearchproject/opensearch:2.17.0

```

The data is saved to the `.sst/storage` directory. So if you restart the dev server, the data will still be there.
We then configure the `dev` property of the `OpenSearch` component with the settings for the local OpenSearch instance.
sst.config.ts
```typescript

dev: {



url: "http://localhost:9200",




username: "admin",




password: "^Passw0rd^"



}

```

By providing the `dev` prop for OpenSearch, SST will use the local OpenSearch process and not deploy a new OpenSearch domain when running `sst dev`.
It also allows us to access the local process through a Resource `link` without having to conditionally check if we are running locally.
index.ts

```typescript

const client = newClient({

node: Resource.MySearch.url,

auth: {

username: Resource.MySearch.username,

password: Resource.MySearch.password,

},

});

```

The above will work in both `sst dev` and `sst deploy`.
sst.config.ts

```typescript


const search = newsst.aws.OpenSearch("MySearch", {



dev: {



url: "http://localhost:9200",




username: "admin",




password: "^Passw0rd^",



},



});




new sst.aws.Function("MyApp", {




handler: "index.handler",




url: true,



link: [search],


});

```

View the
* * *

## [AWS OpenSearch](https://sst.dev/docs/examples#aws-opensearch)

In this example we create a new OpenSearch domain, link it to a function, and then query it.
Start by creating a new OpenSearch domain.
sst.config.ts

```typescript

const search = newsst.aws.OpenSearch("MySearch");

```

Once linked to a function, we can connect to it.
index.ts

```typescript


import { Resource } from"sst";




import { Client } from"@opensearch-project/opensearch";




const client = newClient({




node: Resource.MySearch.url,



auth: {



username: Resource.MySearch.username,




password: Resource.MySearch.password



}



});


```

This is using the
sst.config.ts

```typescript

const search = newsst.aws.OpenSearch("MySearch");

const app = newsst.aws.Function("MyApp", {

handler: "index.handler",

url: true,

link: [search],

});

return {

app: app.url,

url: search.url,

username: search.username,

password: search.password,

};

```

View the
* * *

## [AWS Postgres local](https://sst.dev/docs/examples#aws-postgres-local)

In this example, we connect to a locally running Postgres instance for dev. While on deploy, we use RDS.
We use the
Terminal window```

dockerrun\

--rm\

-p5432:5432\

-v $(pwd)/.sst/storage/postgres:/var/lib/postgresql/data\

-ePOSTGRES_USER=postgres\

-ePOSTGRES_PASSWORD=password\

-ePOSTGRES_DB=local\

postgres:16.4

```

The data is saved to the `.sst/storage` directory. So if you restart the dev server, the data will still be there.
We then configure the `dev` property of the `Postgres` component with the settings for the local Postgres instance.
sst.config.ts
```typescript

dev: {

username: "postgres",

password: "password",

database: "local",

port: 5432,

}

```

By providing the `dev` prop for Postgres, SST will use the local Postgres instance and not deploy a new RDS database when running `sst dev`.
It also allows us to access the database through a Resource `link` without having to conditionally check if we are running locally.
index.ts

```typescript


const pool = newPool({




host: Resource.MyPostgres.host,




port: Resource.MyPostgres.port,




user: Resource.MyPostgres.username,




password: Resource.MyPostgres.password,




database: Resource.MyPostgres.database,




});


```

The above will work in both `sst dev` and `sst deploy`.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc", { nat: "ec2" });

const rds = newsst.aws.Postgres("MyPostgres", {

dev: {

username: "postgres",

password: "password",

database: "local",

host: "localhost",

port: 5432,

},

vpc,

});

new sst.aws.Function("MyFunction", {

vpc,

url: true,

link: [rds],

handler: "index.handler",

});

```

View the
* * *

## [Prisma in Lambda](https://sst.dev/docs/examples#prisma-in-lambda)

To use Prisma in a Lambda function you need to

* Generate the Prisma Client with the right architecture
* Copy the generated client to the function
* Run the function inside a VPC

You can set the architecture using the `binaryTargets` option in `prisma/schema.prisma`.
prisma/schema.prisma```

// For x86

binaryTargets = ["native", "rhel-openssl-3.0.x"]

// For ARM

// binaryTargets = ["native", "linux-arm64-openssl-3.0.x"]

```

You can also switch to ARM, just make sure to also change the function architecture in your `sst.config.ts`.
sst.config.ts
```typescript

{

// For ARM

architecture: "arm64"

}

```

To generate the client, you need to run `prisma generate` when you make changes to the schema.
Since this `postinstall` script to the `package.json`.
package.json```

"scripts": {

"postinstall": "prisma generate"

}

```

This runs the command on `npm install`.
We then need to copy the generated client to the function when we deploy.
sst.config.ts
```typescript

{

copyFiles: [{ from: "node_modules/.prisma/client/" }]

}

```

Our function also needs to run inside a VPC, since Prisma doesn’t support the Data API.
sst.config.ts

```typescript

{


vpc


}

```

#### [Prisma in serverless environments](https://sst.dev/docs/examples#prisma-in-serverless-environments)

Prisma is

  1. It doesn’t support Data API, so you need to manage the connection pool on your own.
  2. Without the Data API, your functions need to run inside a VPC.
     * You cannot use `sst dev` without [connecting to the VPC](https://sst.dev/docs/live#using-a-vpc).
  3. Due to the internal architecture of their client, it’s also has slower cold starts.

Instead we recommend using
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc", { nat: "managed" });

const rds = newsst.aws.Postgres("MyPostgres", { vpc });

const api = newsst.aws.Function("MyApi", {

vpc,

url: true,

link: [rds],

// For ARM

// architecture: "arm64",

handler: "index.handler",

copyFiles: [{ from: "node_modules/.prisma/client/" }],

});

return {

api: api.url,

};

```

View the
* * *

## [Puppeteer in Lambda](https://sst.dev/docs/examples#puppeteer-in-lambda)

To use Puppeteer in a Lambda function you need:

  1. Chromium
     * In `sst dev`, we’ll use a locally installed Chromium version.
     * In `sst deploy`, we’ll use the

#### [Chromium version](https://sst.dev/docs/examples#chromium-version)

Since Puppeteer has a preferred version of Chromium, we’ll need to check the version of Chrome that a given version of Puppeteer supports. Head over to the
For example, Puppeteer v23.1.1 supports Chrome for Testing 127.0.6533.119. So, we’ll use the v127 of `@sparticuz/chromium`.
Terminal window```

npminstallpuppeteer-core@23.1.1@sparticuz/chromium@127.0.0

```

#### [Install Chromium locally](https://sst.dev/docs/examples#install-chromium-locally)

To use this locally, you’ll need to install Chromium.
Terminal window```

npx@puppeteer/browsersinstallchromium@latest--path/tmp/localChromium

```

Once installed you’ll see the location of the Chromium binary, `/tmp/localChromium/chromium/mac_arm-1350406/chrome-mac/Chromium.app/Contents/MacOS/Chromium`.
Update this in your Lambda function.
index.ts

```typescript

// This is the path to the local Chromium binary



const YOUR_LOCAL_CHROMIUM_PATH = "/tmp/localChromium/chromium/mac_arm-1350406/chrome-mac/Chromium.app/Contents/MacOS/Chromium";


```

You’ll notice we are using the right binary with the `SST_DEV` environment variable.
index.ts

```typescript

const browser = await puppeteer.launch({

args: chromium.args,

defaultViewport: chromium.defaultViewport,

process.env.SST_DEV

YOUR_LOCAL_CHROMIUM_PATH

chromium.executablePath(),

headless: chromium.headless,

});

```

#### [Deploy](https://sst.dev/docs/examples#deploy)

We don’t need a layer to deploy this because `@sparticuz/chromium` comes with a pre-built binary for Lambda.
As of writing this, `arm64` is not supported by `@sparticuz/chromium`.
We just need to set it in the [`nodejs.install`](https://sst.dev/docs/component/aws/function#nodejs-install).
sst.config.ts

```typescript

{


nodejs: {



install: ["@sparticuz/chromium"]



}


}

```

And on deploy, SST will use the right binary.
You don’t need to use a Lambda layer to use Puppeteer.
We are giving our function more memory and a longer timeout since running Puppeteer can take a while.
sst.config.ts

```typescript

const api = newsst.aws.Function("MyFunction", {

url: true,

memory: "2 GB",

timeout: "15 minutes",

handler: "index.handler",

nodejs: {

install: ["@sparticuz/chromium"],

},

});

return {

url: api.url,

};

```

View the
* * *

## [AWS Lambda Python container](https://sst.dev/docs/examples#aws-lambda-python-container)

Python Lambda function that use large dependencies like `numpy` and `pandas`, can hit the 250MB Lambda package limit. To work around this, you can deploy them as a container image to Lambda.
Container images on Lambda have a limit of 10GB.
In this example, we deploy two functions as container image.
sst.config.ts

```typescript


const base = newsst.aws.Function("PythonFn", {




true,




handler: "./functions/src/functions/api.handler",




runtime: "python3.11",




link: [linkableValue],




url: true,




});


```

Now when you run `sst deploy`, it uses a built-in Dockerfile to build the image and deploy it. You’ll need to have the Docker daemon running.
You need to have the Docker daemon running locally.
To use a custom Dockerfile, you can place a `Dockerfile` in the root of the uv workspace for your function.
sst.config.ts

```typescript

const custom = newsst.aws.Function("PythonFnCustom", {

python: {

container: true,

},

"./custom_dockerfile/src/custom_dockerfile/api.handler",

runtime: "python3.11",

link: [linkableValue],

url: true,

});

```

Here we have a `Dockerfile` in the `custom_dockerfile/` directory.
custom_dockerfile/Dockerfile```

# The python version to use is supplied as an arg from SST

ARG PYTHON_VERSION=3.11

# Use an official AWS Lambda base image for Python

FROM public.ecr.aws/lambda/python:${PYTHON_VERSION}

#

```

The project structure looks something like this.

```

├── sst.config.ts

├── pyproject.toml

└── custom_dockerfile

├── pyproject.toml

├── Dockerfile

└── src

└── custom_dockerfile

└── api.py

```

Locally, you want to set the Python version in your `pyproject.toml` to make sure that `sst dev` uses the same version as `sst deploy`.
sst.config.ts
```typescript

const linkableValue = newsst.Linkable("MyLinkableValue", {

properties: {

foo: "Hello World",

},

});

const base = newsst.aws.Function("PythonFn", {

python: {

container: true,

},

handler: "./functions/src/functions/api.handler",

runtime: "python3.11",

link: [linkableValue],

url: true,

});

const custom = newsst.aws.Function("PythonFnCustom", {

python: {

container: true,

},

handler: "./custom_dockerfile/src/custom_dockerfile/api.handler",

runtime: "python3.11",

link: [linkableValue],

url: true,

});

return {

base: base.url,

custom: custom.url,

};

```

View the
* * *

## [AWS Lambda Python Hugging Face](https://sst.dev/docs/examples#aws-lambda-python-hugging-face)

Uses a Python Lambda container image to deploy a lightweight
Uses the
This is not a production ready example.
This example also shows how it is possible to use custom index resolution to get dependencies from a private pypi server such as the pytorch cpu link. This example also shows how to use a custom Dockerfile to handle complex builds such as installing pytorch and pruning the build size.
sst.config.ts

```typescript


new sst.aws.Function("MyPythonFunction", {



python: {



container: true,



},



handler: "functions/src/functions/api.handler",




runtime: "python3.12",




timeout: "60 seconds",




url: true,



});

```

View the
* * *

## [AWS Lambda Python](https://sst.dev/docs/examples#aws-lambda-python)

SST uses
Any
Builds currently do not tree shake so lots of workspaces can make the build larger than necessary.
In this example we deploy a handler from the `functions/` directory. It depends on shared code from another uv workspace in the `core/` directory.

```

├── sst.config.ts


├── pyproject.toml


├── core


│   ├── pyproject.toml


│   └── src


│       └── core


│           └── __init__.py


└── functions


├── pyproject.toml


└── src


└── functions


├── __init__.py


└── api.py

```

The `handler` is the path to the handler file and the name of the handler function in it.
sst.config.ts

```typescript

new sst.aws.Function("MyPythonFunction", {

handler: "functions/src/functions/api.handler",

runtime: "python3.11",

link: [linkableValue],

url: true,

});

```

SST will traverse up from the handler path and look for the nearest `pyproject.toml`. And will throw an error if it can’t find one.
To access linked resources, you can use the SST SDK.
functions/src/functions/api.py```

from sst import Resource

defhandler(event, context):

print(Resource.MyLinkableValue.foo)

```

Where the `sst` package can be added to your `pyproject.toml`.
functions/pyproject.toml```

[tool.uv.sources]

sst = { git = "<https://github.com/sst/sst.git>", subdirectory = "sdk/python", branch = "dev" }

```

You also want to set the Python version in your `pyproject.toml` to the same version as the one in Lambda.
functions/pyproject.toml```

requires-python = "==3.11.*"

```

This makes sure that your functions work the same in `sst dev` as `sst deploy`.
sst.config.ts
```typescript

const linkableValue = newsst.Linkable("MyLinkableValue", {

properties: {

foo: "Hello World",

},

});

new sst.aws.Function("MyPythonFunction", {

handler: "functions/src/functions/api.handler",

runtime: "python3.11",

link: [linkableValue],

url: true,

});

```

View the
* * *

## [Subscribe to queues](https://sst.dev/docs/examples#subscribe-to-queues-1)

Create an SQS queue, subscribe to it, and publish to it from a function.
sst.config.ts

```typescript


const queue = newsst.aws.Queue("MyQueue");




queue.subscribe("subscriber.handler");




const app = newsst.aws.Function("MyApp", {




handler: "publisher.handler",




link: [queue],




url: true,




});




return {




app: app.url,




queue: queue.url,



};

```

View the
* * *

## [AWS Redis local](https://sst.dev/docs/examples#aws-redis-local)

In this example, we connect to a local Docker Redis instance for dev. While on deploy, we use Redis ElastiCache.
We use the
Terminal window```

dockerrun\

--rm\

-p6379:6379\

-v $(pwd)/.sst/storage/redis:/data\

redis:latest

```

The data is persisted to the `.sst/storage` directory. So if you restart the dev server, the data will still be there.
We then configure the `dev` property of the `Redis` component with the settings for the local Redis server.
sst.config.ts
```typescript

dev: {



host: "localhost",




port: 6379



}

```

By providing the `dev` prop for Redis, SST will use the local Redis server and not deploy a new Redis ElastiCache cluster when running `sst dev`.
It also allows us to access Redis through a Reosurce `link`.
index.ts

```typescript

const client = Resource.MyRedis.host === "localhost"

?newRedis({

host: Resource.MyRedis.host,

port: Resource.MyRedis.port,

})

:newCluster(

[{

host: Resource.MyRedis.host,

port: Resource.MyRedis.port,

}],

{

redisOptions: {

tls: { checkServerIdentity: ()=>undefined },

username: Resource.MyRedis.username,

password: Resource.MyRedis.password,

},

},

);

```

The local Redis server is running in `standalone` mode, whereas on deploy it’ll be in `cluster` mode. So our Lambda function needs to connect using the right config.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc", { nat: "managed" });




const redis = newsst.aws.Redis("MyRedis", {



dev: {



host: "localhost",




port: 6379,



},



vpc,




});




new sst.aws.Function("MyApp", {



vpc,



url: true,



link: [redis],



handler: "index.handler",



});

```

View the
* * *

## [AWS Remix container with Redis](https://sst.dev/docs/examples#aws-remix-container-with-redis)

Creates a hit counter app with Remix and Redis.
This deploys Remix as a Fargate service to ECS and it’s linked to Redis.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

cluster,

link: [redis],

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "npm run dev",

},

});

```

Since our Redis cluster is in a VPC, we’ll need a tunnel to connect to it from our local machine.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
To start your app locally run.
Terminal window```

npxsstdev

```

Now if you go to `http://localhost:5173` you’ll see a counter update as you refresh the page.
Finally, you can deploy it by adding the `Dockerfile` that’s included in this example and running `npx sst deploy --stage production`.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });




const redis = newsst.aws.Redis("MyRedis", { vpc });




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


link: [redis],


loadBalancer: {



ports: [{ listen: "80/http", forward: "3000/http" }],



},


dev: {



command: "npm run dev",



},


});

```

View the
* * *

## [AWS Remix streaming](https://sst.dev/docs/examples#aws-remix-streaming)

Follows the
Uses the `defer` utility to stream data through the `loader` function.
app/routes/_index.tsx```

returndefer({

spongebob,

friends: friendsPromise,

});

```

Then uses the the `Suspense` and `Await` components to render the data.
app/routes/_index.tsx```


<Suspensefallback={<div>Loading...</div>}>




<Awaitresolve={friends}>




{/* ... */}




</Await>




</Suspense>


```

You should see the _friends_ section load after a 3 second delay.
Safari handles streaming differently than other browsers.
Safari uses a _enough_ initial HTML to trigger streaming. This is typically only a problem for demo apps.
Streaming works out of the box with the `Remix` component.
sst.config.ts

```typescript

new sst.aws.Remix("MyWeb");

```

View the
* * *

## [Router and bucket](https://sst.dev/docs/examples#router-and-bucket)

Creates a router that serves static files from the `public` folder of a given bucket.
sst.config.ts

```typescript

// Create a bucket that CloudFront can access



const bucket = newsst.aws.Bucket("MyBucket", {




access: "cloudfront",




});



// Upload the image to the `public` folder



new aws.s3.BucketObjectv2("MyImage", {




bucket: bucket.name,




key: "public/spongebob.svg",




contentType: "image/svg+xml",




source: $asset("spongebob.svg"),



});



const router = newsst.aws.Router("MyRouter", {



routes: {



"/*": {




bucket,




rewrite: { regex: "^/(.*)$", to: "/public/$1" },



},


},



});




return {




image: $interpolate`${router.url}/spongebob.svg`,



};

```

View the
* * *

## [Router and function URL](https://sst.dev/docs/examples#router-and-function-url)

Creates a router that routes all requests to a function with a URL.
sst.config.ts

```typescript

const api = newsst.aws.Function("MyApi", {

handler: "api.handler",

url: true,

});

const bucket = newsst.aws.Bucket("MyBucket", {

access: "public",

});

const router = newsst.aws.Router("MyRouter", {

domain: "router.ion.dev.sst.dev",

routes: {

"/api/*": api.url,

"/*": $interpolate`https://${bucket.domain}`,

},

});

return {

router: router.url,

bucket: bucket.domain,

};

```

View the
* * *

## [AWS Cluster Service Discovery](https://sst.dev/docs/examples#aws-cluster-service-discovery)

In this example, we are connecting to a service running on a cluster using its AWS Cloud Map service host name. This is useful for service discovery.
We are deploying a service to a cluster in a VPC. And we can access it within the VPC using the service’s cloud map hostname.
lambda.ts

```typescript


const reponse = await fetch(`http://${Resource.MyService.service}`);


```

Here we are accessing it through a Lambda function that’s linked to the service and is deployed to the same VPC.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc", { nat: "ec2" });

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

const service = newsst.aws.Service("MyService", { cluster });

new sst.aws.Function("MyFunction", {

vpc,

url: true,

link: [service],

handler: "lambda.handler",

});

```

View the
* * *

## [Sharp in Lambda](https://sst.dev/docs/examples#sharp-in-lambda)

Uses the `logo.png` local file to 100x100 pixels.
sst.config.ts

```typescript

{



nodejs: { install: ["sharp"] }



}

```

We don’t need a layer to deploy this because `sharp` comes with a pre-built binary for Lambda. This is handled by [`nodejs.install`](https://sst.dev/docs/component/aws/function#nodejs-install).
You don’t need to use a Lambda layer to use Sharp.
In dev, this uses the sharp npm package locally.
package.json```

{

"dependencies": {

"sharp": "^0.33.5"

}

}

```

On deploy, SST will use the right binary from the sharp package for the target Lambda architecture.
sst.config.ts
```typescript


const func = newsst.aws.Function("MyFunction", {




url: true,




handler: "index.handler",




nodejs: { install: ["sharp"] },




copyFiles: [{ from: "logo.png" }],




});




return {




url: func.url,



};

```

View the
* * *

## [AWS SolidStart WebSocket endpoint](https://sst.dev/docs/examples#aws-solidstart-websocket-endpoint)

Deploys a SolidStart app with a
Uses the experimental WebSocket support in Nitro.
app.config.ts

```typescript

exportdefaultdefineConfig({

server: {

experimental: {

websocket: true,

},

},

}).addRouter({

name: "ws",

type: "http",

handler: "./src/ws.ts",

target: "server",

base: "/ws",

});

```

Once deployed you can test the `/ws` endpoint and it’ll send a message back after a 3s delay.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


loadBalancer: {



ports: [{ listen: "80/http", forward: "3000/http" }],



},


dev: {



command: "npm run dev",



},


});

```

View the
* * *

## [AWS static site basic auth](https://sst.dev/docs/examples#aws-static-site-basic-auth)

This deploys a simple static site and adds basic auth to it.
This is useful for dev environments where you want to share a static site with your team but ensure that it’s not publicly accessible.
This works by injecting some code into a CloudFront function that checks the basic auth header and matches it against the `USERNAME` and `PASSWORD` secrets.
sst.config.ts

```typescript

{

injection: $interpolate`

if (

!event.request.headers.authorization

|| event.request.headers.authorization.value !== "Basic ${basicAuth}"

) {

return {

statusCode: 401,

headers: {

"www-authenticate": { value: "Basic" }

}

};

}`,

}

```

To deploy this, you need to first set the `USERNAME` and `PASSWORD` secrets.
Terminal window```

sstsecretsetUSERNAMEmy-username

sstsecretsetPASSWORDmy-password

```

If you are deploying this to preview environments, you might want to set the secrets using the [`--fallback`](https://sst.dev/docs/reference/cli#secret) flag.
sst.config.ts
```typescript

const username = newsst.Secret("USERNAME");

const password = newsst.Secret("PASSWORD");

const basicAuth = $resolve([username.value, password.value]).apply(

([username, password]) =>

Buffer.from(`${username}:${password}`).toString("base64")

);

new sst.aws.StaticSite("MySite", {

path: "site",

// Don't password protect prod

edge: $app.stage!=="production"

? {

viewerRequest: {

injection: $interpolate`

if (

!event.request.headers.authorization

|| event.request.headers.authorization.value !== "Basic ${basicAuth}"

) {

return {

statusCode: 401,

headers: {

"www-authenticate": { value: "Basic" }

}

};

}`,

},

}

:undefined,

});

```

View the
* * *

## [AWS static site](https://sst.dev/docs/examples#aws-static-site)

Deploy a simple HTML file as a static site with S3 and CloudFront. The website is stored in the `site/` directory.
sst.config.ts

```typescript


new sst.aws.StaticSite("MySite", {




path: "site",



});

```

View the
* * *

## [AWS SvelteKit container with Redis](https://sst.dev/docs/examples#aws-sveltekit-container-with-redis)

Creates a hit counter app with SvelteKit and Redis.
This deploys SvelteKit as a Fargate service to ECS and it’s linked to Redis.
sst.config.ts

```typescript

new sst.aws.Service("MyService", {

cluster,

link: [redis],

loadBalancer: {

ports: [{ listen: "80/http", forward: "3000/http" }],

},

dev: {

command: "npm run dev",

},

});

```

Since our Redis cluster is in a VPC, we’ll need a tunnel to connect to it from our local machine.
Terminal window```

sudonpxssttunnelinstall

```

This needs _sudo_ to create a network interface on your machine. You’ll only need to do this once on your machine.
To start your app locally run.
Terminal window```

npxsstdev

```

Now if you go to `http://localhost:5173` you’ll see a counter update as you refresh the page.
Finally, you can deploy it by adding the `Dockerfile` that’s included in this example and running `npx sst deploy --stage production`.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc", { bastion: true });




const redis = newsst.aws.Redis("MyRedis", { vpc });




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




new sst.aws.Service("MyService", {



cluster,


link: [redis],


loadBalancer: {



ports: [{ listen: "80/http", forward: "3000/http" }],



},


dev: {



command: "npm run dev",



},


});

```

View the
* * *

## [Swift in Lambda](https://sst.dev/docs/examples#swift-in-lambda)

Deploys a simple Swift application to Lambda using the `al2023` runtime.
Building this function requires Docker.
Check out the README in the repo for more details.
sst.config.ts

```typescript

const swift = newsst.aws.Function("Swift", {

runtime: "provided.al2023",

architecture: process.arch === "arm64" ? "arm64" : "x86_64",

bundle: build("app"),

handler: "bootstrap",

url: true,

});

const router = newsst.aws.Router("SwiftRouter", {

routes: {

"/*": swift.url,

},

domain: "swift.dev.sst.dev",

});

return {

url: router.url,

};

```

View the
* * *

## [T3 Stack in AWS](https://sst.dev/docs/examples#t3-stack-in-aws)

Deploy
This example was created using `create-t3-app` and the following options: tRPC, Drizzle, no auth, Tailwind, Postgres, and the App Router.
Instead of a local database, we’ll be using an RDS Postgres database.
src/server/db/index.ts

```typescript


const pool = newPool({




Resource.MyPostgres.host,




Resource.MyPostgres.port,




Resource.MyPostgres.username,




Resource.MyPostgres.password,




Resource.MyPostgres.database,




});


```

Similarly, for Drizzle Kit.
drizzle.config.ts

```typescript

exportdefault {

schema: "./src/server/db/schema.ts",

dialect: "postgresql",

dbCredentials: {

ssl: {

rejectUnauthorized: false,

},

host: Resource.MyPostgres.host,

port: Resource.MyPostgres.port,

user: Resource.MyPostgres.username,

password: Resource.MyPostgres.password,

database: Resource.MyPostgres.database,

},

tablesFilter: ["aws-t3_*"],

} satisfiesConfig;

```

In our Next.js app we can access our Postgres database because we [link them](https://sst.dev/docs/linking/) both. We don’t need to use our `.env` files.
sst.config.ts

```typescript


const rds = newsst.aws.Postgres("MyPostgres", { vpc, proxy: true });




new sst.aws.Nextjs("MyWeb", {



vpc,


link: [rds]


});

```

To run this in dev mode run:
Terminal window```

npminstall

npxsstdev

```

It’ll take a few minutes to deploy the database and the VPC.
This also starts a tunnel to let your local machine connect to the RDS Postgres database. Make sure you have it installed, you only need to do this once for your local machine.
Terminal window```


sudonpxssttunnelinstall


```

Now in a new terminal you can run the database migrations.
Terminal window```

npmrundb:push

```

We also have the Drizzle Studio start automatically in dev mode under the **Studio** tab.
sst.config.ts
```typescript


new sst.x.DevCommand("Studio", {



link: [rds],


dev: {



command: "npx drizzle-kit studio",



},


});

```

And to make sure our credentials are available, we update our `package.json` with the [`sst shell`](https://sst.dev/docs/reference/cli) CLI.
package.json```

"db:generate": "sst shell drizzle-kit generate",

"db:migrate": "sst shell drizzle-kit migrate",

"db:push": "sst shell drizzle-kit push",

"db:studio": "sst shell drizzle-kit studio",

```

So running `npm run db:push` will run Drizzle Kit with the right credentials.
To deploy this to production run:
Terminal window```


npxsstdeploy--stageproduction


```

Then run the migrations.
Terminal window```

npxsstshell--stageproductionnpxdrizzle-kitpush

```

If you are running this locally, you’ll need to have a tunnel running.
Terminal window```


npxssttunnel--stageproduction


```

If you are doing this in a CI/CD pipeline, you’d want your build containers to be in the same VPC.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc", { bastion: true, nat: "ec2" });

const rds = newsst.aws.Postgres("MyPostgres", { vpc, proxy: true });

new sst.aws.Nextjs("MyWeb", {

vpc,

link: [rds]

});

new sst.x.DevCommand("Studio", {

link: [rds],

dev: {

command: "npx drizzle-kit studio",

},

});

```

View the
* * *

## [AWS Task Cron](https://sst.dev/docs/examples#aws-task-cron)

Use the [`Task`](https://sst.dev/docs/component/aws/task) and [`Cron`](https://sst.dev/docs/component/aws/cron) components for long running background tasks.
We have a node script that we want to run in `index.mjs`. It’ll be deployed as a Docker container using `Dockerfile`.
It’ll be invoked by a cron job that runs every 2 minutes.
sst.config.ts

```typescript


new sst.aws.Cron("MyCron", {



task,



schedule: "rate(2 minutes)"



});

```

When this is run in `sst dev`, the task is executed locally using `dev.command`.
sst.config.ts

```typescript

dev: {

command: "node index.mjs"

}

```

To deploy, you need the Docker daemon running.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket");




const vpc = newsst.aws.Vpc("MyVpc");




const cluster = newsst.aws.Cluster("MyCluster", { vpc });




const task = newsst.aws.Task("MyTask", {




cluster,




link: [bucket],



dev: {



command: "node index.mjs",



},



});




new sst.aws.Cron("MyCron", {



task,



schedule: "rate(2 minutes)",



});

```

View the
* * *

## [AWS Task](https://sst.dev/docs/examples#aws-task)

Use the [`Task`](https://sst.dev/docs/component/aws/task) component to run background tasks.
We have a node script that we want to run in `image/index.mjs`. It’ll be deployed as a Docker container using `image/Dockerfile`.
We also have a function that the task is linked to. It uses the [SDK](https://sst.dev/docs/reference/sdk/) to start the task.
index.ts

```typescript

import { Resource } from"sst";

import { task } from"sst/aws/task";

export const handler = async () => {

ret = await task.run(Resource.MyTask);

return {

statusCode: 200,

body: JSON.stringify(ret, null, 2),

};

};

```

When this is run in `sst dev`, the task is executed locally using `dev.command`.
sst.config.ts

```typescript

dev: {



command: "node index.mjs"



}

```

To deploy, you need the Docker daemon running.
sst.config.ts

```typescript

const bucket = newsst.aws.Bucket("MyBucket");

const vpc = newsst.aws.Vpc("MyVpc", { nat: "ec2" });

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

const task = newsst.aws.Task("MyTask", {

cluster,

link: [bucket],

image: {

context: "image",

},

dev: {

command: "node index.mjs",

},

});

new sst.aws.Function("MyApp", {

vpc,

url: true,

link: [task],

handler: "index.handler",

});

```

View the
* * *

## [Subscribe to topics](https://sst.dev/docs/examples#subscribe-to-topics)

Create an SNS topic, publish to it from a function, and subscribe to it with a function and a queue.
sst.config.ts

```typescript


const queue = newsst.aws.Queue("MyQueue");




queue.subscribe("subscriber.handler");




const topic = newsst.aws.SnsTopic("MyTopic");




topic.subscribe("MySubscriber1", "subscriber.handler", {});




topic.subscribeQueue("MySubscriber2", queue.arn);




const app = newsst.aws.Function("MyApp", {




handler: "publisher.handler",




link: [topic],




url: true,




});




return {




app: app.url,




topic: topic.name,



};

```

View the
* * *

## [Vector search](https://sst.dev/docs/examples#vector-search)

Store and search for vector data using the Vector component. Includes a seeder API that uses an LLM to generate embeddings for some movies and optionally their posters.
Once seeded, you can call the search API to query the vector database.
sst.config.ts

```typescript

const OpenAiApiKey = newsst.Secret("OpenAiApiKey");

const vector = newsst.aws.Vector("MyVectorDB", {

dimension: 1536,

});

const seeder = newsst.aws.Function("Seeder", {

handler: "index.seeder",

link: [OpenAiApiKey, vector],

copyFiles: [

{ from: "iron-man.jpg", to: "iron-man.jpg" },

{

from: "black-widow.jpg",

to: "black-widow.jpg",

},

{

from: "spider-man.jpg",

to: "spider-man.jpg",

},

{ from: "thor.jpg", to: "thor.jpg" },

{

from: "captain-america.jpg",

to: "captain-america.jpg",

},

],

url: true,

});

const app = newsst.aws.Function("MyApp", {

handler: "index.app",

link: [OpenAiApiKey, vector],

url: true,

});

return { seeder: seeder.url, app: app.url };

```

View the
* * *

## [React SPA with Vite](https://sst.dev/docs/examples#react-spa-with-vite)

Deploy a React single-page app (SPA) with Vite to S3 and CloudFront.
sst.config.ts

```typescript


new sst.aws.StaticSite("Web", {



build: {



command: "pnpm run build",




output: "dist",



},


});

```

View the
* * *

## [Cloudflare Cron](https://sst.dev/docs/examples#cloudflare-cron)

This example creates a Cloudflare Worker that runs on a schedule.
sst.config.ts

```typescript

const cron = newsst.cloudflare.Cron("Cron", {

job: "index.ts",

schedules: ["**** *"]

});

return {};

```

View the
* * *

## [Cloudflare KV](https://sst.dev/docs/examples#cloudflare-kv)

This example creates a Cloudflare KV namespace and links it to a worker. Now you can use the SDK to interact with the KV namespace in your worker.
sst.config.ts

```typescript


const storage = newsst.cloudflare.Kv("MyStorage");




const worker = newsst.cloudflare.Worker("Worker", {




url: true,




link: [storage],




handler: "index.ts",




});




return {




url: worker.url,



};

```

View the
* * *

## [Link multiple secrets](https://sst.dev/docs/examples#link-multiple-secrets)

You might have multiple secrets that need to be used across your app. It can be tedious to create a new secret and link it to each function or resource.
A common pattern to addresses this is to create an object with all your secrets and then link them all at once. Now when you have a new secret, you can add it to the object and it will be automatically available to all your resources.
sst.config.ts

```typescript

// Manage all secrets together

const secrets = {

secret1: newsst.Secret("Secret1", "some-secret-value-1"),

secret2: newsst.Secret("Secret2", "some-secret-value-2"),

};

const allSecrets = Object.values(secrets);

const bucket = newsst.aws.Bucket("MyBucket");

const api = newsst.aws.Function("MyApi", {

link: [bucket, ...allSecrets],

handler: "index.handler",

url: true,

});

return {

url: api.url,

};

```

View the
* * *

## [Default function props](https://sst.dev/docs/examples#default-function-props)

Set default props for all the functions in your app using the global [`$transform`](https://sst.dev/docs/reference/global/#transform).
sst.config.ts

```typescript


$transform(sst.aws.Function, (args)=> {




args.runtime="nodejs14.x";




args.environment= {




FOO: "BAR",



};


});



new sst.aws.Function("MyFunction", {




handler: "index.ts",



});

```

View the
* * *

## [Vercel domains](https://sst.dev/docs/examples#vercel-domains)

Creates a router that uses domains purchased through and hosted in your Vercel account. Ensure the `VERCEL_API_TOKEN` and `VERCEL_TEAM_ID` environment variables are set.
sst.config.ts

```typescript

const router = newsst.aws.Router("MyRouter", {

domain: {

name: "ion.sst.moe",

dns: sst.vercel.dns({ domain: "sst.moe" }),

},

routes: {

"/*": "<https://sst.dev>",

},

});

return {

router: router.url,

};

```

View the

[Skip to content](https://sst.dev/docs/aws-accounts#_top)

# Set up AWS Accounts

Unsurprisingly there are multiple ways to set up AWS accounts. And unfortunately the default process misses a few things that’ll likely make this a lot easier for your team.
If you are using IAM users or have credential files, this guide is for you.
* * *
The ideal setup is to have multiple AWS accounts grouped under a single AWS Organization. While your team authenticates through SSO to access the Console and the CLI.
While this sounds complicated, it’s a one time process that you’ll never have to think about again.
Let’s get started.
* * *

## [Management account](https://sst.dev/docs/aws-accounts#management-account)

The first step is to

  1. Start by using a **work email alias**. For example `aws@acme.com`. This’ll forward to your real email. It allows you to give other people access to it in the future.
  2. The **account name** should be your company name, for example `acme`.
  3. Enter your **billing info** and **confirm your identity**.
  4. Choose **basic support**. You can upgrade this later.

Once you’re done you should be able to login and access the AWS Console.
These credentials are overly powerful. You should rarely ever need them again. Feel free to throw away the password after completing this guide. You can always do a password reset if it’s needed.
The Management account is what you’ll use to manage the users in your organization.
This account won’t have anything deployed to it besides the IAM Identity Center which is how we’ll manage the users in our organization.
* * *

### [AWS Organization](https://sst.dev/docs/aws-accounts#aws-organization)

Next, we’ll create an organization. This allows you to manage multiple AWS accounts together. We’ll need this as we create separate accounts for dev and prod.
Search **AWS Organization** in the search bar to go to its dashboard and click **Create an organization**.
You’ll see that the management account is already in the organization.
* * *

### [IAM Identity Center](https://sst.dev/docs/aws-accounts#iam-identity-center)

Now let’s enable IAM Identity Center.

  1. Search **IAM Identity Center** and go to its dashboard. Click **Enable**.
Make a note of the region you’re in for the IAM Identity Center.
This’ll be created in one region and you cannot change it. However, it doesn’t matter too much which one it is. You’ll just need to navigate to that region when you are trying to find this again.
  2. Click **Enable**. This will give your organization a unique URL to login.
Make a note of the URL that IAM Identity Center gives you.
This is auto-generated but you can click **Customize** to select a unique name. You’ll want to bookmark this for later.

* * *

## [Root user](https://sst.dev/docs/aws-accounts#root-user)

Now we’ll create a root user in IAM Identity Center.

  1. Click **Users** on the left and then **Add user** to create a user for yourself. Make your username your work email, for example `dax@acme.com`, and fill out the required fields.
  2. Skip adding the user to groups.
  3. Finish creating the user.

We’ve created the user. Now let’s give it access to our management account.
* * *

### [User access](https://sst.dev/docs/aws-accounts#user-access)

Go to the left panel and click **AWS Accounts**.

  1. Select your management account. It should be tagged as such. And click **Assign users or groups**.
  2. Select the Users tab, make sure your user is selected and hit **Next**.
  3. Now we’ll need to create a new permission set. We need to do this once. Click **Create permission set**.
  4. In the new tab select **Predefined permission set** and **AdministratorAccess**. Click **Next**.
  5. Increase the session duration to 12 hours. This is the most convenient option. Click **Next** and then **Create**.
  6. Close the tab, return to the previous one and hit the refresh icon. Select **AdministratorAccess** and click **Next** and then **Submit**.

This might seem complicated but all we did was grant the user an _AdministratorAccess role_ into the management account.
Now you’re ready to log in to your user account.
* * *

### [Login](https://sst.dev/docs/aws-accounts#login)

Check your email and you should have an invite.

  1. **Accept the invite** and **create a new password**. Be sure to save it in your password manager. This is important because this account has access to the management account.
If you already have an SSO provider, like Google you can allow your team to _Login with Google_. Let us know if you’d like us to document that as well.
  2. Sign in and you should see your organization with a **list of accounts** below it.
You currently only have access to the management account we created above. So click it and you should see the AdministratorAccess role.
  3. Click **Management Console** to login to the AWS Console.

You’re now done setting up the root user account!
* * *

## [Dev and prod accounts](https://sst.dev/docs/aws-accounts#dev-and-prod-accounts)

As mentioned earlier, your management account isn’t meant to deploy any resources. It’s meant to manage users.
So a good initial setup is to create separate `dev` and `production` accounts. This helps create some isolation. The `dev` account will be shared between your team while the `production` account is just for production.
You can also create a staging account or an account per developer but we’ll start simple.
* * *
Navigate back to **AWS Organizations** by searching for it.

  1. Click **Add an AWS account**.
  2. For the account name append `-dev` to whatever you called your management account. For example, `acme-dev`.
  3. For the email address choose a new email alias. If you’re using Google for email, you can do `aws+dev@acme.com` and it’ll still go to your `aws@acme.com` email.
  4. Click **Create AWS account**.

**Repeat this step** and create the `-production` as well. So you should now have an `acme-dev` and an `acme-production`.
It’ll take a few seconds to finish creating.
* * *

### [Assign users](https://sst.dev/docs/aws-accounts#assign-users)

Once it’s done head over to **IAM Identity Center** to grant your user access to these accounts.

  1. Select the **AWS Accounts** tab on the left.
  2. Select your newly created `acme-dev` and `acme-production` accounts and click **Assign users or groups**.
  3. In the **Users** tab select your user and click **Next**.
  4. Select the **AdministratorAccess** permission set and click **Next** and **Submit**.

Now you can go back to your SSO URL. You should now see three different accounts and you’ll be able to login to whichever one you want.
You can find your SSO URL by clicking **Dashboard** on the left.
You can create additional users and add them to these accounts using the steps above. You can reuse the role or create one with stricter permissions.
Next, let’s configure the AWS CLI and SST to use this setup.
* * *

## [Configure AWS CLI](https://sst.dev/docs/aws-accounts#configure-aws-cli)

The great thing about this setup is that you no longer need to generate AWS IAM credentials for your local machine, you can just use SSO. This is both simpler and more secure.
You can
All you need is a single configuration file for the AWS CLI, SST, or any random scripts you want to run. And there will never be any long lived credentials stored on your machine.
* * *

  1. Add the following block to a `~/.aws/config` file.
~/.aws/config```

[sso-session acme]

sso_start_url=<https://acme.awsapps.com/start>

sso_region=us-east-1

```

Make sure to replace the `sso_start_url` with your SSO URL that you bookmarked. And set the region where you created IAM Identity Center as the `sso_region`.
  2. Add an entry for each environment, in this case `dev` and `production`.
~/.aws/config```

[profile acme-dev]

sso_session=acme

sso_account_id=<account-id>

sso_role_name=AdministratorAccess

region=us-east-1

[profile acme-production]

sso_session=acme

sso_account_id=<account-id>

sso_role_name=AdministratorAccess

region=us-east-1

```

You can find the account ID from your SSO login url. If you expand the account you will see it listed with a `#` sign.
The region specified in the config is the default region that the CLI will use when one isn’t specified.
With this setup you won’t need to save your AWS credentials locally.
And the role name is the one we created above. If you created a different role, you’d need to change this.
  3. Now you can login by running.
Terminal window```

awsssologin--sso-session=acme

```

This’ll open your browser and prompt you to allow access. The sessions will last 12 hours, as we had configured previously.
If you’re using Windows with WSL, you can add a script to open the login browser of the host machine.
View script
login.sh```

# !/bin/bash

ifgrep-qWSL/proc/version; then

exportBROWSER=wslview

fi

awsssologin--sso-session=acme

```

  4. Optionally, for Node.js projects, it can be helpful to add this to a `package.json` script so your team can just run `npm run sso` to login.
package.json```

"scripts": {

"sso": "aws sso login --sso-session=acme"

}

```

  5. Finally, test that everything is working with a simple CLI command that targets your dev account.
Terminal window```

awsstsget-caller-identity--profile=acme-dev

```

Next, let’s configure SST to use these profiles.
* * *

## [Configure SST](https://sst.dev/docs/aws-accounts#configure-sst)

In your `sst.config.ts` file check which stage you are deploying to and return the right profile.
sst.config.ts

```typescript


exportdefault$config({




app(input) {




return {




name: "my-sst-app",




home: "aws",



providers: {


aws: {



profile: input.stage==="production"?"acme-production":"acme-dev"



}


}


};


},



asyncrun() {



// Your resources


}


});

```

This will use the `acme-production` profile just for production and use `acme-dev` for everything else.
The `AWS_PROFILE` environment variable will override the profile set in your `sst.config.ts`.
If you’ve configured AWS credentials previously through the `AWS_PROFILE` environment variable or through a `.env` file, it will override the profile set in your `sst.config.ts`. So make sure to remove any references to `AWS_PROFILE`.
Now to deploy to your production account you just pass in the stage.
Terminal window```

sstdeploy--stageproduction

```

And we are done!
* * *
To summarize, here what we’ve created:
  1. A management account to manage the users in our organization.
  2. A root user that can login to the management account.
  3. Dev and production accounts for our apps.
  4. Finally, given the root user access to both accounts.


You can extend these by adding more users, or adding additional accounts, or modifying the roles you grant.


[Skip to content](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#_top)
# RealtimeLambdaSubscriber
The `RealtimeLambdaSubscriber` component is internally used by the `Realtime` component to add subscriptions to the 
This component is not intended to be created directly.
You’ll find this component returned by the `subscribe` method of the `Realtime` component.
* * *
## [Constructor](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#constructor)
```

newRealtimeLambdaSubscriber(name, args, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#parameters)
  * `name` `string`
  * `args` [`Args`](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#args)
  * `opts?`


## [Properties](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#properties)
### [nodes](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#nodes)
**Type** `Object`
  * [`permission`](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#nodes-permission)
  * [`rule`](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#nodes-rule)
  * [`function`](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#nodes-function)


The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.
####  [nodes.permission](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#nodes-permission)
**Type**
The Lambda permission.
####  [nodes.rule](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#nodes-rule)
**Type**
The IoT Topic rule.
####  [nodes.function](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#nodes-function)
**Type** `Output``<`[`Function`](https://sst.dev/docs/component/aws/function)`>`
The Lambda function that’ll be notified.
## [Args](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#args)
### [filter](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#filter)
**Type** `Input``<``string``>`
Filter the topics that’ll be processed by the subscriber.
Learn more about 
Subscribe to a specific topic.
```

{

filter: `${$app.name}/${$app.stage}/chat/room1`

}

```

Subscribe to all topics under a prefix.
```

{

filter: `${$app.name}/${$app.stage}/chat/#`

}

```

### [iot](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#iot)
**Type** `Input``<``Object``>`
  * [`name`](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#iot-name)


The IoT WebSocket server to use.
####  [iot.name](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#iot-name)
**Type** `Input``<``string``>`
The name of the Realtime component.
### [subscriber](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#subscriber)
**Type** `Input``<``string`` | `[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`>`
The subscriber function.
### [transform?](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#transform)
**Type** `Object`
  * [`topicRule?`](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#transform-topicrule)


[Transform](https://sst.dev/docs/components#transform) how this subscription creates its underlying resources.
####  [transform.topicRule?](https://sst.dev/docs/component/aws/realtime-lambda-subscriber#transform-topicrule)
**Type** ` | ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the IoT Topic rule resource.


[Skip to content](https://sst.dev/docs/component/aws/cluster#_top)
# Cluster
The `Cluster` component lets you create an `Service` and `Task` components to it.
sst.config.ts
```typescript


const vpc = newsst.aws.Vpc("MyVpc");




const cluster = newsst.aws.Cluster("MyCluster", { vpc });


```

Once created, you can add the following to it:

  1. `Service`: These are containers that are always running, like web or application servers. They automatically restart if they fail.
  2. `Task`: These are containers that are used for long running asynchronous work, like data processing.

* * *

## [Constructor](https://sst.dev/docs/component/aws/cluster#constructor)

```


newCluster(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cluster#parameters)

* `name` `string`
* `args` [`ClusterArgs`](https://sst.dev/docs/component/aws/cluster#clusterargs)
* `opts?`

## [ClusterArgs](https://sst.dev/docs/component/aws/cluster#clusterargs)

### [transform?](https://sst.dev/docs/component/aws/cluster#transform)

**Type** `Object`

* [`cluster?`](https://sst.dev/docs/component/aws/cluster#transform-cluster)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.cluster?](https://sst.dev/docs/component/aws/cluster#transform-cluster)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the ECS Cluster resource.

### [vpc](https://sst.dev/docs/component/aws/cluster#vpc)

**Type** [`Vpc`](https://sst.dev/docs/component/aws/vpc)`| ``Input``<``Object``>`

* [`cloudmapNamespaceId?`](https://sst.dev/docs/component/aws/cluster#vpc-cloudmapnamespaceid)
* [`cloudmapNamespaceName?`](https://sst.dev/docs/component/aws/cluster#vpc-cloudmapnamespacename)
* [`containerSubnets?`](https://sst.dev/docs/component/aws/cluster#vpc-containersubnets)
* [`id`](https://sst.dev/docs/component/aws/cluster#vpc-id)
* [`loadBalancerSubnets`](https://sst.dev/docs/component/aws/cluster#vpc-loadbalancersubnets)
* [`securityGroups`](https://sst.dev/docs/component/aws/cluster#vpc-securitygroups)

The VPC to use for the cluster.
Create a `Vpc` component.
sst.config.ts

```typescript

const myVpc = newsst.aws.Vpc("MyVpc");

```

Or reference an existing VPC.
sst.config.ts

```typescript


const myVpc = sst.aws.Vpc.get("MyVpc", {




id: "vpc-12345678901234567"




});


```

And pass it in.

```

{



vpc: myVpc



}

```

By default, both the load balancer and the services are deployed in public subnets. The above is equivalent to:

```

{


vpc: {



id: myVpc.id,




securityGroups: myVpc.securityGroups,




containerSubnets: myVpc.publicSubnets,




loadBalancerSubnets: myVpc.publicSubnets,




cloudmapNamespaceId: myVpc.nodes.cloudmapNamespace.id,




cloudmapNamespaceName: myVpc.nodes.cloudmapNamespace.name



}


}

```

#### [vpc.cloudmapNamespaceId?](https://sst.dev/docs/component/aws/cluster#vpc-cloudmapnamespaceid)

**Type** `Input``<``string``>`
The ID of the Cloud Map namespace to use for the service.

#### [vpc.cloudmapNamespaceName?](https://sst.dev/docs/component/aws/cluster#vpc-cloudmapnamespacename)

**Type** `Input``<``string``>`
The name of the Cloud Map namespace to use for the service.

#### [vpc.containerSubnets?](https://sst.dev/docs/component/aws/cluster#vpc-containersubnets)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of subnet IDs in the VPC to place the containers in.

#### [vpc.id](https://sst.dev/docs/component/aws/cluster#vpc-id)

**Type** `Input``<``string``>`
The ID of the VPC.

#### [vpc.loadBalancerSubnets](https://sst.dev/docs/component/aws/cluster#vpc-loadbalancersubnets)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of subnet IDs in the VPC to place the load balancer in.

#### [vpc.securityGroups](https://sst.dev/docs/component/aws/cluster#vpc-securitygroups)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of VPC security group IDs for the service.

## [Properties](https://sst.dev/docs/component/aws/cluster#properties)

### [id](https://sst.dev/docs/component/aws/cluster#id)

**Type** `Output``<``string``>`
The cluster ID.

### [nodes](https://sst.dev/docs/component/aws/cluster#nodes)

**Type** `Object`

* [`cluster`](https://sst.dev/docs/component/aws/cluster#nodes-cluster)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.cluster](https://sst.dev/docs/component/aws/cluster#nodes-cluster)

**Type** `Output``<``>`
The Amazon ECS Cluster.

## [Methods](https://sst.dev/docs/component/aws/cluster#methods)

### [static get](https://sst.dev/docs/component/aws/cluster#static-get)

```


Cluster.get(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cluster#parameters-1)

* `name` `string`
The name of the component.
* `args` [`ClusterGetArgs`](https://sst.dev/docs/component/aws/cluster#clustergetargs)
The arguments to get the cluster.
* `opts?`

**Returns** [`Cluster`](https://sst.dev/docs/component/aws/)
Reference an existing ECS Cluster with the given ID. This is useful when you create a cluster in one stage and want to share it in another. It avoids having to create a new cluster in the other stage.
You can use the `static get` method to share cluster across stages.
Imagine you create a cluster in the `dev` stage. And in your personal stage `frank`, instead of creating a new cluster, you want to share the same cluster from `dev`.
sst.config.ts

```typescript

const cluster = $app.stage === "frank"

? sst.aws.Cluster.get("MyCluster", {

id: "arn:aws:ecs:us-east-1:123456789012:cluster/app-dev-MyCluster",

vpc,

})

:new sst.aws.Cluster("MyCluster", { vpc });

```

Here `arn:aws:ecs:us-east-1:123456789012:cluster/app-dev-MyCluster` is the ID of the cluster created in the `dev` stage. You can find these by outputting the cluster ID in the `dev` stage.
sst.config.ts

```typescript


return {




id: cluster.id,



};

```

## [ClusterGetArgs](https://sst.dev/docs/component/aws/cluster#clustergetargs)

### [id](https://sst.dev/docs/component/aws/cluster#id-1)

**Type** `Input``<``string``>`
The ID of the cluster.

### [vpc](https://sst.dev/docs/component/aws/cluster#vpc-1)

**Type** [`Vpc`](https://sst.dev/docs/component/aws/vpc)`| ``Input``<``Object``>`

* [`cloudmapNamespaceId?`](https://sst.dev/docs/component/aws/cluster#vpc-cloudmapnamespaceid-1)
* [`cloudmapNamespaceName?`](https://sst.dev/docs/component/aws/cluster#vpc-cloudmapnamespacename-1)
* [`containerSubnets?`](https://sst.dev/docs/component/aws/cluster#vpc-containersubnets-1)
* [`id`](https://sst.dev/docs/component/aws/cluster#vpc-id-1)
* [`loadBalancerSubnets`](https://sst.dev/docs/component/aws/cluster#vpc-loadbalancersubnets-1)
* [`securityGroups`](https://sst.dev/docs/component/aws/cluster#vpc-securitygroups-1)

The VPC used for the cluster.

#### [vpc.cloudmapNamespaceId?](https://sst.dev/docs/component/aws/cluster#vpc-cloudmapnamespaceid-1)

**Type** `Input``<``string``>`
The ID of the Cloud Map namespace to use for the service.

#### [vpc.cloudmapNamespaceName?](https://sst.dev/docs/component/aws/cluster#vpc-cloudmapnamespacename-1)

**Type** `Input``<``string``>`
The name of the Cloud Map namespace to use for the service.

#### [vpc.containerSubnets?](https://sst.dev/docs/component/aws/cluster#vpc-containersubnets-1)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of subnet IDs in the VPC to place the containers in.

#### [vpc.id](https://sst.dev/docs/component/aws/cluster#vpc-id-1)

**Type** `Input``<``string``>`
The ID of the VPC.

#### [vpc.loadBalancerSubnets](https://sst.dev/docs/component/aws/cluster#vpc-loadbalancersubnets-1)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of subnet IDs in the VPC to place the load balancer in.

#### [vpc.securityGroups](https://sst.dev/docs/component/aws/cluster#vpc-securitygroups-1)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of VPC security group IDs for the service.

[Skip to content](https://sst.dev/docs/component/aws/providers/function-environment-update#_top)

# FunctionEnvironmentUpdate

The `FunctionEnvironmentUpdate` component is internally used by the `Function` component to update the environment variables of a function.
This component is not intended to be created directly.
You’ll find this component returned by the `addEnvironment` method of the `Function` component.
* * *

## [Constructor](https://sst.dev/docs/component/aws/providers/function-environment-update#constructor)

```


newFunctionEnvironmentUpdate(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/providers/function-environment-update#parameters)

* `name` `string`
* `args` [`FunctionEnvironmentUpdateInputs`](https://sst.dev/docs/component/aws/providers/function-environment-update#functionenvironmentupdateinputs)
* `opts?`

## [FunctionEnvironmentUpdateInputs](https://sst.dev/docs/component/aws/providers/function-environment-update#functionenvironmentupdateinputs)

### [environment](https://sst.dev/docs/component/aws/providers/function-environment-update#environment)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
The environment variables to update.

### [functionName](https://sst.dev/docs/component/aws/providers/function-environment-update#functionname)

**Type** `Input``<``string``>`
The name of the function to update.

### [region](https://sst.dev/docs/component/aws/providers/function-environment-update#region)

**Type** `Input``<``string``>`
The region of the function to update.

[Skip to content](https://sst.dev/docs/component/aws/queue-lambda-subscriber#_top)

# QueueLambdaSubscriber

The `QueueLambdaSubscriber` component is internally used by the `Queue` component to add a consumer to
This component is not intended to be created directly.
You’ll find this component returned by the `subscribe` method of the `Queue` component.
* * *

## [Constructor](https://sst.dev/docs/component/aws/queue-lambda-subscriber#constructor)

```


newQueueLambdaSubscriber(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/queue-lambda-subscriber#parameters)

* `name` `string`
* `args` [`Args`](https://sst.dev/docs/component/aws/queue-lambda-subscriber#args)
* `opts?`

## [Properties](https://sst.dev/docs/component/aws/queue-lambda-subscriber#properties)

### [nodes](https://sst.dev/docs/component/aws/queue-lambda-subscriber#nodes)

**Type** `Object`

* [`eventSourceMapping`](https://sst.dev/docs/component/aws/queue-lambda-subscriber#nodes-eventsourcemapping)
* [`function`](https://sst.dev/docs/component/aws/queue-lambda-subscriber#nodes-function)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.eventSourceMapping](https://sst.dev/docs/component/aws/queue-lambda-subscriber#nodes-eventsourcemapping)

**Type**
The Lambda event source mapping.

#### [nodes.function](https://sst.dev/docs/component/aws/queue-lambda-subscriber#nodes-function)

**Type** `Output``<`[`Function`](https://sst.dev/docs/component/aws/function)`>`
The Lambda function that’ll be notified.

## [Args](https://sst.dev/docs/component/aws/queue-lambda-subscriber#args)

### [batch?](https://sst.dev/docs/component/aws/queue-lambda-subscriber#batch)

**Type** `Input``<``Object``>`

* [`partialResponses?`](https://sst.dev/docs/component/aws/queue-lambda-subscriber#batch-partialresponses)
* [`size?`](https://sst.dev/docs/component/aws/queue-lambda-subscriber#batch-size)
* [`window?`](https://sst.dev/docs/component/aws/queue-lambda-subscriber#batch-window)

**Default** `{size: 10, window: “20 seconds”, partialResponses: false}`
Configure batch processing options for the consumer function.

#### [batch.partialResponses?](https://sst.dev/docs/component/aws/queue-lambda-subscriber#batch-partialresponses)

**Type** `Input``<``boolean``>`
**Default** `false`
Whether to return partial successful responses for a batch.
Enables reporting of individual message failures in a batch. When enabled, only failed messages become visible in the queue again, preventing unnecessary reprocessing of successful messages.
The handler function must return a response with failed message IDs.
Ensure your Lambda function is updated to handle `batchItemFailures` responses when enabling this option.
Read more about
Enable partial responses.

```

{


batch: {



partialResponses: true



}


}

```

For a batch of messages (id1, id2, id3, id4, id5), if id2 and id4 fail:

```

{



"batchItemFailures": [



{



"itemIdentifier": "id2"



},


{



"itemIdentifier": "id4"



}


]


}

```

This makes only id2 and id4 visible again in the queue.

#### [batch.size?](https://sst.dev/docs/component/aws/queue-lambda-subscriber#batch-size)

**Type** `Input``<``number``>`
**Default** `10`
The maximum number of events that will be processed together in a single invocation of the consumer function.
Value must be between 1 and 10000.
When `size` is set to a value greater than 10, `window` must be set to at least `1 second`.
Set batch size to 1. This will process events individually.

```

{


batch: {



size: 1



}


}

```

#### [batch.window?](https://sst.dev/docs/component/aws/queue-lambda-subscriber#batch-window)

**Type** `Input``<``“``${number} minute``”`` | ``“``${number} minutes``”`` | ``“``${number} second``”`` | ``“``${number} seconds``”``>`
**Default** `“0 seconds”`
The maximum amount of time to wait for collecting events before sending the batch to the consumer function, even if the batch size hasn’t been reached.
Value must be between 0 seconds and 5 minutes (300 seconds).

```

{


batch: {



window: "20 seconds"



}


}

```

### [filters?](https://sst.dev/docs/component/aws/queue-lambda-subscriber#filters)

**Type** `Input``<``Input``<``Record``<``string`, `any``>``>``[]``>`
Filter the records that’ll be processed by the `subscriber` function.
You can pass in up to 5 different filters.
You can pass in up to 5 different filter policies. These will logically ORed together. Meaning that if any single policy matches, the record will be processed. Learn more about the
For example, if you Queue contains records in this JSON format.

```

{



RecordNumber: 0000,




RequestCode: "AAAA",




TimeStamp: "yyyy-mm-ddThh:mm:ss"



}

```

To process only those records where the `RequestCode` is `BBBB`.

```

{


filters: [


{


body: {



RequestCode: ["BBBB"]



}


}


]


}

```

And to process only those records where `RecordNumber` greater than `9999`.

```

{


filters: [


{


body: {



RecordNumber: [{ numeric: [ ">", 9999 ] }]



}


}


]


}

```

### [queue](https://sst.dev/docs/component/aws/queue-lambda-subscriber#queue)

**Type** `Input``<``Object``>`

* [`arn`](https://sst.dev/docs/component/aws/queue-lambda-subscriber#queue-arn)

The queue to use.

#### [queue.arn](https://sst.dev/docs/component/aws/queue-lambda-subscriber#queue-arn)

**Type** `Input``<``string``>`
The ARN of the queue.

### [subscriber](https://sst.dev/docs/component/aws/queue-lambda-subscriber#subscriber)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`>`
The subscriber function.

### [transform?](https://sst.dev/docs/component/aws/queue-lambda-subscriber#transform)

**Type** `Object`

* [`eventSourceMapping?`](https://sst.dev/docs/component/aws/queue-lambda-subscriber#transform-eventsourcemapping)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.eventSourceMapping?](https://sst.dev/docs/component/aws/queue-lambda-subscriber#transform-eventsourcemapping)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Lambda Event Source Mapping resource.

[Skip to content](https://sst.dev/docs/component/aws/bucket-notification#_top)

# BucketNotification

The `BucketNotification` component is internally used by the `Bucket` component to add bucket notifications to
This component is not intended to be created directly.
You’ll find this component returned by the `notify` method of the `Bucket` component.
* * *

## [Constructor](https://sst.dev/docs/component/aws/bucket-notification#constructor)

```


newBucketNotification(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/bucket-notification#parameters)

* `name` `string`
* `args` [`Args`](https://sst.dev/docs/component/aws/bucket-notification#args)
* `opts?`

## [Properties](https://sst.dev/docs/component/aws/bucket-notification#properties)

### [nodes](https://sst.dev/docs/component/aws/bucket-notification#nodes)

**Type** `Object`

* [`notification`](https://sst.dev/docs/component/aws/bucket-notification#nodes-notification)
* [`functions`](https://sst.dev/docs/component/aws/bucket-notification#nodes-functions)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.notification](https://sst.dev/docs/component/aws/bucket-notification#nodes-notification)

**Type**
The notification resource that’s created.

#### [nodes.functions](https://sst.dev/docs/component/aws/bucket-notification#nodes-functions)

**Type** `Output``<`[`Function`](https://sst.dev/docs/component/aws/function)`[]``>`
The functions that will be notified.

## [Args](https://sst.dev/docs/component/aws/bucket-notification#args)

### [bucket](https://sst.dev/docs/component/aws/bucket-notification#bucket)

**Type** `Input``<``Object``>`

* [`arn`](https://sst.dev/docs/component/aws/bucket-notification#bucket-arn)
* [`name`](https://sst.dev/docs/component/aws/bucket-notification#bucket-name)

The bucket to use.

#### [bucket.arn](https://sst.dev/docs/component/aws/bucket-notification#bucket-arn)

**Type** `Input``<``string``>`
The ARN of the bucket.

#### [bucket.name](https://sst.dev/docs/component/aws/bucket-notification#bucket-name)

**Type** `Input``<``string``>`
The name of the bucket.

### [notifications](https://sst.dev/docs/component/aws/bucket-notification#notifications)

**Type** `Input``<``Input``<``Object``>``[]``>`

* [`events?`](https://sst.dev/docs/component/aws/bucket-notification#notifications-events)
* [`filterPrefix?`](https://sst.dev/docs/component/aws/bucket-notification#notifications-filterprefix)
* [`filterSuffix?`](https://sst.dev/docs/component/aws/bucket-notification#notifications-filtersuffix)
* [`function?`](https://sst.dev/docs/component/aws/bucket-notification#notifications-function)
* [`name`](https://sst.dev/docs/component/aws/bucket-notification#notifications-name)
* [`queue?`](https://sst.dev/docs/component/aws/bucket-notification#notifications-queue)
* [`topic?`](https://sst.dev/docs/component/aws/bucket-notification#notifications-topic)

A list of subscribers that’ll be notified when events happen in the bucket.

#### [notifications[].events?](https://sst.dev/docs/component/aws/bucket-notification#notifications-events)

**Type** `Input``<``Input``<``“``s3:ObjectCreated:*``”`` | ``“``s3:ObjectCreated:Put``”`` | ``“``s3:ObjectCreated:Post``”`` | ``“``s3:ObjectCreated:Copy``”`` | ``“``s3:ObjectCreated:CompleteMultipartUpload``”`` | ``“``s3:ObjectRemoved:*``”`` | ``“``s3:ObjectRemoved:Delete``”`` | ``“``s3:ObjectRemoved:DeleteMarkerCreated``”`` | ``“``s3:ObjectRestore:*``”`` | ``“``s3:ObjectRestore:Post``”`` | ``“``s3:ObjectRestore:Completed``”`` | ``“``s3:ObjectRestore:Delete``”`` | ``“``s3:ReducedRedundancyLostObject``”`` | ``“``s3:Replication:*``”`` | ``“``s3:Replication:OperationFailedReplication``”`` | ``“``s3:Replication:OperationMissedThreshold``”`` | ``“``s3:Replication:OperationReplicatedAfterThreshold``”`` | ``“``s3:Replication:OperationNotTracked``”`` | ``“``s3:LifecycleExpiration:*``”`` | ``“``s3:LifecycleExpiration:Delete``”`` | ``“``s3:LifecycleExpiration:DeleteMarkerCreated``”`` | ``“``s3:LifecycleTransition``”`` | ``“``s3:IntelligentTiering``”`` | ``“``s3:ObjectTagging:*``”`` | ``“``s3:ObjectTagging:Put``”`` | ``“``s3:ObjectTagging:Delete``”`` | ``“``s3:ObjectAcl:Put``”``>``[]``>`
**Default** All S3 events
A list of S3 event types that’ll trigger a notification.

```

{



events: ["s3:ObjectCreated:*", "s3:ObjectRemoved:*"]



}

```

#### [notifications[].filterPrefix?](https://sst.dev/docs/component/aws/bucket-notification#notifications-filterprefix)

**Type** `Input``<``string``>`
An S3 object key prefix that will trigger a notification.
To be notified for all the objects in the `images/` folder.

```

{



filterPrefix: "images/"



}

```

#### [notifications[].filterSuffix?](https://sst.dev/docs/component/aws/bucket-notification#notifications-filtersuffix)

**Type** `Input``<``string``>`
An S3 object key suffix that will trigger the notification.
To be notified for all the objects with the `.jpg` suffix.

```

{



filterSuffix: ".jpg"



}

```

#### [notifications[].function?](https://sst.dev/docs/component/aws/bucket-notification#notifications-function)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
The function that’ll be notified.

```

{



name: "MySubscriber",




function: "src/subscriber.handler"



}

```

Customize the subscriber function. The `link` ensures the subscriber can access the bucket through the [SDK](https://sst.dev/docs/reference/sdk/).

```

{



name: "MySubscriber",




function: {




handler: "src/subscriber.handler",




timeout: "60 seconds",




link: [bucket]



}


}

```

Or pass in the ARN of an existing Lambda function.

```

{



name: "MySubscriber",




function: "arn:aws:lambda:us-east-1:123456789012:function:my-function"



}

```

#### [notifications[].name](https://sst.dev/docs/component/aws/bucket-notification#notifications-name)

**Type** `Input``<``string``>`
The name of the subscriber.

#### [notifications[].queue?](https://sst.dev/docs/component/aws/bucket-notification#notifications-queue)

**Type** `Input``<``string`` |`[`Queue`](https://sst.dev/docs/component/aws/queue)`>`
The Queue that’ll be notified.
For example, let’s say you have a queue.
sst.config.ts

```typescript

const myQueue = newsst.aws.Queue("MyQueue");

```

You can subscribe to this bucket with it.

```

{

name: "MySubscriber",

queue: myQueue

}

```

Or pass in the ARN of an existing SQS queue.

```

{

name: "MySubscriber",

queue: "arn:aws:sqs:us-east-1:123456789012:my-queue"

}

```

#### [notifications[].topic?](https://sst.dev/docs/component/aws/bucket-notification#notifications-topic)

**Type** `Input``<``string`` |`[`SnsTopic`](https://sst.dev/docs/component/aws/sns-topic)`>`
The SNS topic that’ll be notified.
For example, let’s say you have a topic.
sst.config.ts

```typescript


const myTopic = newsst.aws.SnsTopic("MyTopic");


```

You can subscribe to this bucket with it.

```

{



name: "MySubscriber",




topic: myTopic



}

```

Or pass in the ARN of an existing SNS topic.

```

{



name: "MySubscriber",




topic: "arn:aws:sns:us-east-1:123456789012:my-topic"



}

```

### [transform?](https://sst.dev/docs/component/aws/bucket-notification#transform)

**Type** `Object`

* [`notification?`](https://sst.dev/docs/component/aws/bucket-notification#transform-notification)

[Transform](https://sst.dev/docs/components#transform) how this notification creates its underlying resources.

#### [transform.notification?](https://sst.dev/docs/component/aws/bucket-notification#transform-notification)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the S3 Bucket Notification resource.

[Skip to content](https://sst.dev/docs/component/aws/postgres#_top)

# Postgres

The `Postgres` component lets you add a Postgres database to your app using

#### [Create the database](https://sst.dev/docs/component/aws/postgres#create-the-database)

sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc");

const database = newsst.aws.Postgres("MyDatabase", { vpc });

```

#### [Link to a resource](https://sst.dev/docs/component/aws/postgres#link-to-a-resource)

You can link your database to other resources, like a function or your Next.js app.
sst.config.ts

```typescript


new sst.aws.Nextjs("MyWeb", {



link: [database],


vpc


});

```

Once linked, you can connect to it from your function code.
app/page.tsx```

import { Resource } from"sst";

import { Pool } from"pg";

const client = newPool({

Resource.MyDatabase.username,

Resource.MyDatabase.password,

Resource.MyDatabase.database,

Resource.MyDatabase.host,

Resource.MyDatabase.port,

});

await client.connect();

```

#### [Running locally](https://sst.dev/docs/component/aws/postgres#running-locally)
By default, your RDS Postgres database is deployed in `sst dev`. But let’s say you are running Postgres locally.
Terminal window```


dockerrun\




--rm\




-p5432:5432\




-v $(pwd)/.sst/storage/postgres:/var/lib/postgresql/data\




-ePOSTGRES_USER=postgres\




-ePOSTGRES_PASSWORD=password\




-ePOSTGRES_DB=local\



postgres:16.4

```

You can connect to it in `sst dev` by configuring the `dev` prop.
sst.config.ts

```typescript

const postgres = newsst.aws.Postgres("MyPostgres", {

vpc,

"postgres",

"password",

"local",

5432

});

```

This will skip deploying an RDS database and link to the locally running Postgres database instead. [Check out the full example](https://sst.dev/docs/examples/#aws-postgres-local).
* * *

### [Cost](https://sst.dev/docs/component/aws/postgres#cost)

By default this component uses a _Single-AZ Deployment_ , _On-Demand DB Instances_ of a `db.t4g.micro` at $0.016 per hour. And 20GB of _General Purpose gp3 Storage_ at $0.115 per GB per month.
That works out to $0.016 x 24 x 30 + $0.115 x 20 or **$14 per month**. Adjust this for the `instance` type and the `storage` you are using.
The above are rough estimates for _us-east-1_ , check out the

#### [RDS Proxy](https://sst.dev/docs/component/aws/postgres#rds-proxy)

If you enable the `proxy`, it uses _Provisioned instances_ with 2 vCPUs at $0.015 per hour.
That works out to an **additional** $0.015 x 2 x 24 x 30 or **$22 per month**.
This is a rough estimate for _us-east-1_ , check out the
* * *

## [Constructor](https://sst.dev/docs/component/aws/postgres#constructor)

```

newPostgres(name, args, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/postgres#parameters)

* `name` `string`
* `args` [`PostgresArgs`](https://sst.dev/docs/component/aws/postgres#postgresargs)
* `opts?`

## [PostgresArgs](https://sst.dev/docs/component/aws/postgres#postgresargs)

### [database?](https://sst.dev/docs/component/aws/postgres#database)

**Type** `Input``<``string``>`
**Default** Based on the name of the current app
Name of a database that is automatically created.
The name must begin with a letter and contain only lowercase letters, numbers, or underscores. By default, it takes the name of the app, and replaces the hyphens with underscores.

```

{

database: "acme"

}

```

### [dev?](https://sst.dev/docs/component/aws/postgres#dev)

**Type** `Object`

* [`database?`](https://sst.dev/docs/component/aws/postgres#dev-database)
* [`host?`](https://sst.dev/docs/component/aws/postgres#dev-host)
* [`password?`](https://sst.dev/docs/component/aws/postgres#dev-password)
* [`port?`](https://sst.dev/docs/component/aws/postgres#dev-port)
* [`username?`](https://sst.dev/docs/component/aws/postgres#dev-username)

Configure how this component works in `sst dev`.
By default, your Postgres database is deployed in `sst dev`. But if you want to instead connect to a locally running Postgres database, you can configure the `dev` prop.
This will not create an RDS database in `sst dev`.
This will skip deploying an RDS database and link to the locally running Postgres database instead.
Setting the `dev` prop also means that any linked resources will connect to the right database both in `sst dev` and `sst deploy`.

```

{

dev: {

username: "postgres",

password: "password",

database: "postgres",

host: "localhost",

port: 5432

}

}

```

#### [dev.database?](https://sst.dev/docs/component/aws/postgres#dev-database)

**Type** `Input``<``string``>`
**Default** Inherit from the top-level [`database`](https://sst.dev/docs/component/aws/postgres#database).
The database of the local Postgres to connect to when running in dev.

#### [dev.host?](https://sst.dev/docs/component/aws/postgres#dev-host)

**Type** `Input``<``string``>`
**Default** `“localhost”`
The host of the local Postgres to connect to when running in dev.

#### [dev.password?](https://sst.dev/docs/component/aws/postgres#dev-password)

**Type** `Input``<``string``>`
**Default** Inherit from the top-level [`password`](https://sst.dev/docs/component/aws/postgres#password).
The password of the local Postgres to connect to when running in dev.

#### [dev.port?](https://sst.dev/docs/component/aws/postgres#dev-port)

**Type** `Input``<``number``>`
**Default** `5432`
The port of the local Postgres to connect to when running in dev.

#### [dev.username?](https://sst.dev/docs/component/aws/postgres#dev-username)

**Type** `Input``<``string``>`
**Default** Inherit from the top-level [`username`](https://sst.dev/docs/component/aws/postgres#username).
The username of the local Postgres to connect to when running in dev.

### [instance?](https://sst.dev/docs/component/aws/postgres#instance)

**Type** `Input``<``string``>`
**Default** `“t4g.micro”`
The type of instance to use for the database. Check out the

```

{

instance: "m7g.xlarge"

}

```

By default, these changes are not applied immediately by RDS. Instead, they are applied in the next maintenance window. Check out the

### [multiAz?](https://sst.dev/docs/component/aws/postgres#multiaz)

**Type** `Input``<``boolean``>`
**Default** `false`
Enable
This creates a standby replica for the database in another availability zone (AZ). The standby database provides automatic failover in case the primary database fails. However, when the primary database is healthy, the standby database is not used for serving read traffic.
Using Multi-AZ will approximately double the cost of the database since it will be deployed in two AZs.

```

{

multiAz: true

}

```

### [password?](https://sst.dev/docs/component/aws/postgres#password)

**Type** `Input``<``string``>`
**Default** A random password is generated.
The password of the master user.

```

{

password: "Passw0rd!"

}

```

You can use a `Secret` to manage the password.

```

{

password: newsst.Secret("MyDBPassword").value

}

```

### [proxy?](https://sst.dev/docs/component/aws/postgres#proxy)

**Type** `Input``<``boolean`` | ``Object``>`

* [`credentials?`](https://sst.dev/docs/component/aws/postgres#proxy-credentials) `Input``<``Input``<``Object``>``[]``>`
  * [`password`](https://sst.dev/docs/component/aws/postgres#proxy-credentials-password)
  * [`username`](https://sst.dev/docs/component/aws/postgres#proxy-credentials-username)

**Default** `false`
Enable

```

{

proxy: true

}

```

#### [proxy.credentials?](https://sst.dev/docs/component/aws/postgres#proxy-credentials)

**Type** `Input``<``Input``<``Object``>``[]``>`
Additional credentials the proxy can use to connect to the database. You don’t need to specify the master user credentials as they are always added by default.
This component will not create the Postgres users listed here. You need to create them manually in the database.

```

{

credentials: [

{

username: "metabase",

password: "Passw0rd!"

}

]

}

```

You can use a `Secret` to manage the password.

```

{

credentials: [

{

username: "metabase",

password: newsst.Secret("MyDBPassword").value

}

]

}

```

##### [proxy.credentials[].password](https://sst.dev/docs/component/aws/postgres#proxy-credentials-password)

**Type** `Input``<``string``>`
The password of the user.

##### [proxy.credentials[].username](https://sst.dev/docs/component/aws/postgres#proxy-credentials-username)

**Type** `Input``<``string``>`
The username of the user.

### [storage?](https://sst.dev/docs/component/aws/postgres#storage)

**Type** `Input``<``“``${number} GB``”`` | ``“``${number} TB``”``>`
**Default** `“20 GB”`
The maximum storage limit for the database.
RDS will autoscale your storage to match your usage up to the given limit. You are not billed for the maximum storage limit, You are only billed for the storage you use.
You are only billed for the storage you use, not the maximum limit.
By default,
The minimum storage size is 20 GB. And the maximum storage size is 64 TB.

```

{

storage: "100 GB"

}

```

### [transform?](https://sst.dev/docs/component/aws/postgres#transform)

**Type** `Object`

* [`instance?`](https://sst.dev/docs/component/aws/postgres#transform-instance)
* [`parameterGroup?`](https://sst.dev/docs/component/aws/postgres#transform-parametergroup)
* [`proxy?`](https://sst.dev/docs/component/aws/postgres#transform-proxy)
* [`subnetGroup?`](https://sst.dev/docs/component/aws/postgres#transform-subnetgroup)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.instance?](https://sst.dev/docs/component/aws/postgres#transform-instance)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the database instance in the RDS Cluster.

#### [transform.parameterGroup?](https://sst.dev/docs/component/aws/postgres#transform-parametergroup)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the RDS parameter group.

#### [transform.proxy?](https://sst.dev/docs/component/aws/postgres#transform-proxy)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the RDS Proxy.

#### [transform.subnetGroup?](https://sst.dev/docs/component/aws/postgres#transform-subnetgroup)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the RDS subnet group.

### [username?](https://sst.dev/docs/component/aws/postgres#username)

**Type** `Input``<``string``>`
**Default** `“postgres”`
The username of the master user.
Changing the username will cause the database to be destroyed and recreated.

```

{

username: "admin"

}

```

### [version?](https://sst.dev/docs/component/aws/postgres#version)

**Type** `Input``<``string``>`
**Default** `“16.4”`
The Postgres engine version. Check out the

```

{

version: "17.2"

}

```

### [vpc](https://sst.dev/docs/component/aws/postgres#vpc)

**Type** [`Vpc`](https://sst.dev/docs/component/aws/vpc)`| ``Input``<``Object``>`

* [`subnets`](https://sst.dev/docs/component/aws/postgres#vpc-subnets)

The VPC subnets to use for the database.

```

{

vpc: {

subnets: ["subnet-0db7376a7ad4db5fd ", "subnet-06fc7ee8319b2c0ce"]

}

}

```

Or create a `Vpc` component.
sst.config.ts

```typescript


const myVpc = newsst.aws.Vpc("MyVpc");


```

And pass it in. The database will be placed in the private subnets.

```

{



vpc: myVpc



}

```

#### [vpc.subnets](https://sst.dev/docs/component/aws/postgres#vpc-subnets)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of subnet IDs in the VPC.

## [Properties](https://sst.dev/docs/component/aws/postgres#properties)

### [database](https://sst.dev/docs/component/aws/postgres#database-1)

**Type** `Output``<``string``>`
The name of the database.

### [host](https://sst.dev/docs/component/aws/postgres#host)

**Type** `Output``<``string``>`
The host of the database.

### [id](https://sst.dev/docs/component/aws/postgres#id)

**Type** `Output``<``string``>`
The identifier of the Postgres instance.

### [nodes](https://sst.dev/docs/component/aws/postgres#nodes)

**Type** `Object`

* [`instance`](https://sst.dev/docs/component/aws/postgres#nodes-instance)

#### [nodes.instance](https://sst.dev/docs/component/aws/postgres#nodes-instance)

**Type** `undefined`` |`

### [password](https://sst.dev/docs/component/aws/postgres#password-1)

**Type** `Output``<``string``>`
The password of the master user.

### [port](https://sst.dev/docs/component/aws/postgres#port)

**Type** `Output``<``number``>`
The port of the database.

### [proxyId](https://sst.dev/docs/component/aws/postgres#proxyid)

**Type** `Output``<``string``>`
The name of the Postgres proxy.

### [username](https://sst.dev/docs/component/aws/postgres#username-1)

**Type** `Output``<``string``>`
The username of the master user.

## [SDK](https://sst.dev/docs/component/aws/postgres#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/postgres#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `database` `string`
The name of the database.
* `host` `string`
The host of the database.
* `password` `string`
The password of the master user.
* `port` `number`
The port of the database.
* `username` `string`
The username of the master user.

## [Methods](https://sst.dev/docs/component/aws/postgres#methods)

### [static get](https://sst.dev/docs/component/aws/postgres#static-get)

```


Postgres.get(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/postgres#parameters-1)

* `name` `string`
The name of the component.
* `args` [`PostgresGetArgs`](https://sst.dev/docs/component/aws/postgres#postgresgetargs)
The arguments to get the Postgres database.
* `opts?`

**Returns** [`Postgres`](https://sst.dev/docs/component/aws/)
Reference an existing Postgres database with the given name. This is useful when you create a Postgres database in one stage and want to share it in another. It avoids having to create a new Postgres database in the other stage.
You can use the `static get` method to share Postgres databases across stages.
Imagine you create a database in the `dev` stage. And in your personal stage `frank`, instead of creating a new database, you want to share the same database from `dev`.
sst.config.ts

```typescript

const database = $app.stage === "frank"

? sst.aws.Postgres.get("MyDatabase", {

id: "app-dev-mydatabase",

proxyId: "app-dev-mydatabase-proxy"

})

:new sst.aws.Postgres("MyDatabase", {

proxy: true

});

```

Here `app-dev-mydatabase` is the ID of the database, and `app-dev-mydatabase-proxy` is the ID of the proxy created in the `dev` stage. You can find these by outputting the database ID and proxy ID in the `dev` stage.
sst.config.ts

```typescript


return {




id: database.id,




proxyId: database.proxyId



};

```

## [PostgresGetArgs](https://sst.dev/docs/component/aws/postgres#postgresgetargs)

### [id](https://sst.dev/docs/component/aws/postgres#id-1)

**Type** `Input``<``string``>`
The ID of the database.

### [proxyId?](https://sst.dev/docs/component/aws/postgres#proxyid-1)

**Type** `Input``<``string``>`
The ID of the proxy.

[Skip to content](https://sst.dev/docs/component/aws/efs#_top)

# Efs

The `Efs` component lets you add

#### [Create the file system](https://sst.dev/docs/component/aws/efs#create-the-file-system)

sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc");

const efs = newsst.aws.Efs("MyEfs", { vpc });

```

This needs a VPC.

#### [Attach it to a Lambda function](https://sst.dev/docs/component/aws/efs#attach-it-to-a-lambda-function)

sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {



vpc,



handler: "lambda.handler",




volume: { efs, path: "/mnt/efs" }



});

```

This is now mounted at `/mnt/efs` in the Lambda function.

#### [Attach it to a container](https://sst.dev/docs/component/aws/efs#attach-it-to-a-container)

sst.config.ts

```typescript

const cluster = newsst.aws.Cluster("MyCluster", { vpc });

new sst.aws.Service("MyService", {

cluster,

public: {

ports: [{ listen: "80/http" }],

},

volumes: [

{ efs, path: "/mnt/efs" }

]

});

```

Mounted at `/mnt/efs` in the container.
* * *

### [Cost](https://sst.dev/docs/component/aws/efs#cost)

By default this component uses _Regional (Multi-AZ) with Elastic Throughput_. The pricing is pay-per-use.

* For storage: $0.30 per GB per month
* For reads: $0.03 per GB per month
* For writes: $0.06 per GB per month

The above are rough estimates for _us-east-1_ , check out the
* * *

## [Constructor](https://sst.dev/docs/component/aws/efs#constructor)

```

newEfs(name, args, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/efs#parameters)

* `name` `string`
* `args` [`EfsArgs`](https://sst.dev/docs/component/aws/efs#efsargs)
* `opts?`

## [EfsArgs](https://sst.dev/docs/component/aws/efs#efsargs)

### [performance?](https://sst.dev/docs/component/aws/efs#performance)

**Type** `Input``<``“``general-purpose``”`` | ``“``max-io``”``>`
**Default** `“general-purpose”`
The performance mode for the EFS file system.
The `max-io` mode can support higher throughput, but with slightly higher latency. It’s recommended for larger workloads like data analysis or meadia processing.
Both the modes are priced the same, but `general-purpose` is recommended for most use cases.

```

{

performance: "max-io"

}

```

### [throughput?](https://sst.dev/docs/component/aws/efs#throughput)

**Type** `Input``<``“``provisioned``”`` | ``“``bursting``”`` | ``“``elastic``”``>`
**Default** `“elastic”`
The throughput mode for the EFS file system.
The default `elastic` mode scales up or down based on the workload. However, if you know your access patterns, you can use `provisioned` to have a fixed throughput.
Or you can use `bursting` to scale with the amount of storage you’re using. It also supports bursting to higher levels for up to 12 hours per day.

```

{

throughput: "bursting"

}

```

### [transform?](https://sst.dev/docs/component/aws/efs#transform)

**Type** `Object`

* [`accessPoint?`](https://sst.dev/docs/component/aws/efs#transform-accesspoint)
* [`fileSystem?`](https://sst.dev/docs/component/aws/efs#transform-filesystem)
* [`securityGroup?`](https://sst.dev/docs/component/aws/efs#transform-securitygroup)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.accessPoint?](https://sst.dev/docs/component/aws/efs#transform-accesspoint)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EFS access point.

#### [transform.fileSystem?](https://sst.dev/docs/component/aws/efs#transform-filesystem)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EFS file system.

#### [transform.securityGroup?](https://sst.dev/docs/component/aws/efs#transform-securitygroup)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the security group for the EFS mount targets.

### [vpc](https://sst.dev/docs/component/aws/efs#vpc)

**Type** [`Vpc`](https://sst.dev/docs/component/aws/vpc)`| ``Input``<``Object``>`

* [`id`](https://sst.dev/docs/component/aws/efs#vpc-id)
* [`subnets`](https://sst.dev/docs/component/aws/efs#vpc-subnets)

The VPC to use for the EFS file system.
Create a VPC component.

```

const myVpc = newsst.aws.Vpc("MyVpc");

```

And pass it in.

```

{

vpc: myVpc

}

```

Or pass in a custom VPC configuration.

```

{

vpc: {

subnets: ["subnet-0db7376a7ad4db5fd ", "subnet-06fc7ee8319b2c0ce"]

}

}

```

#### [vpc.id](https://sst.dev/docs/component/aws/efs#vpc-id)

**Type** `Input``<``string``>`
The ID of the VPC.

#### [vpc.subnets](https://sst.dev/docs/component/aws/efs#vpc-subnets)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of subnet IDs in the VPC to create the EFS mount targets in.

## [Properties](https://sst.dev/docs/component/aws/efs#properties)

### [accessPoint](https://sst.dev/docs/component/aws/efs#accesspoint)

**Type** `Output``<``string``>`
The ID of the EFS access point.

### [id](https://sst.dev/docs/component/aws/efs#id)

**Type** `Output``<``string``>`
The ID of the EFS file system.

### [nodes](https://sst.dev/docs/component/aws/efs#nodes)

**Type** `Object`

* [`accessPoint`](https://sst.dev/docs/component/aws/efs#nodes-accesspoint)
* [`fileSystem`](https://sst.dev/docs/component/aws/efs#nodes-filesystem)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.accessPoint](https://sst.dev/docs/component/aws/efs#nodes-accesspoint)

**Type** `Output``<``>`
The Amazon EFS access point.

#### [nodes.fileSystem](https://sst.dev/docs/component/aws/efs#nodes-filesystem)

**Type** `Output``<``>`
The Amazon EFS file system.

## [Methods](https://sst.dev/docs/component/aws/efs#methods)

### [static get](https://sst.dev/docs/component/aws/efs#static-get)

```

Efs.get(name, fileSystemID, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/efs#parameters-1)

* `name` `string`
The name of the component.
* `fileSystemID` `Input``<``string``>`
The ID of the existing EFS file system.
* `opts?`

**Returns** [`Efs`](https://sst.dev/docs/component/aws/)
Reference an existing EFS file system with the given file system ID. This is useful when you create a EFS file system in one stage and want to share it in another. It avoids having to create a new EFS file system in the other stage.
You can use the `static get` method to share EFS file systems across stages.
Imagine you create a EFS file system in the `dev` stage. And in your personal stage `frank`, instead of creating a new file system, you want to share the same file system from `dev`.
sst.config.ts

```typescript


const efs = $app.stage === "frank"




? sst.aws.Efs.get("MyEfs", "app-dev-myefs")




:new sst.aws.Efs("MyEfs", { vpc });


```

Here `app-dev-myefs` is the ID of the file system created in the `dev` stage. You can find this by outputting the file system ID in the `dev` stage.
sst.config.ts

```typescript

return {

id: efs.id

};

```

[Skip to content](https://sst.dev/docs/component/aws/task#_top)

# Task

The `Task` component lets you create containers that are used for long running asynchronous work, like data processing. It uses

#### [Create a Task](https://sst.dev/docs/component/aws/task#create-a-task)

Tasks are run inside an ECS Cluster. If you haven’t already, create one.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc");




const cluster = newsst.aws.Cluster("MyCluster", { vpc });


```

Add the task to it.
sst.config.ts

```typescript

const task = newsst.aws.Task("MyTask", { cluster });

```

#### [Configure the container image](https://sst.dev/docs/component/aws/task#configure-the-container-image)

By default, the task will look for a Dockerfile in the root directory. Optionally, configure the image context and dockerfile.
sst.config.ts

```typescript


new sst.aws.Task("MyTask", {



cluster,


image: {



context: "./app",




dockerfile: "Dockerfile"



}


});

```

To add multiple containers in the task, pass in an array of containers args.
sst.config.ts

```typescript

new sst.aws.Task("MyTask", {

cluster,

containers: [

{

name: "app",

image: "nginxdemos/hello:plain-text"

},

{

name: "admin",

image: {

context: "./admin",

dockerfile: "Dockerfile"

}

}

]

});

```

This is useful for running sidecar containers.

#### [Link resources](https://sst.dev/docs/component/aws/task#link-resources)

[Link resources](https://sst.dev/docs/linking/) to your task. This will grant permissions to the resources and allow you to access it in your app.
sst.config.ts

```typescript


const bucket = newsst.aws.Bucket("MyBucket");




new sst.aws.Task("MyTask", {



cluster,


link: [bucket]


});

```

You can use the [SDK](https://sst.dev/docs/reference/sdk/) to access the linked resources in your task.
app.ts

```typescript

import { Resource } from"sst";

console.log(Resource.MyBucket.name);

```

#### [Task SDK](https://sst.dev/docs/component/aws/task#task-sdk)

With the [Task JS SDK](https://sst.dev/docs/component/aws/task#sdk), you can run your tasks, stop your tasks, and get the status of your tasks.
For example, you can link the task to a function in your app.
sst.config.ts

```typescript


new sst.aws.Function("MyFunction", {




handler: "src/lambda.handler",



link: [task]


});

```

Then from your function run the task.
src/lambda.ts

```typescript

import { Resource } from"sst";

import { task } from"sst/aws/task";

const runRet = await task.run(Resource.MyTask);

const taskArn = runRet.arn;

```

If you are not using Node.js, you can use the AWS SDK instead. Here’s
* * *

### [Cost](https://sst.dev/docs/component/aws/task#cost)

By default, this uses a _Linux/X86_ _Fargate_ container with 0.25 vCPUs at $0.04048 per vCPU per hour and 0.5 GB of memory at $0.004445 per GB per hour. It includes 20GB of _Ephemeral Storage_ for free with additional storage at $0.000111 per GB per hour. Each container also gets a public IPv4 address at $0.005 per hour.
It works out to $0.04048 x 0.25 + $0.004445 x 0.5 + $0.005. Or **$0.02 per hour** your task runs for.
Adjust this for the `cpu`, `memory` and `storage` you are using. And check the prices for _Linux/ARM_ if you are using `arm64` as your `architecture`.
The above are rough estimates for _us-east-1_ , check out the
* * *

## [Constructor](https://sst.dev/docs/component/aws/task#constructor)

```

newTask(name, args, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/task#parameters)

* `name` `string`
* `args` [`TaskArgs`](https://sst.dev/docs/component/aws/task#taskargs)
* `opts?`

## [TaskArgs](https://sst.dev/docs/component/aws/task#taskargs)

### [architecture?](https://sst.dev/docs/component/aws/task#architecture)

**Type** `Input``<``“``x86_64``”`` | ``“``arm64``”``>`
**Default** `“x86_64”`
The CPU architecture of the container.

```

{

architecture: "arm64"

}

```

### [cluster](https://sst.dev/docs/component/aws/task#cluster)

**Type** [`Cluster`](https://sst.dev/docs/component/aws/cluster)
The ECS Cluster to use. Create a new `Cluster` in your app, if you haven’t already.
sst.config.ts

```typescript


const vpc = newsst.aws.Vpc("MyVpc");




const myCluster = newsst.aws.Cluster("MyCluster", { vpc });


```

And pass it in.

```

{



cluster: myCluster



}

```

### [command?](https://sst.dev/docs/component/aws/task#command)

**Type** `Input``<``Input``<``string``>``[]``>`
The command to override the default command in the container.

```

{



command: ["npm", "run", "start"]



}

```

### [containers?](https://sst.dev/docs/component/aws/task#containers)

**Type** `Input``<``Object``>``[]`

* [`command?`](https://sst.dev/docs/component/aws/task#containers-command)
* [`cpu?`](https://sst.dev/docs/component/aws/task#containers-cpu)
* [`entrypoint?`](https://sst.dev/docs/component/aws/task#containers-entrypoint)
* [`environment?`](https://sst.dev/docs/component/aws/task#containers-environment)
* [`environmentFiles?`](https://sst.dev/docs/component/aws/task#containers-environmentfiles)
* [`image?`](https://sst.dev/docs/component/aws/task#containers-image) `Input``<``string`` | ``Object``>`
  * [`args?`](https://sst.dev/docs/component/aws/task#containers-image-args)
  * [`context?`](https://sst.dev/docs/component/aws/task#containers-image-context)
  * [`dockerfile?`](https://sst.dev/docs/component/aws/task#containers-image-dockerfile)
  * [`target?`](https://sst.dev/docs/component/aws/task#containers-image-target)
* [`logging?`](https://sst.dev/docs/component/aws/task#containers-logging) `Input``<``Object``>`
  * [`name?`](https://sst.dev/docs/component/aws/task#containers-logging-name)
  * [`retention?`](https://sst.dev/docs/component/aws/task#containers-logging-retention)
* [`memory?`](https://sst.dev/docs/component/aws/task#containers-memory)
* [`name`](https://sst.dev/docs/component/aws/task#containers-name)
* [`ssm?`](https://sst.dev/docs/component/aws/task#containers-ssm)
* [`volumes?`](https://sst.dev/docs/component/aws/task#containers-volumes) `Input``<``Object``>``[]`
  * [`efs`](https://sst.dev/docs/component/aws/task#containers-volumes-efs) `Input``<`[`Efs`](https://sst.dev/docs/component/aws/efs)`| ``Object``>`
    * [`accessPoint`](https://sst.dev/docs/component/aws/task#containers-volumes-efs-accesspoint)
    * [`fileSystem`](https://sst.dev/docs/component/aws/task#containers-volumes-efs-filesystem)
  * [`path`](https://sst.dev/docs/component/aws/task#containers-volumes-path)

The containers to run in the task.
You can optionally run multiple containers in a task.
By default this starts a single container. To add multiple containers in the task, pass in an array of containers args.

```

{


containers: [


{



name: "app",




image: "nginxdemos/hello:plain-text"



},


{



name: "admin",



image: {



context: "./admin",




dockerfile: "Dockerfile"



}


}


]


}

```

If you specify `containers`, you cannot list the above args at the top-level. For example, you **cannot** pass in `image` at the top level.

```

{



image: "nginxdemos/hello:plain-text",



containers: [


{



name: "app",




image: "nginxdemos/hello:plain-text"



},


{



name: "admin",




image: "nginxdemos/hello:plain-text"



}


]


}

```

You will need to pass in `image` as a part of the `containers`.

#### [containers[].command?](https://sst.dev/docs/component/aws/task#containers-command)

**Type** `Input``<``string``[]``>`
The command to override the default command in the container. Same as the top-level [`command`](https://sst.dev/docs/component/aws/task#command).

#### [containers[].cpu?](https://sst.dev/docs/component/aws/task#containers-cpu)

**Type** `“``${number} vCPU``”`
The amount of CPU allocated to the container.
By default, a container can use up to all the CPU allocated to all the containers. If set, this container is capped at this allocation even if more idle CPU is available.
The sum of all the containers’ CPU must be less than or equal to the total available CPU.

```

{



cpu: "0.25 vCPU"



}

```

#### [containers[].entrypoint?](https://sst.dev/docs/component/aws/task#containers-entrypoint)

**Type** `Input``<``string``[]``>`
The entrypoint to override the default entrypoint in the container. Same as the top-level [`entrypoint`](https://sst.dev/docs/component/aws/task#entrypoint).

#### [containers[].environment?](https://sst.dev/docs/component/aws/task#containers-environment)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Key-value pairs of values that are set as container environment variables. Same as the top-level [`environment`](https://sst.dev/docs/component/aws/task#environment).

#### [containers[].environmentFiles?](https://sst.dev/docs/component/aws/task#containers-environmentfiles)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of Amazon S3 file paths of environment files to load environment variables from. Same as the top-level [`environmentFiles`](https://sst.dev/docs/component/aws/task#environmentFiles).

#### [containers[].image?](https://sst.dev/docs/component/aws/task#containers-image)

**Type** `Input``<``string`` | ``Object``>`
Configure the Docker image for the container. Same as the top-level [`image`](https://sst.dev/docs/component/aws/task#image).

##### [containers[].image.args?](https://sst.dev/docs/component/aws/task#containers-image-args)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Key-value pairs of build args. Same as the top-level [`image.args`](https://sst.dev/docs/component/aws/task#image-args).

##### [containers[].image.context?](https://sst.dev/docs/component/aws/task#containers-image-context)

**Type** `Input``<``string``>`
The path to the Docker build context. Same as the top-level [`image.context`](https://sst.dev/docs/component/aws/task#image-context).

##### [containers[].image.dockerfile?](https://sst.dev/docs/component/aws/task#containers-image-dockerfile)

**Type** `Input``<``string``>`
The path to the Dockerfile. Same as the top-level [`image.dockerfile`](https://sst.dev/docs/component/aws/task#image-dockerfile).

##### [containers[].image.target?](https://sst.dev/docs/component/aws/task#containers-image-target)

**Type** `Input``<``string``>`
The stage to build up to. Same as the top-level [`image.target`](https://sst.dev/docs/component/aws/task#image-target).

#### [containers[].logging?](https://sst.dev/docs/component/aws/task#containers-logging)

**Type** `Input``<``Object``>`
Configure the logs in CloudWatch. Same as the top-level [`logging`](https://sst.dev/docs/component/aws/task#logging).

##### [containers[].logging.name?](https://sst.dev/docs/component/aws/task#containers-logging-name)

**Type** `Input``<``string``>`
The name of the CloudWatch log group. Same as the top-level [`logging.name`](https://sst.dev/docs/component/aws/task#logging-name).

##### [containers[].logging.retention?](https://sst.dev/docs/component/aws/task#containers-logging-retention)

**Type** `Input``<``“``1 day``”`` | ``“``3 days``”`` | ``“``5 days``”`` | ``“``1 week``”`` | ``“``2 weeks``”`` | ``“``1 month``”`` | ``“``2 months``”`` | ``“``3 months``”`` | ``“``4 months``”`` | ``“``5 months``”`` | ``“``6 months``”`` | ``“``1 year``”`` | ``“``13 months``”`` | ``“``18 months``”`` | ``“``2 years``”`` | ``“``3 years``”`` | ``“``5 years``”`` | ``“``6 years``”`` | ``“``7 years``”`` | ``“``8 years``”`` | ``“``9 years``”`` | ``“``10 years``”`` | ``“``forever``”``>`
The duration the logs are kept in CloudWatch. Same as the top-level [`logging.retention`](https://sst.dev/docs/component/aws/task#logging-retention).

#### [containers[].memory?](https://sst.dev/docs/component/aws/task#containers-memory)

**Type** `“``${number} GB``”`
The amount of memory allocated to the container.
By default, a container can use up to all the memory allocated to all the containers. If set, the container is capped at this allocation. If exceeded, the container will be killed even if there is idle memory available.
The sum of all the containers’ memory must be less than or equal to the total available memory.

```

{



memory: "0.5 GB"



}

```

#### [containers[].name](https://sst.dev/docs/component/aws/task#containers-name)

**Type** `Input``<``string``>`
The name of the container.
This is used as the `--name` option in the Docker run command.

#### [containers[].ssm?](https://sst.dev/docs/component/aws/task#containers-ssm)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Key-value pairs of AWS Systems Manager Parameter Store parameter ARNs or AWS Secrets Manager secret ARNs. The values will be loaded into the container as environment variables. Same as the top-level [`ssm`](https://sst.dev/docs/component/aws/task#ssm).

#### [containers[].volumes?](https://sst.dev/docs/component/aws/task#containers-volumes)

**Type** `Input``<``Object``>``[]`
Mount Amazon EFS file systems into the container. Same as the top-level [`efs`](https://sst.dev/docs/component/aws/task#efs).

##### [containers[].volumes[].efs](https://sst.dev/docs/component/aws/task#containers-volumes-efs)

**Type** `Input``<`[`Efs`](https://sst.dev/docs/component/aws/efs)`| ``Object``>`
The Amazon EFS file system to mount.

##### [containers[].volumes[].efs.accessPoint](https://sst.dev/docs/component/aws/task#containers-volumes-efs-accesspoint)

**Type** `Input``<``string``>`
The ID of the EFS access point.

##### [containers[].volumes[].efs.fileSystem](https://sst.dev/docs/component/aws/task#containers-volumes-efs-filesystem)

**Type** `Input``<``string``>`
The ID of the EFS file system.

##### [containers[].volumes[].path](https://sst.dev/docs/component/aws/task#containers-volumes-path)

**Type** `Input``<``string``>`
The path to mount the volume.

### [cpu?](https://sst.dev/docs/component/aws/task#cpu)

**Type** `“``0.25 vCPU``”`` | ``“``0.5 vCPU``”`` | ``“``1 vCPU``”`` | ``“``2 vCPU``”`` | ``“``4 vCPU``”`` | ``“``8 vCPU``”`` | ``“``16 vCPU``”`
**Default** `“0.25 vCPU”`
The amount of CPU allocated to the container. If there are multiple containers, this is the total amount of CPU shared across all the containers.

```

{



cpu: "1 vCPU"



}

```

### [dev?](https://sst.dev/docs/component/aws/task#dev)

**Type** `false`` | ``Object`

* [`command?`](https://sst.dev/docs/component/aws/task#dev-command)
* [`directory?`](https://sst.dev/docs/component/aws/task#dev-directory)

Configure how this component works in `sst dev`.
In `sst dev` a _stub_ version of your task is deployed.
By default, your task in not deployed in `sst dev`. Instead, you can set the `dev.command` and it’ll run locally in a **Tasks** tab in the `sst dev` multiplexer.
Here’s what happens when you run `sst dev`:

  1. A _stub_ version of your task is deployed. This is a minimal image that starts up faster.
  2. When your task is started through the SDK, the stub version is provisioned. This can take roughly **10 - 20 seconds**.
  3. The stub version proxies the payload to your local machine using the same events system used by [Live](https://sst.dev/docs/live/).
  4. The `dev.command` is called to run your task locally. Once complete, the stub version of your task is stopped as well.

The advantage with this approach is that you can test your task locally even it’s invoked remotely, or through a cron job.
You are charged for the time it takes to run the stub version of your task.
Since the stub version runs while your task is running, you are charged for the time it takes to run. This is roughly **$0.02 per hour**.
To disable this and deploy your task in `sst dev`, pass in `false`. Read more about [Live](https://sst.dev/docs/live/) and [`sst dev`](https://sst.dev/docs/reference/cli/#dev).

#### [dev.command?](https://sst.dev/docs/component/aws/task#dev-command)

**Type** `Input``<``string``>`
The command that `sst dev` runs in dev mode.

#### [dev.directory?](https://sst.dev/docs/component/aws/task#dev-directory)

**Type** `Input``<``string``>`
**Default** Uses the `image.dockerfile` path
Change the directory from where the `command` is run.

### [entrypoint?](https://sst.dev/docs/component/aws/task#entrypoint)

**Type** `Input``<``string``[]``>`
The entrypoint that overrides the default entrypoint in the container.

```

{



entrypoint: ["/usr/bin/my-entrypoint"]



}

```

### [environment?](https://sst.dev/docs/component/aws/task#environment)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Key-value pairs of values that are set as

  1. Start with a letter.
  2. Be at least 2 characters long.
  3. Contain only letters, numbers, or underscores.

```

{


environment: {



DEBUG: "true"



}


}

```

### [environmentFiles?](https://sst.dev/docs/component/aws/task#environmentfiles)

**Type** `Input``<``Input``<``string``>``[]``>`
A list of Amazon S3 object ARNs pointing to
Each file must be a plain text file in `.env` format.
Create an S3 bucket and upload an environment file.
sst.config.ts

```typescript

const bucket = newsst.aws.Bucket("EnvBucket");

const file = newaws.s3.BucketObjectv2("EnvFile", {

bucket: bucket.name,

key: "test.env",

content: ["FOO=hello", "BAR=world"].join("\n"),

});

```

And pass in the ARN of the environment file.
sst.config.ts

```typescript

{



environmentFiles: [file.arn]



}

```

### [executionRole?](https://sst.dev/docs/component/aws/task#executionrole)

**Type** `Input``<``string``>`
**Default** Creates a new role
Assigns the given IAM role name to AWS ECS to launch and manage the containers. This allows you to pass in a previously created role.
By default, a new IAM role is created.

```

{



executionRole: "my-execution-role"



}

```

### [image?](https://sst.dev/docs/component/aws/task#image)

**Type** `Input``<``string`` | ``Object``>`

* [`args?`](https://sst.dev/docs/component/aws/task#image-args)
* [`context?`](https://sst.dev/docs/component/aws/task#image-context)
* [`dockerfile?`](https://sst.dev/docs/component/aws/task#image-dockerfile)
* [`tags?`](https://sst.dev/docs/component/aws/task#image-tags)
* [`target?`](https://sst.dev/docs/component/aws/task#image-target)

**Default** Build a Docker image from the Dockerfile in the root directory.
Configure the Docker build command for building the image or specify a pre-built image.
Building a Docker image.
Prior to building the image, SST will automatically add the `.sst` directory to the `.dockerignore` if not already present.

```

{


image: {



context: "./app",




dockerfile: "Dockerfile",



args: {



MY_VAR: "value"



}


}


}

```

Alternatively, you can pass in a pre-built image.

```

{



image: "nginxdemos/hello:plain-text"



}

```

#### [image.args?](https://sst.dev/docs/component/aws/task#image-args)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Key-value pairs of

```

{


args: {



MY_VAR: "value"



}


}

```

#### [image.context?](https://sst.dev/docs/component/aws/task#image-context)

**Type** `Input``<``string``>`
**Default** `”.”`
The path to the `sst.config.ts`.
To change where the Docker build context is located.

```

{



context: "./app"



}

```

#### [image.dockerfile?](https://sst.dev/docs/component/aws/task#image-dockerfile)

**Type** `Input``<``string``>`
**Default** `“Dockerfile”`
The path to the `context`.
To use a different Dockerfile.

```

{



dockerfile: "Dockerfile.prod"



}

```

#### [image.tags?](https://sst.dev/docs/component/aws/task#image-tags)

**Type** `Input``<``Input``<``string``>``[]``>`
Tags to apply to the Docker image.

```

{



tags: ["v1.0.0", "commit-613c1b2"]



}

```

#### [image.target?](https://sst.dev/docs/component/aws/task#image-target)

**Type** `Input``<``string``>`
The stage to build up to in a

```

{



target: "stage1"



}

```

### [link?](https://sst.dev/docs/component/aws/task#link)

**Type** `Input``<``any``[]``>`
[Link resources](https://sst.dev/docs/linking/) to your containers. This will:

  1. Grant the permissions needed to access the resources.
  2. Allow you to access it in your app using the [SDK](https://sst.dev/docs/reference/sdk/).

Takes a list of components to link to the containers.

```

{



link: [bucket, stripeKey]



}

```

### [logging?](https://sst.dev/docs/component/aws/task#logging)

**Type** `Input``<``Object``>`

* [`name?`](https://sst.dev/docs/component/aws/task#logging-name)
* [`retention?`](https://sst.dev/docs/component/aws/task#logging-retention)

**Default** `{ retention: “1 month” }`
Configure the logs in CloudWatch.

```

{


logging: {



retention: "forever"



}


}

```

#### [logging.name?](https://sst.dev/docs/component/aws/task#logging-name)

**Type** `Input``<``string``>`
**Default** `“/sst/cluster/${CLUSTER_NAME}/${SERVICE_NAME}/${CONTAINER_NAME}”`
The name of the CloudWatch log group. If omitted, the log group name is generated based on the cluster name, service name, and container name.

#### [logging.retention?](https://sst.dev/docs/component/aws/task#logging-retention)

**Type** `Input``<``“``1 day``”`` | ``“``3 days``”`` | ``“``5 days``”`` | ``“``1 week``”`` | ``“``2 weeks``”`` | ``“``1 month``”`` | ``“``2 months``”`` | ``“``3 months``”`` | ``“``4 months``”`` | ``“``5 months``”`` | ``“``6 months``”`` | ``“``1 year``”`` | ``“``13 months``”`` | ``“``18 months``”`` | ``“``2 years``”`` | ``“``3 years``”`` | ``“``5 years``”`` | ``“``6 years``”`` | ``“``7 years``”`` | ``“``8 years``”`` | ``“``9 years``”`` | ``“``10 years``”`` | ``“``forever``”``>`
**Default** `“1 month”`
The duration the logs are kept in CloudWatch.

### [memory?](https://sst.dev/docs/component/aws/task#memory)

**Type** `“``${number} GB``”`
**Default** `“0.5 GB”`
The amount of memory allocated to the container. If there are multiple containers, this is the total amount of memory shared across all the containers.

```

{



memory: "2 GB"



}

```

### [permissions?](https://sst.dev/docs/component/aws/task#permissions)

**Type** `Input``<``Object``[]``>`

* [`actions`](https://sst.dev/docs/component/aws/task#permissions-actions)
* [`effect?`](https://sst.dev/docs/component/aws/task#permissions-effect)
* [`resources`](https://sst.dev/docs/component/aws/task#permissions-resources)

Permissions and the resources that you need to access. These permissions are used to create the
If you `link` the service to a resource, the permissions to access it are automatically added.
Allow the container to read and write to an S3 bucket called `my-bucket`.

```

{


permissions: [


{



actions: ["s3:GetObject", "s3:PutObject"],




resources: ["arn:aws:s3:::my-bucket/*"]



},


]


}

```

Allow the container to perform all actions on an S3 bucket called `my-bucket`.

```

{


permissions: [


{



actions: ["s3:*"],




resources: ["arn:aws:s3:::my-bucket/*"]



},


]


}

```

Granting the container permissions to access all resources.

```

{


permissions: [


{



actions: ["*"],




resources: ["*"]



},


]


}

```

#### [permissions[].actions](https://sst.dev/docs/component/aws/task#permissions-actions)

**Type** `string``[]`
The

```

{



actions: ["s3:*"]



}

```

#### [permissions[].effect?](https://sst.dev/docs/component/aws/task#permissions-effect)

**Type** `“``allow``”`` | ``“``deny``”`
**Default** `“allow”`
Configures whether the permission is allowed or denied.

```

{



effect: "deny"



}

```

#### [permissions[].resources](https://sst.dev/docs/component/aws/task#permissions-resources)

**Type** `Input``<``Input``<``string``>``[]``>`
The resourcess specified using the

```

{



resources: ["arn:aws:s3:::my-bucket/*"]



}

```

### [publicIp?](https://sst.dev/docs/component/aws/task#publicip)

**Type** `Input``<``boolean``>`
Assign a public IP address to the task.
Defaults:

* If an SST VPC component is passed to the `vpc` property, tasks run in public subnets by default and `publicIp` defaults to `true`.
* If a non-SST VPC is used, tasks run in the specified subnets and `publicIp` defaults to `false`.

```

{



publicIp: true



}

```

### [ssm?](https://sst.dev/docs/component/aws/task#ssm)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Key-value pairs of AWS Systems Manager Parameter Store parameter ARNs or AWS Secrets Manager secret ARNs. The values will be loaded into the container as environment variables.

```

{


ssm: {



DATABASE_PASSWORD: "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret-123abc"



}


}

```

### [storage?](https://sst.dev/docs/component/aws/task#storage)

**Type** `“``${number} GB``”`
**Default** `“20 GB”`
The amount of ephemeral storage (in GB) allocated to the container.

```

{



storage: "100 GB"



}

```

### [taskRole?](https://sst.dev/docs/component/aws/task#taskrole)

**Type** `Input``<``string``>`
**Default** Creates a new role
Assigns the given IAM role name to the containers. This allows you to pass in a previously created role.
When you pass in a role, it will not update it if you add `permissions` or `link` resources.
By default, a new IAM role is created. It’ll update this role if you add `permissions` or `link` resources.
However, if you pass in a role, you’ll need to update it manually if you add `permissions` or `link` resources.

```

{



taskRole: "my-task-role"



}

```

### [transform?](https://sst.dev/docs/component/aws/task#transform)

**Type** `Object`

* [`executionRole?`](https://sst.dev/docs/component/aws/task#transform-executionrole)
* [`image?`](https://sst.dev/docs/component/aws/task#transform-image)
* [`logGroup?`](https://sst.dev/docs/component/aws/task#transform-loggroup)
* [`taskDefinition?`](https://sst.dev/docs/component/aws/task#transform-taskdefinition)
* [`taskRole?`](https://sst.dev/docs/component/aws/task#transform-taskrole)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.executionRole?](https://sst.dev/docs/component/aws/task#transform-executionrole)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the ECS Execution IAM Role resource.

#### [transform.image?](https://sst.dev/docs/component/aws/task#transform-image)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Docker Image resource.

#### [transform.logGroup?](https://sst.dev/docs/component/aws/task#transform-loggroup)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the CloudWatch log group resource.

#### [transform.taskDefinition?](https://sst.dev/docs/component/aws/task#transform-taskdefinition)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the ECS Task Definition resource.

#### [transform.taskRole?](https://sst.dev/docs/component/aws/task#transform-taskrole)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the ECS Task IAM Role resource.

### [volumes?](https://sst.dev/docs/component/aws/task#volumes)

**Type** `Input``<``Object``>``[]`

* [`efs`](https://sst.dev/docs/component/aws/task#volumes-efs) `Input``<`[`Efs`](https://sst.dev/docs/component/aws/efs)`| ``Object``>`
  * [`accessPoint`](https://sst.dev/docs/component/aws/task#volumes-efs-accesspoint)
  * [`fileSystem`](https://sst.dev/docs/component/aws/task#volumes-efs-filesystem)
* [`path`](https://sst.dev/docs/component/aws/task#volumes-path)

Mount Amazon EFS file systems into the container.
Create an EFS file system.
sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc");

const fileSystem = newsst.aws.Efs("MyFileSystem", { vpc });

```

And pass it in.

```

{

volumes: [

{

efs: fileSystem,

path: "/mnt/efs"

}

]

}

```

Or pass in a the EFS file system ID.

```

{

volumes: [

{

efs: {

fileSystem: "fs-12345678",

accessPoint: "fsap-12345678"

},

path: "/mnt/efs"

}

]

}

```

#### [volumes[].efs](https://sst.dev/docs/component/aws/task#volumes-efs)

**Type** `Input``<`[`Efs`](https://sst.dev/docs/component/aws/efs)`| ``Object``>`
The Amazon EFS file system to mount.

##### [volumes[].efs.accessPoint](https://sst.dev/docs/component/aws/task#volumes-efs-accesspoint)

**Type** `Input``<``string``>`
The ID of the EFS access point.

##### [volumes[].efs.fileSystem](https://sst.dev/docs/component/aws/task#volumes-efs-filesystem)

**Type** `Input``<``string``>`
The ID of the EFS file system.

#### [volumes[].path](https://sst.dev/docs/component/aws/task#volumes-path)

**Type** `Input``<``string``>`
The path to mount the volume.

## [Properties](https://sst.dev/docs/component/aws/task#properties)

### [nodes](https://sst.dev/docs/component/aws/task#nodes)

**Type** `Object`

* [`executionRole`](https://sst.dev/docs/component/aws/task#nodes-executionrole)
* [`taskDefinition`](https://sst.dev/docs/component/aws/task#nodes-taskdefinition)
* [`taskRole`](https://sst.dev/docs/component/aws/task#nodes-taskrole)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.executionRole](https://sst.dev/docs/component/aws/task#nodes-executionrole)

**Type**
The Amazon ECS Execution Role.

#### [nodes.taskDefinition](https://sst.dev/docs/component/aws/task#nodes-taskdefinition)

**Type** `Output``<``>`
The Amazon ECS Task Definition.

#### [nodes.taskRole](https://sst.dev/docs/component/aws/task#nodes-taskrole)

**Type**
The Amazon ECS Task Role.

### [taskDefinition](https://sst.dev/docs/component/aws/task#taskdefinition)

**Type** `Output``<``string``>`
The ARN of the ECS Task Definition.

## [SDK](https://sst.dev/docs/component/aws/task#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/task#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `assignPublicIp` `boolean`
Whether to assign a public IP address to the task.
* `cluster` `string`
The ARN of the cluster this task is deployed to.
* `containers` `string``[]`
The names of the containers in the task.
* `securityGroups` `string``[]`
The security groups for the task.
* `subnets` `string``[]`
The subnets for the task.
* `taskDefinition` `string`
The ARN of the ECS Task Definition.

The `task` client SDK is available through the following.
src/app.ts

```typescript


import { task } from"sst/aws/task";


```

If you are not using Node.js, you can use the AWS SDK instead. For example, you can call
* * *

### [describe](https://sst.dev/docs/component/aws/task#describe)

```


task.describe(resource, task, options?)


```

#### [Parameters](https://sst.dev/docs/component/aws/task#parameters-1)

* `resource` [`Resource`](https://sst.dev/docs/component/aws/task#resource)
* `task` `string`
* `options?` [`Options`](https://sst.dev/docs/component/aws/task#options)

**Returns** `Promise``<`[`DescribeResponse`](https://sst.dev/docs/component/aws/task#describeresponse)`>`
Get the details of a given task.
If a task had been stopped over an hour ago, it’s not returned.
For example, let’s say you had previously started a task.
src/app.ts

```typescript

const runRet = await task.run(Resource.MyTask);

const taskArn = runRet.tasks[0].taskArn;

```

You can use that to get the details of the task.
src/app.ts

```typescript


const describeRet = await task.describe(Resource.MyTask, taskArn);




console.log(describeRet.status);


```

If you are not using Node.js, you can use the AWS SDK and call

### [run](https://sst.dev/docs/component/aws/task#run)

```


task.run(resource, environment?, options?)


```

#### [Parameters](https://sst.dev/docs/component/aws/task#parameters-2)

* `resource` [`Resource`](https://sst.dev/docs/component/aws/task#resource)
* `environment?` `Record``<``string`, `string``>`
* `options?` [`RunOptions`](https://sst.dev/docs/component/aws/task#runoptions)

**Returns** `Promise``<`[`RunResponse`](https://sst.dev/docs/component/aws/task#runresponse)`>`
Runs a task.
For example, let’s say you have defined a task.
sst.config.ts

```typescript

newsst.aws.Task("MyTask", { cluster });

```

You can then run the task in your application with the SDK.
src/app.ts

```typescript


import { Resource } from"sst";




import { task } from"sst/aws/task";




const runRet = await task.run(Resource.MyTask);




const taskArn = runRet.tasks[0].taskArn;


```

This internally calls an AWS SDK API that returns an array of tasks. But in our case, there’s only one task.
The `taskArn` is the ARN of the task. You can use it to call the `describe` or `stop` functions.
You can also pass in any environment variables to the task.
src/app.ts

```typescript

awaittask.run(Resource.MyTask, {

MY_ENV_VAR: "my-value"

});

```

If you are not using Node.js, you can use the AWS SDK and call

### [stop](https://sst.dev/docs/component/aws/task#stop)

```

task.stop(resource, task, options?)

```

#### [Parameters](https://sst.dev/docs/component/aws/task#parameters-3)

* `resource` [`Resource`](https://sst.dev/docs/component/aws/task#resource)
* `task` `string`
* `options?` [`Options`](https://sst.dev/docs/component/aws/task#options)

**Returns** `Promise``<`[`StopResponse`](https://sst.dev/docs/component/aws/task#stopresponse)`>`
Stops a task.
For example, let’s say you had previously started a task.
src/app.ts

```typescript


const runRet = await task.run(Resource.MyTask);




const taskArn = runRet.tasks[0].taskArn;


```

You can stop the task with the following.
src/app.ts

```typescript

const stopRet = await task.stop(Resource.MyTask, taskArn);

```

Stopping a task is asnychronous. When you call `stop`, AWS marks a task to be stopped, but it may take a few minutes for the task to actually stop.
Stopping a task in asyncrhonous.
In most cases you probably don’t need to check if it has been stopped. But if necessary, you can use the `describe` function to get a task’s status.
If you are not using Node.js, you can use the AWS SDK and call

### [DescribeResponse](https://sst.dev/docs/component/aws/task#describeresponse)

**Type** `Object`

* [`arn`](https://sst.dev/docs/component/aws/task#describeresponse-arn)
* [`response`](https://sst.dev/docs/component/aws/task#describeresponse-response)
* [`status`](https://sst.dev/docs/component/aws/task#describeresponse-status)

#### [DescribeResponse.arn](https://sst.dev/docs/component/aws/task#describeresponse-arn)

**Type** `string`
The ARN of the task.

#### [DescribeResponse.response](https://sst.dev/docs/component/aws/task#describeresponse-response)

**Type**
The raw response from the AWS ECS DescribeTasks API.

#### [DescribeResponse.status](https://sst.dev/docs/component/aws/task#describeresponse-status)

**Type** `string`
The status of the task.

### [Options](https://sst.dev/docs/component/aws/task#options)

**Type** `Object`

* [`aws?`](https://sst.dev/docs/component/aws/task#options-aws) `Object`
  * [`accessKeyId?`](https://sst.dev/docs/component/aws/task#options-aws-accesskeyid)
  * [`allHeaders?`](https://sst.dev/docs/component/aws/task#options-aws-allheaders)
  * [`appendSessionToken?`](https://sst.dev/docs/component/aws/task#options-aws-appendsessiontoken)
  * [`cache?`](https://sst.dev/docs/component/aws/task#options-aws-cache)
  * [`datetime?`](https://sst.dev/docs/component/aws/task#options-aws-datetime)
  * [`region?`](https://sst.dev/docs/component/aws/task#options-aws-region)
  * [`secretAccessKey?`](https://sst.dev/docs/component/aws/task#options-aws-secretaccesskey)
  * [`service?`](https://sst.dev/docs/component/aws/task#options-aws-service)
  * [`sessionToken?`](https://sst.dev/docs/component/aws/task#options-aws-sessiontoken)
  * [`signQuery?`](https://sst.dev/docs/component/aws/task#options-aws-signquery)
  * [`singleEncode?`](https://sst.dev/docs/component/aws/task#options-aws-singleencode)

#### [Options.aws?](https://sst.dev/docs/component/aws/task#options-aws)

**Type** `Object`
Configure the options for the

##### [Options.aws.accessKeyId?](https://sst.dev/docs/component/aws/task#options-aws-accesskeyid)

**Type** `string`

##### [Options.aws.allHeaders?](https://sst.dev/docs/component/aws/task#options-aws-allheaders)

**Type** `boolean`

##### [Options.aws.appendSessionToken?](https://sst.dev/docs/component/aws/task#options-aws-appendsessiontoken)

**Type** `boolean`

##### [Options.aws.cache?](https://sst.dev/docs/component/aws/task#options-aws-cache)

**Type** `Map``<``string`, `ArrayBuffer``<``>``>`

##### [Options.aws.datetime?](https://sst.dev/docs/component/aws/task#options-aws-datetime)

**Type** `string`

##### [Options.aws.region?](https://sst.dev/docs/component/aws/task#options-aws-region)

**Type** `string`

##### [Options.aws.secretAccessKey?](https://sst.dev/docs/component/aws/task#options-aws-secretaccesskey)

**Type** `string`

##### [Options.aws.service?](https://sst.dev/docs/component/aws/task#options-aws-service)

**Type** `string`

##### [Options.aws.sessionToken?](https://sst.dev/docs/component/aws/task#options-aws-sessiontoken)

**Type** `string`

##### [Options.aws.signQuery?](https://sst.dev/docs/component/aws/task#options-aws-signquery)

**Type** `boolean`

##### [Options.aws.singleEncode?](https://sst.dev/docs/component/aws/task#options-aws-singleencode)

**Type** `boolean`

### [Resource](https://sst.dev/docs/component/aws/task#resource)

**Type** `Object`

* [`assignPublicIp`](https://sst.dev/docs/component/aws/task#resource-assignpublicip)
* [`cluster`](https://sst.dev/docs/component/aws/task#resource-cluster)
* [`containers`](https://sst.dev/docs/component/aws/task#resource-containers)
* [`securityGroups`](https://sst.dev/docs/component/aws/task#resource-securitygroups)
* [`subnets`](https://sst.dev/docs/component/aws/task#resource-subnets)
* [`taskDefinition`](https://sst.dev/docs/component/aws/task#resource-taskdefinition)

#### [Resource.assignPublicIp](https://sst.dev/docs/component/aws/task#resource-assignpublicip)

**Type** `boolean`
Whether to assign a public IP address to the task.

#### [Resource.cluster](https://sst.dev/docs/component/aws/task#resource-cluster)

**Type** `string`
The ARN of the cluster.

#### [Resource.containers](https://sst.dev/docs/component/aws/task#resource-containers)

**Type** `string``[]`
The names of the containers in the task.

#### [Resource.securityGroups](https://sst.dev/docs/component/aws/task#resource-securitygroups)

**Type** `string``[]`
The security groups to use for the task.

#### [Resource.subnets](https://sst.dev/docs/component/aws/task#resource-subnets)

**Type** `string``[]`
The subnets to use for the task.

#### [Resource.taskDefinition](https://sst.dev/docs/component/aws/task#resource-taskdefinition)

**Type** `string`
The ARN of the task definition.

### [RunOptions](https://sst.dev/docs/component/aws/task#runoptions)

**Type** `Object`

* [`aws?`](https://sst.dev/docs/component/aws/task#runoptions-aws) `Object`
  * [`accessKeyId?`](https://sst.dev/docs/component/aws/task#runoptions-aws-accesskeyid)
  * [`allHeaders?`](https://sst.dev/docs/component/aws/task#runoptions-aws-allheaders)
  * [`appendSessionToken?`](https://sst.dev/docs/component/aws/task#runoptions-aws-appendsessiontoken)
  * [`cache?`](https://sst.dev/docs/component/aws/task#runoptions-aws-cache)
  * [`datetime?`](https://sst.dev/docs/component/aws/task#runoptions-aws-datetime)
  * [`region?`](https://sst.dev/docs/component/aws/task#runoptions-aws-region)
  * [`secretAccessKey?`](https://sst.dev/docs/component/aws/task#runoptions-aws-secretaccesskey)
  * [`service?`](https://sst.dev/docs/component/aws/task#runoptions-aws-service)
  * [`sessionToken?`](https://sst.dev/docs/component/aws/task#runoptions-aws-sessiontoken)
  * [`signQuery?`](https://sst.dev/docs/component/aws/task#runoptions-aws-signquery)
  * [`singleEncode?`](https://sst.dev/docs/component/aws/task#runoptions-aws-singleencode)
* [`capacity?`](https://sst.dev/docs/component/aws/task#runoptions-capacity)

#### [RunOptions.aws?](https://sst.dev/docs/component/aws/task#runoptions-aws)

**Type** `Object`
Configure the options for the

##### [RunOptions.aws.accessKeyId?](https://sst.dev/docs/component/aws/task#runoptions-aws-accesskeyid)

**Type** `string`

##### [RunOptions.aws.allHeaders?](https://sst.dev/docs/component/aws/task#runoptions-aws-allheaders)

**Type** `boolean`

##### [RunOptions.aws.appendSessionToken?](https://sst.dev/docs/component/aws/task#runoptions-aws-appendsessiontoken)

**Type** `boolean`

##### [RunOptions.aws.cache?](https://sst.dev/docs/component/aws/task#runoptions-aws-cache)

**Type** `Map``<``string`, `ArrayBuffer``<``>``>`

##### [RunOptions.aws.datetime?](https://sst.dev/docs/component/aws/task#runoptions-aws-datetime)

**Type** `string`

##### [RunOptions.aws.region?](https://sst.dev/docs/component/aws/task#runoptions-aws-region)

**Type** `string`

##### [RunOptions.aws.secretAccessKey?](https://sst.dev/docs/component/aws/task#runoptions-aws-secretaccesskey)

**Type** `string`

##### [RunOptions.aws.service?](https://sst.dev/docs/component/aws/task#runoptions-aws-service)

**Type** `string`

##### [RunOptions.aws.sessionToken?](https://sst.dev/docs/component/aws/task#runoptions-aws-sessiontoken)

**Type** `string`

##### [RunOptions.aws.signQuery?](https://sst.dev/docs/component/aws/task#runoptions-aws-signquery)

**Type** `boolean`

##### [RunOptions.aws.singleEncode?](https://sst.dev/docs/component/aws/task#runoptions-aws-singleencode)

**Type** `boolean`

#### [RunOptions.capacity?](https://sst.dev/docs/component/aws/task#runoptions-capacity)

**Type** `“``fargate``”`` | ``“``spot``”`
**Default** `“fargate”`
Configure the capacity provider; regular Fargate or Fargate Spot, for this task.

### [RunResponse](https://sst.dev/docs/component/aws/task#runresponse)

**Type** `Object`

* [`arn`](https://sst.dev/docs/component/aws/task#runresponse-arn)
* [`response`](https://sst.dev/docs/component/aws/task#runresponse-response)
* [`status`](https://sst.dev/docs/component/aws/task#runresponse-status)

#### [RunResponse.arn](https://sst.dev/docs/component/aws/task#runresponse-arn)

**Type** `string`
The ARN of the task.

#### [RunResponse.response](https://sst.dev/docs/component/aws/task#runresponse-response)

**Type**
The raw response from the AWS ECS RunTask API.

#### [RunResponse.status](https://sst.dev/docs/component/aws/task#runresponse-status)

**Type** `string`
The status of the task.

### [StopResponse](https://sst.dev/docs/component/aws/task#stopresponse)

**Type** `Object`

* [`arn`](https://sst.dev/docs/component/aws/task#stopresponse-arn)
* [`response`](https://sst.dev/docs/component/aws/task#stopresponse-response)
* [`status`](https://sst.dev/docs/component/aws/task#stopresponse-status)

#### [StopResponse.arn](https://sst.dev/docs/component/aws/task#stopresponse-arn)

**Type** `string`
The ARN of the task.

#### [StopResponse.response](https://sst.dev/docs/component/aws/task#stopresponse-response)

**Type**
The raw response from the AWS ECS StopTask API.

#### [StopResponse.status](https://sst.dev/docs/component/aws/task#stopresponse-status)

**Type** `string`
The status of the task.

[Skip to content](https://sst.dev/docs/component/cloudflare/binding#_top)

# Cloudflare Linkable helper

The Cloudflare Binding Linkable helper is used to define the Cloudflare bindings included with the [`sst.Linkable`](https://sst.dev/docs/component/linkable/) component.

```

sst.cloudflare.binding({

type: "r2BucketBindings",

properties: {

bucketName: "my-bucket"

}

})

```

* * *

## [Functions](https://sst.dev/docs/component/cloudflare/binding#functions)

### [binding](https://sst.dev/docs/component/cloudflare/binding#binding)

```

binding(input)

```

#### [Parameters](https://sst.dev/docs/component/cloudflare/binding#parameters)

* `input` [`KvBinding`](https://sst.dev/docs/component/cloudflare/binding#kvbinding)` | `[`SecretTextBinding`](https://sst.dev/docs/component/cloudflare/binding#secrettextbinding)` | `[`ServiceBinding`](https://sst.dev/docs/component/cloudflare/binding#servicebinding)` | `[`PlainTextBinding`](https://sst.dev/docs/component/cloudflare/binding#plaintextbinding)` | `[`QueueBinding`](https://sst.dev/docs/component/cloudflare/binding#queuebinding)` | `[`R2BucketBinding`](https://sst.dev/docs/component/cloudflare/binding#r2bucketbinding)` | `[`D1DatabaseBinding`](https://sst.dev/docs/component/cloudflare/binding#d1databasebinding)

**Returns** `Object`

## [D1DatabaseBinding](https://sst.dev/docs/component/cloudflare/binding#d1databasebinding)

### [properties](https://sst.dev/docs/component/cloudflare/binding#properties)

**Type** `Object`

* [`id`](https://sst.dev/docs/component/cloudflare/binding#properties-id)

#### [properties.id](https://sst.dev/docs/component/cloudflare/binding#properties-id)

**Type** `Input``<``string``>`

### [type](https://sst.dev/docs/component/cloudflare/binding#type)

**Type** `“``d1DatabaseBindings``”`

## [KvBinding](https://sst.dev/docs/component/cloudflare/binding#kvbinding)

### [properties](https://sst.dev/docs/component/cloudflare/binding#properties-1)

**Type** `Object`

* [`namespaceId`](https://sst.dev/docs/component/cloudflare/binding#properties-namespaceid)

#### [properties.namespaceId](https://sst.dev/docs/component/cloudflare/binding#properties-namespaceid)

**Type** `Input``<``string``>`

### [type](https://sst.dev/docs/component/cloudflare/binding#type-1)

**Type** `“``kvNamespaceBindings``”`

## [PlainTextBinding](https://sst.dev/docs/component/cloudflare/binding#plaintextbinding)

### [properties](https://sst.dev/docs/component/cloudflare/binding#properties-2)

**Type** `Object`

* [`text`](https://sst.dev/docs/component/cloudflare/binding#properties-text)

#### [properties.text](https://sst.dev/docs/component/cloudflare/binding#properties-text)

**Type** `Input``<``string``>`

### [type](https://sst.dev/docs/component/cloudflare/binding#type-2)

**Type** `“``plainTextBindings``”`

## [QueueBinding](https://sst.dev/docs/component/cloudflare/binding#queuebinding)

### [properties](https://sst.dev/docs/component/cloudflare/binding#properties-3)

**Type** `Object`

* [`queue`](https://sst.dev/docs/component/cloudflare/binding#properties-queue)

#### [properties.queue](https://sst.dev/docs/component/cloudflare/binding#properties-queue)

**Type** `Input``<``string``>`

### [type](https://sst.dev/docs/component/cloudflare/binding#type-3)

**Type** `“``queueBindings``”`

## [R2BucketBinding](https://sst.dev/docs/component/cloudflare/binding#r2bucketbinding)

### [properties](https://sst.dev/docs/component/cloudflare/binding#properties-4)

**Type** `Object`

* [`bucketName`](https://sst.dev/docs/component/cloudflare/binding#properties-bucketname)

#### [properties.bucketName](https://sst.dev/docs/component/cloudflare/binding#properties-bucketname)

**Type** `Input``<``string``>`

### [type](https://sst.dev/docs/component/cloudflare/binding#type-4)

**Type** `“``r2BucketBindings``”`

## [SecretTextBinding](https://sst.dev/docs/component/cloudflare/binding#secrettextbinding)

### [properties](https://sst.dev/docs/component/cloudflare/binding#properties-5)

**Type** `Object`

* [`text`](https://sst.dev/docs/component/cloudflare/binding#properties-text-1)

#### [properties.text](https://sst.dev/docs/component/cloudflare/binding#properties-text-1)

**Type** `Input``<``string``>`

### [type](https://sst.dev/docs/component/cloudflare/binding#type-5)

**Type** `“``secretTextBindings``”`

## [ServiceBinding](https://sst.dev/docs/component/cloudflare/binding#servicebinding)

### [properties](https://sst.dev/docs/component/cloudflare/binding#properties-6)

**Type** `Object`

* [`service`](https://sst.dev/docs/component/cloudflare/binding#properties-service)

#### [properties.service](https://sst.dev/docs/component/cloudflare/binding#properties-service)

**Type** `Input``<``string``>`

### [type](https://sst.dev/docs/component/cloudflare/binding#type-6)

**Type** `“``serviceBindings``”`

[Skip to content](https://sst.dev/docs/component/aws/permission#_top)

# AWS Linkable helper

The AWS Permission Linkable helper is used to define the AWS permissions included with the [`sst.Linkable`](https://sst.dev/docs/component/linkable/) component.

```

sst.aws.permission({

actions: ["lambda:InvokeFunction"],

resources: ["*"]

})

```

* * *

## [Functions](https://sst.dev/docs/component/aws/permission#functions)

### [permission](https://sst.dev/docs/component/aws/permission#permission)

```

permission(input)

```

#### [Parameters](https://sst.dev/docs/component/aws/permission#parameters)

* `input` [`InputArgs`](https://sst.dev/docs/component/aws/permission#inputargs)

**Returns** `Object`

## [InputArgs](https://sst.dev/docs/component/aws/permission#inputargs)

### [actions](https://sst.dev/docs/component/aws/permission#actions)

**Type** `string``[]`
The

```

{

actions: ["s3:*"]

}

```

### [effect?](https://sst.dev/docs/component/aws/permission#effect)

**Type** `“``allow``”`` | ``“``deny``”`
**Default** `“allow”`
Configures whether the permission is allowed or denied.

```

{

effect: "deny"

}

```

### [resources](https://sst.dev/docs/component/aws/permission#resources)

**Type** `Input``<``Input``<``string``>``[]``>`
The resourcess specified using the

```

{

resources: ["arn:aws:s3:::my-bucket/*"]

}

```

[Skip to content](https://sst.dev/docs/component/secret#_top)

# Secret

The `Secret` component lets you create secrets in your app.
Secrets are encrypted and stored in an S3 Bucket in your AWS account. If used in your app config, they’ll be encrypted in your state file as well. If used in your function code, they are encrypted and included in the bundle. They are then decrypted synchronously when your function starts up by the SST SDK.

#### [Create a secret](https://sst.dev/docs/component/secret#create-a-secret)

The name of a secret follows the same rules as a component name. It must start with a capital letter and contain only letters and numbers.
Secret names must start with a capital letter and contain only letters and numbers.
sst.config.ts

```typescript


const secret = newsst.Secret("MySecret");


```

#### [Set a placeholder](https://sst.dev/docs/component/secret#set-a-placeholder)

You can optionally set a `placeholder`.
Useful for cases where you might use a secret for values that aren’t sensitive, so you can just set them in code.
sst.config.ts

```typescript

const secret = newsst.Secret("MySecret", "my-secret-placeholder-value");

```

#### [Set the value of the secret](https://sst.dev/docs/component/secret#set-the-value-of-the-secret)

You can then set the value of a secret using the [CLI](https://sst.dev/docs/reference/cli/).
Terminal```

sstsecretsetMySecretmy-secret-value

```

If you are not running `sst dev`, you’ll need to `sst deploy` to apply the secret.

#### [Set a fallback for the secret](https://sst.dev/docs/component/secret#set-a-fallback-for-the-secret)

You can set a _fallback_ value for the secret with the `--fallback` flag. If the secret is not set for a stage, it’ll use the fallback value instead.
Terminal```

sstsecretsetMySecretmy-fallback-value--fallback

```

This is useful for PR environments that are auto-deployed.

#### [Use the secret in your app config](https://sst.dev/docs/component/secret#use-the-secret-in-your-app-config)

You can now use the secret in your app config.
sst.config.ts

```typescript


console.log(mySecret.value);


```

This is an [Output](https://sst.dev/docs/components#outputs) that can be used as an Input to other components.

#### [Link the secret to a resource](https://sst.dev/docs/component/secret#link-the-secret-to-a-resource)

You can link the secret to other resources, like a function or your Next.js app.
sst.config.ts

```typescript

new sst.aws.Nextjs("MyWeb", {

link: [secret]

});

```

Once linked, you can use the secret in your function code.
app/page.tsx```

import { Resource } from"sst";

console.log(Resource.MySecret.value);

```

* * *

## [Constructor](https://sst.dev/docs/component/secret#constructor)

```

newSecret(name, placeholder?)

```

#### [Parameters](https://sst.dev/docs/component/secret#parameters)

* `name` `string`
* `placeholder?` `Input``<``string``>`
A placeholder value of the secret. This can be useful for cases where you might not be storing sensitive values.

## [Properties](https://sst.dev/docs/component/secret#properties)

### [name](https://sst.dev/docs/component/secret#name)

**Type** `Output``<``string``>`
The name of the secret.

### [placeholder](https://sst.dev/docs/component/secret#placeholder)

**Type** `undefined`` | ``Output``<``string``>`
The placeholder value of the secret.

### [value](https://sst.dev/docs/component/secret#value)

**Type** `Output``<``string``>`
The value of the secret. It’ll be `undefined` if the secret has not been set through the CLI or if the `placeholder` hasn’t been set.

## [SDK](https://sst.dev/docs/component/secret#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/secret#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `value` `string`
The value of the secret. It’ll be `undefined` if the secret has not been set through the CLI or if the `placeholder` hasn’t been set.

[Skip to content](https://sst.dev/docs/component/aws/cognito-identity-pool#_top)

# CognitoIdentityPool

The `CognitoIdentityPool` component lets you add a

#### [Create the identity pool](https://sst.dev/docs/component/aws/cognito-identity-pool#create-the-identity-pool)

sst.config.ts
```typescript

new sst.aws.CognitoIdentityPool("MyIdentityPool", {

userPools: [

{

userPool: "us-east-1_QY6Ly46JH",

client: "6va5jg3cgtrd170sgokikjm5m6"

}

]

});

```

#### [Configure permissions for authenticated users](https://sst.dev/docs/component/aws/cognito-identity-pool#configure-permissions-for-authenticated-users)

sst.config.ts

```typescript


new sst.aws.CognitoIdentityPool("MyIdentityPool", {



userPools: [


{



userPool: "us-east-1_QY6Ly46JH",




client: "6va5jg3cgtrd170sgokikjm5m6"



}


],


permissions: {


authenticated: [


{



actions: ["s3:GetObject", "s3:PutObject"],




resources: ["arn:aws:s3:::my-bucket/*"]



}


]


}


});

```

* * *

## [Constructor](https://sst.dev/docs/component/aws/cognito-identity-pool#constructor)

```


newCognitoIdentityPool(name, args?, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cognito-identity-pool#parameters)

* `name` `string`
* `args?` [`CognitoIdentityPoolArgs`](https://sst.dev/docs/component/aws/cognito-identity-pool#cognitoidentitypoolargs)
* `opts?`

## [CognitoIdentityPoolArgs](https://sst.dev/docs/component/aws/cognito-identity-pool#cognitoidentitypoolargs)

### [permissions?](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions)

**Type** `Input``<``Object``>`

* [`authenticated?`](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-authenticated) `Input``<``Object``[]``>`
  * [`actions`](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-authenticated-actions)
  * [`effect?`](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-authenticated-effect)
  * [`resources`](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-authenticated-resources)
* [`unauthenticated?`](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-unauthenticated) `Input``<``Object``[]``>`
  * [`actions`](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-unauthenticated-actions)
  * [`effect?`](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-unauthenticated-effect)
  * [`resources`](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-unauthenticated-resources)

The permissions to attach to the authenticated and unauthenticated roles. This allows the authenticated and unauthenticated users to access other AWS resources.

```

{


permissions: {


authenticated: [


{



actions: ["s3:GetObject", "s3:PutObject"],




resources: ["arn:aws:s3:::my-bucket/*"]



}


],


unauthenticated: [


{



actions: ["s3:GetObject"],




resources: ["arn:aws:s3:::my-bucket/*"]



}


]


}


}

```

#### [permissions.authenticated?](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-authenticated)

**Type** `Input``<``Object``[]``>`
Attaches the given list of permissions to the authenticated users.

##### [permissions.authenticated[].actions](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-authenticated-actions)

**Type** `string``[]`
The

```

{



actions: ["s3:*"]



}

```

##### [permissions.authenticated[].effect?](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-authenticated-effect)

**Type** `“``allow``”`` | ``“``deny``”`
**Default** `“allow”`
Configures whether the permission is allowed or denied.

```

{



effect: "deny"



}

```

##### [permissions.authenticated[].resources](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-authenticated-resources)

**Type** `Input``<``Input``<``string``>``[]``>`
The resourcess specified using the

```

{



resources: ["arn:aws:s3:::my-bucket/*"]



}

```

#### [permissions.unauthenticated?](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-unauthenticated)

**Type** `Input``<``Object``[]``>`
Attaches the given list of permissions to the unauthenticated users.

##### [permissions.unauthenticated[].actions](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-unauthenticated-actions)

**Type** `string``[]`
The

```

{



actions: ["s3:*"]



}

```

##### [permissions.unauthenticated[].effect?](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-unauthenticated-effect)

**Type** `“``allow``”`` | ``“``deny``”`
**Default** `“allow”`
Configures whether the permission is allowed or denied.

```

{



effect: "deny"



}

```

##### [permissions.unauthenticated[].resources](https://sst.dev/docs/component/aws/cognito-identity-pool#permissions-unauthenticated-resources)

**Type** `Input``<``Input``<``string``>``[]``>`
The resourcess specified using the

```

{



resources: ["arn:aws:s3:::my-bucket/*"]



}

```

### [transform?](https://sst.dev/docs/component/aws/cognito-identity-pool#transform)

**Type** `Object`

* [`authenticatedRole?`](https://sst.dev/docs/component/aws/cognito-identity-pool#transform-authenticatedrole)
* [`identityPool?`](https://sst.dev/docs/component/aws/cognito-identity-pool#transform-identitypool)
* [`unauthenticatedRole?`](https://sst.dev/docs/component/aws/cognito-identity-pool#transform-unauthenticatedrole)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.authenticatedRole?](https://sst.dev/docs/component/aws/cognito-identity-pool#transform-authenticatedrole)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the authenticated IAM role resource.

#### [transform.identityPool?](https://sst.dev/docs/component/aws/cognito-identity-pool#transform-identitypool)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Cognito identity pool resource.

#### [transform.unauthenticatedRole?](https://sst.dev/docs/component/aws/cognito-identity-pool#transform-unauthenticatedrole)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the unauthenticated IAM role resource.

### [userPools?](https://sst.dev/docs/component/aws/cognito-identity-pool#userpools)

**Type** `Input``<``Input``<``Object``>``[]``>`

* [`client`](https://sst.dev/docs/component/aws/cognito-identity-pool#userpools-client)
* [`userPool`](https://sst.dev/docs/component/aws/cognito-identity-pool#userpools-userpool)

Configure Cognito User Pools as identity providers to your identity pool.

```

{


userPools: [


{



userPool: "us-east-1_QY6Ly46JH",




client: "6va5jg3cgtrd170sgokikjm5m6"



}


]


}

```

#### [userPools[].client](https://sst.dev/docs/component/aws/cognito-identity-pool#userpools-client)

**Type** `Input``<``string``>`
The Cognito User Pool client ID.

#### [userPools[].userPool](https://sst.dev/docs/component/aws/cognito-identity-pool#userpools-userpool)

**Type** `Input``<``string``>`
The Cognito user pool ID.

## [Properties](https://sst.dev/docs/component/aws/cognito-identity-pool#properties)

### [id](https://sst.dev/docs/component/aws/cognito-identity-pool#id)

**Type** `Output``<``string``>`
The Cognito identity pool ID.

### [nodes](https://sst.dev/docs/component/aws/cognito-identity-pool#nodes)

**Type** `Object`

* [`authenticatedRole`](https://sst.dev/docs/component/aws/cognito-identity-pool#nodes-authenticatedrole)
* [`identityPool`](https://sst.dev/docs/component/aws/cognito-identity-pool#nodes-identitypool)
* [`unauthenticatedRole`](https://sst.dev/docs/component/aws/cognito-identity-pool#nodes-unauthenticatedrole)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.authenticatedRole](https://sst.dev/docs/component/aws/cognito-identity-pool#nodes-authenticatedrole)

**Type**
The authenticated IAM role.

#### [nodes.identityPool](https://sst.dev/docs/component/aws/cognito-identity-pool#nodes-identitypool)

**Type**
The Amazon Cognito identity pool.

#### [nodes.unauthenticatedRole](https://sst.dev/docs/component/aws/cognito-identity-pool#nodes-unauthenticatedrole)

**Type**
The unauthenticated IAM role.

## [SDK](https://sst.dev/docs/component/aws/cognito-identity-pool#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/cognito-identity-pool#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `id` `string`
The Cognito identity pool ID.

## [Methods](https://sst.dev/docs/component/aws/cognito-identity-pool#methods)

### [static get](https://sst.dev/docs/component/aws/cognito-identity-pool#static-get)

```


CognitoIdentityPool.get(name, identityPoolID, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cognito-identity-pool#parameters-1)

* `name` `string`
The name of the component.
* `identityPoolID` `Input``<``string``>`
The ID of the existing Identity Pool.
* `opts?`

**Returns** [`CognitoIdentityPool`](https://sst.dev/docs/component/aws/)
Reference an existing Identity Pool with the given ID. This is useful when you create a Identity Pool in one stage and want to share it in another. It avoids having to create a new Identity Pool in the other stage.
You can use the `static get` method to share Identity Pools across stages.
Imagine you create a Identity Pool in the `dev` stage. And in your personal stage `frank`, instead of creating a new pool, you want to share the same pool from `dev`.
sst.config.ts

```typescript

const identityPool = $app.stage === "frank"

? sst.aws.CognitoIdentityPool.get("MyIdentityPool", "us-east-1:02facf30-e2f3-49ec-9e79-c55187415cf8")

:new sst.aws.CognitoIdentityPool("MyIdentityPool");

```

Here `us-east-1:02facf30-e2f3-49ec-9e79-c55187415cf8` is the ID of the Identity Pool created in the `dev` stage. You can find this by outputting the Identity Pool ID in the `dev` stage.
sst.config.ts

```typescript


return {




identityPool: identityPool.id



};

```

[Skip to content](https://sst.dev/docs/component/aws/sns-topic#_top)

# SnsTopic

The `SnsTopic` component lets you add an
The difference between an `SnsTopic` and a `Queue` is that with a topic you can deliver messages to multiple subscribers.

#### [Create a topic](https://sst.dev/docs/component/aws/sns-topic#create-a-topic)

sst.config.ts

```typescript

const topic = newsst.aws.SnsTopic("MyTopic");

```

#### [Make it a FIFO topic](https://sst.dev/docs/component/aws/sns-topic#make-it-a-fifo-topic)

You can optionally make it a FIFO topic.
sst.config.ts

```typescript


new sst.aws.SnsTopic("MyTopic", {




fifo: true



});

```

#### [Add a subscriber](https://sst.dev/docs/component/aws/sns-topic#add-a-subscriber)

sst.config.ts

```typescript

topic.subscribe("MySubscriber", "src/subscriber.handler");

```

#### [Link the topic to a resource](https://sst.dev/docs/component/aws/sns-topic#link-the-topic-to-a-resource)

You can link the topic to other resources, like a function or your Next.js app.
sst.config.ts

```typescript


new sst.aws.Nextjs("MyWeb", {



link: [topic]


});

```

Once linked, you can publish messages to the topic from your function code.
app/page.tsx```

import { Resource } from"sst";

import { SNSClient, PublishCommand } from"@aws-sdk/client-sns";

const sns = newSNSClient({});

await sns.send(newPublishCommand({

TopicArn: Resource.MyTopic.arn,

Message: "Hello from Next.js!"

}));

```

* * *
## [Constructor](https://sst.dev/docs/component/aws/sns-topic#constructor)
```

newSnsTopic(name, args?, opts?)

```

#### [Parameters](https://sst.dev/docs/component/aws/sns-topic#parameters)
  * `name` `string`
  * `args?` [`SnsTopicArgs`](https://sst.dev/docs/component/aws/sns-topic#snstopicargs)
  * `opts?`


## [SnsTopicArgs](https://sst.dev/docs/component/aws/sns-topic#snstopicargs)
### [fifo?](https://sst.dev/docs/component/aws/sns-topic#fifo)
**Type** `Input``<``boolean``>`
**Default** `false`
FIFO (First-In-First-Out) topics are designed to provide strict message ordering.
Changing a standard topic to a FIFO topic or the other way around will result in the destruction and recreation of the topic.
```

{

fifo: true

}

```

### [transform?](https://sst.dev/docs/component/aws/sns-topic#transform)
**Type** `Object`
  * [`topic?`](https://sst.dev/docs/component/aws/sns-topic#transform-topic)


[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.
####  [transform.topic?](https://sst.dev/docs/component/aws/sns-topic#transform-topic)
**Type** ` | ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the SNS Topic resource.
## [Properties](https://sst.dev/docs/component/aws/sns-topic#properties)
### [arn](https://sst.dev/docs/component/aws/sns-topic#arn)
**Type** `Output``<``string``>`
The ARN of the SNS Topic.
### [name](https://sst.dev/docs/component/aws/sns-topic#name)
**Type** `Output``<``string``>`
The name of the SNS Topic.
### [nodes](https://sst.dev/docs/component/aws/sns-topic#nodes)
**Type** `Object`
  * [`topic`](https://sst.dev/docs/component/aws/sns-topic#nodes-topic)


The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.
####  [nodes.topic](https://sst.dev/docs/component/aws/sns-topic#nodes-topic)
**Type**
The Amazon SNS Topic.
## [SDK](https://sst.dev/docs/component/aws/sns-topic#sdk)
Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *
### [Links](https://sst.dev/docs/component/aws/sns-topic#links)
This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).
  * `arn` `string`
The ARN of the SNS Topic.


## [Methods](https://sst.dev/docs/component/aws/sns-topic#methods)
### [subscribe](https://sst.dev/docs/component/aws/sns-topic#subscribe)
```

subscribe(name, subscriber, args?)

```

#### [Parameters](https://sst.dev/docs/component/aws/sns-topic#parameters-1)
  * `name` `string`
The name of the subscriber.
  * `subscriber` `Input``<``string`` | `[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)` | ``“arn:aws:lambda:${string}”``>`
The function that’ll be notified.
  * `args?` [`SnsTopicSubscriberArgs`](https://sst.dev/docs/component/aws/sns-topic#snstopicsubscriberargs)
Configure the subscription.


**Returns** `Output``<`[`SnsTopicLambdaSubscriber`](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber)`>`
Subscribe to this SNS Topic.
sst.config.ts
```typescript


topic.subscribe("MySubscriber", "src/subscriber.handler");


```

Add a filter to the subscription.
sst.config.ts

```typescript

topic.subscribe("MySubscriber", "src/subscriber.handler", {

filter: {

price_usd: [{numeric: [">=", 100]}]

}

});

```

Customize the subscriber function.
sst.config.ts

```typescript


topic.subscribe("MySubscriber", {




handler: "src/subscriber.handler",




timeout: "60 seconds"



});

```

Or pass in the ARN of an existing Lambda function.
sst.config.ts

```typescript

topic.subscribe("MySubscriber", "arn:aws:lambda:us-east-1:123456789012:function:my-function");

```

### [subscribeQueue](https://sst.dev/docs/component/aws/sns-topic#subscribequeue)

```

subscribeQueue(name, queue, args?)

```

#### [Parameters](https://sst.dev/docs/component/aws/sns-topic#parameters-2)

* `name` `string`
The name of the subscriber.
* `queue` `Input``<``string`` |`[`Queue`](https://sst.dev/docs/component/aws/queue)`>`
The ARN of the queue or `Queue` component that’ll be notified.
* `args?` [`SnsTopicSubscriberArgs`](https://sst.dev/docs/component/aws/sns-topic#snstopicsubscriberargs)
Configure the subscription.

**Returns** `Output``<`[`SnsTopicQueueSubscriber`](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber)`>`
Subscribe to this SNS Topic with an SQS Queue.
For example, let’s say you have a queue.
sst.config.ts

```typescript


const queue = sst.aws.Queue("MyQueue");


```

You can subscribe to this topic with it.
sst.config.ts

```typescript

topic.subscribeQueue("MySubscriber", queue.arn);

```

Add a filter to the subscription.
sst.config.ts

```typescript


topic.subscribeQueue("MySubscriber", queue.arn, {



filter: {



price_usd: [{numeric: [">=", 100]}]



}


});

```

### [static get](https://sst.dev/docs/component/aws/sns-topic#static-get)

```


SnsTopic.get(name, topicArn, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/sns-topic#parameters-3)

* `name` `string`
The name of the component.
* `topicArn` `Input``<``string``>`
The ARN of the existing SNS Topic.
* `opts?`

**Returns** [`SnsTopic`](https://sst.dev/docs/component/aws/)
Reference an existing SNS topic with its topic ARN. This is useful when you create a topic in one stage and want to share it in another stage. It avoids having to create a new topic in the other stage.
You can use the `static get` method to share SNS topics across stages.
Imagine you create a topic in the `dev` stage. And in your personal stage `frank`, instead of creating a new topic, you want to share the topic from `dev`.
sst.config.ts

```typescript

const topic = $app.stage === "frank"

? sst.aws.SnsTopic.get("MyTopic", "arn:aws:sns:us-east-1:123456789012:MyTopic")

:new sst.aws.SnsTopic("MyTopic");

```

Here `arn:aws:sns:us-east-1:123456789012:MyTopic` is the ARN of the topic created in the `dev` stage. You can find this by outputting the topic ARN in the `dev` stage.
sst.config.ts

```typescript


return topic.arn;


```

### [static subscribe](https://sst.dev/docs/component/aws/sns-topic#static-subscribe)

```


SnsTopic.subscribe(name, topicArn, subscriber, args?)


```

#### [Parameters](https://sst.dev/docs/component/aws/sns-topic#parameters-4)

* `name` `string`
The name of the subscriber.
* `topicArn` `Input``<``string``>`
The ARN of the SNS Topic to subscribe to.
* `subscriber` `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
The function that’ll be notified.
* `args?` [`SnsTopicSubscriberArgs`](https://sst.dev/docs/component/aws/sns-topic#snstopicsubscriberargs)
Configure the subscription.

**Returns** `Output``<`[`SnsTopicLambdaSubscriber`](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber)`>`
Subscribe to an SNS Topic that was not created in your app.
For example, let’s say you have an existing SNS Topic with the following ARN.
sst.config.ts

```typescript

const topicArn = "arn:aws:sns:us-east-1:123456789012:MyTopic";

```

You can subscribe to it by passing in the ARN.
sst.config.ts

```typescript


sst.aws.SnsTopic.subscribe("MySubscriber", topicArn, "src/subscriber.handler");


```

Add a filter to the subscription.
sst.config.ts

```typescript

sst.aws.SnsTopic.subscribe("MySubscriber", topicArn, "src/subscriber.handler", {

filter: {

price_usd: [{numeric: [">=", 100]}]

}

});

```

Customize the subscriber function.
sst.config.ts

```typescript


sst.aws.SnsTopic.subscribe("MySubscriber", topicArn, {




handler: "src/subscriber.handler",




timeout: "60 seconds"



});

```

### [static subscribeQueue](https://sst.dev/docs/component/aws/sns-topic#static-subscribequeue)

```


SnsTopic.subscribeQueue(name, topicArn, queue, args?)


```

#### [Parameters](https://sst.dev/docs/component/aws/sns-topic#parameters-5)

* `name` `string`
The name of the subscriber.
* `topicArn` `Input``<``string``>`
The ARN of the SNS Topic to subscribe to.
* `queue` `Input``<``string`` |`[`Queue`](https://sst.dev/docs/component/aws/queue)`>`
The ARN of the queue or `Queue` component that’ll be notified.
* `args?` [`SnsTopicSubscriberArgs`](https://sst.dev/docs/component/aws/sns-topic#snstopicsubscriberargs)
Configure the subscription.

**Returns** `Output``<`[`SnsTopicQueueSubscriber`](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber)`>`
Subscribe to an existing SNS Topic with a previously created SQS Queue.
For example, let’s say you have an existing SNS Topic and SQS Queue with the following ARNs.
sst.config.ts

```typescript

const topicArn = "arn:aws:sns:us-east-1:123456789012:MyTopic";

const queueArn = "arn:aws:sqs:us-east-1:123456789012:MyQueue";

```

You can subscribe to the topic with the queue.
sst.config.ts

```typescript


sst.aws.SnsTopic.subscribeQueue("MySubscriber", topicArn, queueArn);


```

Add a filter to the subscription.
sst.config.ts

```typescript

sst.aws.SnsTopic.subscribeQueue("MySubscriber", topicArn, queueArn, {

filter: {

price_usd: [{numeric: [">=", 100]}]

}

});

```

## [SnsTopicSubscriberArgs](https://sst.dev/docs/component/aws/sns-topic#snstopicsubscriberargs)

### [filter?](https://sst.dev/docs/component/aws/sns-topic#filter)

**Type** `Input``<``Record``<``string`, `any``>``>`
Filter the messages that’ll be processed by the subscriber.
If any single property in the filter doesn’t match an attribute assigned to the message, then the policy rejects the message.
Learn more about
For example, if your SNS Topic message contains this in a JSON format.

```

{

store: "example_corp",

event: "order-placed",

customer_interests: [

"soccer",

"rugby",

"hockey"

],

price_usd: 210.75

}

```

Then this filter policy accepts the message.

```

{

filter: {

store: ["example_corp"],

event: [{"anything-but": "order_cancelled"}],

customer_interests: [

"rugby",

"football",

"baseball"

],

price_usd: [{numeric: [">=", 100]}]

}

}

```

### [transform?](https://sst.dev/docs/component/aws/sns-topic#transform-1)

**Type** `Object`

* [`subscription?`](https://sst.dev/docs/component/aws/sns-topic#transform-subscription)

[Transform](https://sst.dev/docs/components#transform) how this subscription creates its underlying resources.

#### [transform.subscription?](https://sst.dev/docs/component/aws/sns-topic#transform-subscription)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the SNS Topic Subscription resource.

[Skip to content](https://sst.dev/docs/component/aws/cognito-user-pool#_top)

# CognitoUserPool

The `CognitoUserPool` component lets you add a

#### [Create the user pool](https://sst.dev/docs/component/aws/cognito-user-pool#create-the-user-pool)

sst.config.ts

```typescript


const userPool = newsst.aws.CognitoUserPool("MyUserPool");


```

#### [Login using email](https://sst.dev/docs/component/aws/cognito-user-pool#login-using-email)

sst.config.ts

```typescript

new sst.aws.CognitoUserPool("MyUserPool", {

usernames: ["email"]

});

```

#### [Configure triggers](https://sst.dev/docs/component/aws/cognito-user-pool#configure-triggers)

sst.config.ts

```typescript


new sst.aws.CognitoUserPool("MyUserPool", {



triggers: {



preAuthentication: "src/preAuthentication.handler",




postAuthentication: "src/postAuthentication.handler",



},


});

```

#### [Add Google identity provider](https://sst.dev/docs/component/aws/cognito-user-pool#add-google-identity-provider)

sst.config.ts

```typescript

const GoogleClientId = newsst.Secret("GOOGLE_CLIENT_ID");

const GoogleClientSecret = newsst.Secret("GOOGLE_CLIENT_SECRET");

userPool.addIdentityProvider({

type: "google",

details: {

authorize_scopes: "email profile",

client_id: GoogleClientId.value,

client_secret: GoogleClientSecret.value,

},

attributes: {

email: "email",

name: "name",

username: "sub",

},

});

```

#### [Add a client](https://sst.dev/docs/component/aws/cognito-user-pool#add-a-client)

sst.config.ts

```typescript


userPool.addClient("Web");


```

* * *

## [Constructor](https://sst.dev/docs/component/aws/cognito-user-pool#constructor)

```


newCognitoUserPool(name, args?, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cognito-user-pool#parameters)

* `name` `string`
* `args?` [`CognitoUserPoolArgs`](https://sst.dev/docs/component/aws/cognito-user-pool#cognitouserpoolargs)
* `opts?`

## [CognitoUserPoolArgs](https://sst.dev/docs/component/aws/cognito-user-pool#cognitouserpoolargs)

### [advancedSecurity?](https://sst.dev/docs/component/aws/cognito-user-pool#advancedsecurity)

**Type** `Input``<``“``audit``”`` | ``“``enforced``”``>`
**Default** Advanced security is disabled.
Enable advanced security features.
Learn more about

```

{



advancedSecurity: "enforced"



}

```

### [aliases?](https://sst.dev/docs/component/aws/cognito-user-pool#aliases)

**Type** `Input``<``Input``<``“``email``”`` | ``“``phone``”`` | ``“``preferred_username``”``>``[]``>`
**Default** User can only sign in with their username.
Configure the different ways a user can sign in besides using their username.
You cannot change the aliases property once the User Pool has been created. Learn more about

```

{



aliases: ["email"]



}

```

### [mfa?](https://sst.dev/docs/component/aws/cognito-user-pool#mfa)

**Type** `Input``<``“``on``”`` | ``“``optional``”``>`
**Default** MFA is disabled.
Configure the multi-factor authentication (MFA) settings for the User Pool.
If you enable MFA using `on` or `optional`, you need to configure either `sms` or `softwareToken` as well.

```

{



mfa: "on"



}

```

### [sms?](https://sst.dev/docs/component/aws/cognito-user-pool#sms)

**Type** `Input``<``Object``>`

* [`externalId`](https://sst.dev/docs/component/aws/cognito-user-pool#sms-externalid)
* [`snsCallerArn`](https://sst.dev/docs/component/aws/cognito-user-pool#sms-snscallerarn)
* [`snsRegion?`](https://sst.dev/docs/component/aws/cognito-user-pool#sms-snsregion)

**Default** No SMS settings.
Configure the SMS settings for the User Pool.

```

{


sms: {



externalId: "1234567890",




snsCallerArn: "arn:aws:iam::1234567890:role/CognitoSnsCaller",




snsRegion: "us-east-1",



}


}

```

#### [sms.externalId](https://sst.dev/docs/component/aws/cognito-user-pool#sms-externalid)

**Type** `Input``<``string``>`
The external ID used in IAM role trust relationships.
Learn more about

#### [sms.snsCallerArn](https://sst.dev/docs/component/aws/cognito-user-pool#sms-snscallerarn)

**Type** `Input``<``string``>`
The ARN of the IAM role that Amazon Cognito can assume to access the Amazon SNS

#### [sms.snsRegion?](https://sst.dev/docs/component/aws/cognito-user-pool#sms-snsregion)

**Type** `Input``<``string``>`
The AWS Region that Amazon Cognito uses to send SMS messages.

### [smsAuthenticationMessage?](https://sst.dev/docs/component/aws/cognito-user-pool#smsauthenticationmessage)

**Type** `Input``<``string``>`
**Default** The default message template.
The message template for SMS messages sent to users who are being authenticated.
The template must include the `{####}` placeholder, which will be replaced with the verification code.

```

{



smsAuthenticationMessage: "Your authentication code is {####}"



}

```

### [softwareToken?](https://sst.dev/docs/component/aws/cognito-user-pool#softwaretoken)

**Type** `Input``<``boolean``>`
**Default** `false`
Enable software token MFA for the User Pool.

```

{



softwareToken: true



}

```

### [transform?](https://sst.dev/docs/component/aws/cognito-user-pool#transform)

**Type** `Object`

* [`userPool?`](https://sst.dev/docs/component/aws/cognito-user-pool#transform-userpool)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.userPool?](https://sst.dev/docs/component/aws/cognito-user-pool#transform-userpool)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Cognito User Pool resource.

### [triggers?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers)

**Type** `Input``<``Object``>`

* [`createAuthChallenge?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-createauthchallenge)
* [`customEmailSender?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-customemailsender)
* [`customMessage?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-custommessage)
* [`customSmsSender?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-customsmssender)
* [`defineAuthChallenge?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-defineauthchallenge)
* [`kmsKey?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-kmskey)
* [`postAuthentication?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-postauthentication)
* [`postConfirmation?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-postconfirmation)
* [`preAuthentication?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-preauthentication)
* [`preSignUp?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-presignup)
* [`preTokenGeneration?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-pretokengeneration)
* [`preTokenGenerationVersion?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-pretokengenerationversion)
* [`userMigration?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-usermigration)
* [`verifyAuthChallengeResponse?`](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-verifyauthchallengeresponse)

**Default** No triggers
Configure triggers for this User Pool

```

{


triggers: {



preAuthentication: "src/preAuthentication.handler",




postAuthentication: "src/postAuthentication.handler"



}


}

```

#### [triggers.createAuthChallenge?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-createauthchallenge)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered after the user successfully responds to the previous challenge, and a new challenge needs to be created.
Takes the handler path, the function args, or a function ARN.

#### [triggers.customEmailSender?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-customemailsender)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered during events like user sign-up, password recovery, email/phone number verification, and when an admin creates a user. Use this trigger to customize the email provider.
Takes the handler path, the function args, or a function ARN.

#### [triggers.customMessage?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-custommessage)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered during events like user sign-up, password recovery, email/phone number verification, and when an admin creates a user. Use this trigger to customize the message that is sent to your users.
Takes the handler path, the function args, or a function ARN.

#### [triggers.customSmsSender?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-customsmssender)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered when an SMS message needs to be sent, such as for MFA or verification codes. Use this trigger to customize the SMS provider.
Takes the handler path, the function args, or a function ARN.

#### [triggers.defineAuthChallenge?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-defineauthchallenge)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered after each challenge response to determine the next action. Evaluates whether the user has completed the authentication process or if additional challenges are needed. ARN of the lambda function to name a custom challenge.
Takes the handler path, the function args, or a function ARN.

#### [triggers.kmsKey?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-kmskey)

**Type** `Input``<``string``>`
The ARN of the AWS KMS key used for encryption.
When `customEmailSender` or `customSmsSender` are configured, Cognito encrypts the verification code and temporary passwords before sending them to your Lambda functions.

#### [triggers.postAuthentication?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-postauthentication)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered after a successful authentication event. Use this to perform custom actions, such as logging or modifying user attributes, after the user is authenticated.
Takes the handler path, the function args, or a function ARN.

#### [triggers.postConfirmation?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-postconfirmation)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered after a user is successfully confirmed; sign-up or email/phone number verification. Use this to perform additional actions, like sending a welcome email or initializing user data, after user confirmation.
Takes the handler path, the function args, or a function ARN.

#### [triggers.preAuthentication?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-preauthentication)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered before the authentication process begins. Use this to implement custom validation or checks (like checking if the user is banned) before continuing authentication.
Takes the handler path, the function args, or a function ARN.

#### [triggers.preSignUp?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-presignup)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered before the user sign-up process completes. Use this to perform custom validation, auto-confirm users, or auto-verify attributes based on custom logic.
Takes the handler path, the function args, or a function ARN.

#### [triggers.preTokenGeneration?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-pretokengeneration)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered before tokens are generated in the authentication process. Use this to customize or add claims to the tokens that will be generated and returned to the user.
Takes the handler path, the function args, or a function ARN.

#### [triggers.preTokenGenerationVersion?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-pretokengenerationversion)

**Type** `“``v2``”`` | ``“``v1``”`
**Default** `“v1”`
The version of the preTokenGeneration trigger to use. Higher versions have access to more information that support new features.

#### [triggers.userMigration?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-usermigration)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered when a user attempts to sign in but does not exist in the current user pool. Use this to import and validate users from an existing user directory into the Cognito User Pool during sign-in.
Takes the handler path, the function args, or a function ARN.

#### [triggers.verifyAuthChallengeResponse?](https://sst.dev/docs/component/aws/cognito-user-pool#triggers-verifyauthchallengeresponse)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
Triggered after the user responds to a custom authentication challenge. Use this to verify the user’s response to the challenge and determine whether to continue authenticating the user.
Takes the handler path, the function args, or a function ARN.

### [usernames?](https://sst.dev/docs/component/aws/cognito-user-pool#usernames)

**Type** `Input``<``Input``<``“``email``”`` | ``“``phone``”``>``[]``>`
**Default** User can only sign in with their username.
Allow users to be able to sign up and sign in with an email addresses or phone number as their username.
You cannot change the usernames property once the User Pool has been created. Learn more about

```

{



usernames: ["email"]



}

```

### [verify?](https://sst.dev/docs/component/aws/cognito-user-pool#verify)

**Type** `Input``<``Object``>`

* [`emailMessage?`](https://sst.dev/docs/component/aws/cognito-user-pool#verify-emailmessage)
* [`emailSubject?`](https://sst.dev/docs/component/aws/cognito-user-pool#verify-emailsubject)
* [`smsMessage?`](https://sst.dev/docs/component/aws/cognito-user-pool#verify-smsmessage)

Configure the verification message sent to users who are being authenticated.

#### [verify.emailMessage?](https://sst.dev/docs/component/aws/cognito-user-pool#verify-emailmessage)

**Type** `Input``<``string``>`
**Default** `“The verification code to your new account is {####}”`
The template for email messages sent to users who are being authenticated.
The template must include the `{####}` placeholder, which will be replaced with the verification code.

```

{


verify: {



emailMessage: "The verification code to your new Awesome account is {####}"



}


}

```

#### [verify.emailSubject?](https://sst.dev/docs/component/aws/cognito-user-pool#verify-emailsubject)

**Type** `Input``<``string``>`
**Default** `“Verify your new account”`
Subject line for Email messages sent to users who are being authenticated.

```

{


verify: {



emailSubject: "Verify your new Awesome account"



}


}

```

#### [verify.smsMessage?](https://sst.dev/docs/component/aws/cognito-user-pool#verify-smsmessage)

**Type** `Input``<``string``>`
**Default** `“The verification code to your new account is {####}”`
The template for SMS messages sent to users who are being authenticated.
The template must include the `{####}` placeholder, which will be replaced with the verification code.

```

{


verify: {



smsMessage: "The verification code to your new Awesome account is {####}"



}


}

```

## [Properties](https://sst.dev/docs/component/aws/cognito-user-pool#properties)

### [arn](https://sst.dev/docs/component/aws/cognito-user-pool#arn)

**Type** `Output``<``string``>`
The Cognito User Pool ARN.

### [id](https://sst.dev/docs/component/aws/cognito-user-pool#id)

**Type** `Output``<``string``>`
The Cognito User Pool ID.

### [nodes](https://sst.dev/docs/component/aws/cognito-user-pool#nodes)

**Type** `Object`

* [`userPool`](https://sst.dev/docs/component/aws/cognito-user-pool#nodes-userpool)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.userPool](https://sst.dev/docs/component/aws/cognito-user-pool#nodes-userpool)

**Type** `Output``<``>`
The Amazon Cognito User Pool.

## [SDK](https://sst.dev/docs/component/aws/cognito-user-pool#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/cognito-user-pool#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `id` `string`
The Cognito User Pool ID.

## [Methods](https://sst.dev/docs/component/aws/cognito-user-pool#methods)

### [addClient](https://sst.dev/docs/component/aws/cognito-user-pool#addclient)

```


addClient(name, args?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cognito-user-pool#parameters-1)

* `name` `string`
Name of the client.
* `args?` [`CognitoUserPoolClientArgs`](https://sst.dev/docs/component/aws/cognito-user-pool#cognitouserpoolclientargs)
Configure the client.

**Returns** [`CognitoUserPoolClient`](https://sst.dev/docs/component/aws/cognito-user-pool-client)
Add a client to the User Pool.

```


userPool.addClient("Web");


```

### [addIdentityProvider](https://sst.dev/docs/component/aws/cognito-user-pool#addidentityprovider)

```


addIdentityProvider(name, args)


```

#### [Parameters](https://sst.dev/docs/component/aws/cognito-user-pool#parameters-2)

* `name` `string`
Name of the identity provider.
* `args` [`CognitoIdentityProviderArgs`](https://sst.dev/docs/component/aws/cognito-user-pool#cognitoidentityproviderargs)
Configure the identity provider.

**Returns** [`CognitoIdentityProvider`](https://sst.dev/docs/component/aws/cognito-identity-provider)
Add a federated identity provider to the User Pool.
For example, add a GitHub (OIDC) identity provider.
sst.config.ts

```typescript

const GithubClientId = newsst.Secret("GITHUB_CLIENT_ID");

const GithubClientSecret = newsst.Secret("GITHUB_CLIENT_SECRET");

userPool.addIdentityProvider("GitHub", {

type: "oidc",

details: {

authorize_scopes: "read:user user:email",

client_id: GithubClientId.value,

client_secret: GithubClientSecret.value,

oidc_issuer: "<https://github.com/>",

},

attributes: {

email: "email",

username: "sub",

},

});

```

Or add a Google identity provider.
sst.config.ts

```typescript


const GoogleClientId = newsst.Secret("GOOGLE_CLIENT_ID");




const GoogleClientSecret = newsst.Secret("GOOGLE_CLIENT_SECRET");




userPool.addIdentityProvider("Google", {




type: "google",



details: {



authorize_scopes: "email profile",




client_id: GoogleClientId.value,




client_secret: GoogleClientSecret.value,



},


attributes: {



email: "email",




name: "name",




username: "sub",



},


});

```

### [static get](https://sst.dev/docs/component/aws/cognito-user-pool#static-get)

```


CognitoUserPool.get(name, userPoolID, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cognito-user-pool#parameters-3)

* `name` `string`
The name of the component.
* `userPoolID` `Input``<``string``>`
The ID of the existing User Pool.
* `opts?`

**Returns** [`CognitoUserPool`](https://sst.dev/docs/component/aws/)
Reference an existing User Pool with the given ID. This is useful when you create a User Pool in one stage and want to share it in another. It avoids having to create a new User Pool in the other stage.
You can use the `static get` method to share User Pools across stages.
Imagine you create a User Pool in the `dev` stage. And in your personal stage `frank`, instead of creating a new pool, you want to share the same pool from `dev`.
sst.config.ts

```typescript

const userPool = $app.stage === "frank"

? sst.aws.CognitoUserPool.get("MyUserPool", "us-east-1_gcF5PjhQK")

:new sst.aws.CognitoUserPool("MyUserPool");

```

Here `us-east-1_gcF5PjhQK` is the ID of the User Pool created in the `dev` stage. You can find this by outputting the User Pool ID in the `dev` stage.
sst.config.ts

```typescript


return {




userPool: userPool.id



};

```

## [CognitoIdentityProviderArgs](https://sst.dev/docs/component/aws/cognito-user-pool#cognitoidentityproviderargs)

### [attributes?](https://sst.dev/docs/component/aws/cognito-user-pool#attributes)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Define a mapping between identity provider attributes and user pool attributes.

```

{



email: "email",




username: "sub"



}

```

### [details](https://sst.dev/docs/component/aws/cognito-user-pool#details)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Configure the identity provider details, including the scopes, URLs, and identifiers.

```

{



authorize_scopes: "email profile",




client_id: "your-client-id",




client_secret: "your-client-secret"



}

```

### [transform?](https://sst.dev/docs/component/aws/cognito-user-pool#transform-1)

**Type** `Object`

* [`identityProvider?`](https://sst.dev/docs/component/aws/cognito-user-pool#transform-identityprovider)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.identityProvider?](https://sst.dev/docs/component/aws/cognito-user-pool#transform-identityprovider)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Cognito identity provider resource.

### [type](https://sst.dev/docs/component/aws/cognito-user-pool#type)

**Type** `Input``<``“``oidc``”`` | ``“``saml``”`` | ``“``google``”`` | ``“``facebook``”`` | ``“``apple``”`` | ``“``amazon``”``>`
The type of identity provider.

## [CognitoUserPoolClientArgs](https://sst.dev/docs/component/aws/cognito-user-pool#cognitouserpoolclientargs)

### [providers?](https://sst.dev/docs/component/aws/cognito-user-pool#providers)

**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `[“COGNITO”]`
A list of identity providers that are supported for this client.
Reference federated identity providers using their `providerName` property.
If you are using a federated identity provider.
sst.config.ts

```typescript

const provider = userPool.addIdentityProvider("MyProvider", {

type: "oidc",

details: {

authorize_scopes: "email profile",

client_id: "your-client-id",

client_secret: "your-client-secret"

},

});

```

Make sure to pass in `provider.providerName` instead of hardcoding it to `"MyProvider"`.
sst.config.ts

```typescript


userPool.addClient("Web", {




providers: [provider.providerName]



});

```

This ensures the client is created after the provider.

### [transform?](https://sst.dev/docs/component/aws/cognito-user-pool#transform-2)

**Type** `Object`

* [`client?`](https://sst.dev/docs/component/aws/cognito-user-pool#transform-client)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.client?](https://sst.dev/docs/component/aws/cognito-user-pool#transform-client)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Cognito User Pool client resource.

[Skip to content](https://sst.dev/docs/configure-a-router#_top)

# Configure a Router

You can set [custom domains](https://sst.dev/docs/custom-domains) on components like your frontends, APIs, or services. Each of these create their own CloudFront distribution. But as your app grows you might:

  1. Have multiple frontends, like a landing page, or a docs site, etc.
  2. Want to serve resources from different paths of the same domain; like `/docs`, or `/api`.
  3. Want to set up preview environments on subdomains.

Also since CloudFront distributions can take 15-20 minutes to deploy, creating new distributions for each of the components, and for each stage, can really impact how long it takes to deploy your app.
The `Router` lets you create and share a single CloudFront distribution for your entire app.
The ideal setup here is to create a single CloudFront distribution for your entire app and share that across components and across stages.
Let’s look at how to do this with the `Router` component.
* * *

#### [A sample app](https://sst.dev/docs/configure-a-router#a-sample-app)

To demo this, let’s say you have the following components in your app.
sst.config.ts

```typescript

// Frontend

const web = newsst.aws.Nextjs("MyWeb", {

path: "packages/web"

});

// API

const api = newsst.aws.Function("MyApi", {

url: true,

handler: "packages/functions/api.handler"

});

// Docs

const docs = newsst.aws.Astro("MyDocs", {

path: "packages/docs"

});

```

This has a frontend, a docs site, and an API. In production we’d like to have:

* `example.com` serve `MyWeb`
* `example.com/api` serve `MyApi`
* `docs.example.com` serve `MyDocs`

We’ll create a Router for production.
In our dev stage we’d like to have:

* `dev.example.com` serve `MyWeb`
* `dev.example.com/api` serve `MyApi`
* `docs.dev.example.com` serve `MyDocs`

For our PR stages or preview environments we’d like to have:

* `pr-123.dev.example.com` serve `MyWeb`
* `pr-123.dev.example.com/api` serve `MyApi`
* `docs-pr-123.dev.example.com` serve `MyDocs`

We’ll create a separate Router for the dev stage and share it across all the PR stages.
We are doing `docs-pr-123.dev.` instead of `docs.pr-123.dev.` because of a limitation with custom domains in CloudFront that we’ll look at below.
Let’s set this up.
* * *

## [Add a router](https://sst.dev/docs/configure-a-router#add-a-router)

Instead of adding custom domains to each component, let’s add a `Router` to our app with the domain we are going to use in production.
sst.config.ts

```typescript


const router = newsst.aws.Router("MyRouter", {



domain: {



name: "example.com",




aliases: ["*.example.com"]



}



});


```

The `*.example.com` alias is because we want to route to the `docs.` subdomain.
And use that in our components.
sst.config.ts

```typescript

// Frontend

const web = newsst.aws.Nextjs("MyWeb", {

path: "packages/web",

router

});

// API

const api = newsst.aws.Function("MyApi", {

handler: "packages/functions/api.handler",

router,

"/api"

});

// Docs

const docs = newsst.aws.Astro("MyDocs", {

path: "packages/docs",

router,

"docs.example.com"

});

```

Next, let’s configure the dev stage.
* * *

## [Stage based domains](https://sst.dev/docs/configure-a-router#stage-based-domains)

Since we also want to configure domains for our dev stage, let’s add a function that returns the domain we want, based on the stage.
sst.config.ts

```typescript


const domain = $app.stage === "production"




?"example.com"




: $app.stage==="dev"




?"dev.example.com"




:undefined;


```

Now when we deploy the dev stage, we’ll create a new `Router` with our dev domain.
sst.config.ts

```typescript

const router = newsst.aws.Router("MyRouter", {

domain: {

"example.com",

 ["*.example.com"]

name: domain,

 [`*.${domain}`]

}

});

```

And update the `MyDocs` component to use this.
sst.config.ts

```typescript

// Docs



const docs = newsst.aws.Astro("MyDocs", {




path: "packages/docs",



router: {



instance: router,




"docs.example.com"




domain: `docs.${domain}`



}



});


```

* * *

## [Preview environments](https://sst.dev/docs/configure-a-router#preview-environments)

Currently, we create a new CloudFront distribution for dev and production. But we want to **share the same distribution from dev** in our PR stages.
* * *

### [Share the router](https://sst.dev/docs/configure-a-router#share-the-router)

To do that, let’s modify how we create the `Router`.
sst.config.ts

```typescript

const router = newsst.aws.Router("MyRouter", {

const router = isPermanentStage

? new sst.aws.Router("MyRouter", {

domain: {

name: domain,

aliases: [`*.${domain}`]

}

})

sst.aws.Router.get("MyRouter", "A2WQRGCYGTFB7Z");

```

The `A2WQRGCYGTFB7Z` is the ID of the Router distribution created in the dev stage. You can look this up in the SST Console or output it when you deploy your dev stage.
sst.config.ts

```typescript


return {




router: router.distributionID



};

```

We are also defining `isPermanentStage`. This is set to `true` if the stage is `dev` or `production`.
sst.config.ts

```typescript

const isPermanentStage = ["production", "dev"].includes($app.stage);

```

Let’s also update our `domain` helper.
sst.config.ts

```typescript


const domain = $app.stage === "production"




?"example.com"




: $app.stage==="dev"




?"dev.example.com"




:undefined;




: `${$app.stage}.dev.example.com`;


```

Since the domain alias for the dev stage is set to `*.dev.example.com`, it can match `pr-123.dev.example.com`. But not `docs.pr-123.dev.example.com`. This is a limitation of CloudFront.
* * *

### [Nested subdomains](https://sst.dev/docs/configure-a-router#nested-subdomains)

So we’ll be using `docs-pr-123.dev.example.com` instead.
Nested wildcards domain patterns are not supported.
To do this, let’s add a helper function.
sst.config.ts

```typescript

functionsubdomain(name:string) {

if (isPermanentStage) return`${name}.${domain}`;

return`${name}-${domain}`;

}

```

This will add the `-` for our PR stages. Let’s update our `MyDocs` component to use this.
sst.config.ts

```typescript

// Docs



const docs = newsst.aws.Astro("MyDocs", {




path: "packages/docs",



router: {



instance: router,




`docs.${domain}`




domain: subdomain("docs")



}



});


```

* * *

## [Wrapping up](https://sst.dev/docs/configure-a-router#wrapping-up)

And that’s it! We’ve now configured our router to serve our entire app.
Here’s what the final config looks like.
sst.config.ts

```typescript

const isPermanentStage = ["production", "dev"].includes($app.stage);

const domain = $app.stage === "production"

?"example.com"

: $app.stage==="dev"

?"dev.example.com"

:`${$app.stage}.dev.example.com`;

functionsubdomain(name:string) {

if (isPermanentStage) return`${name}.${domain}`;

return`${name}-${domain}`;

}

const router = isPermanentStage

?new sst.aws.Router("MyRouter", {

domain: {

name: domain,

aliases: [`*.${domain}`]

}

})

: sst.aws.Router.get("MyRouter", "A2WQRGCYGTFB7Z");

// Frontend

const web = newsst.aws.Nextjs("MyWeb", {

path: "packages/web",

router: {

instance: router

}

});

// API

const api = newsst.aws.Function("MyApi", {

handler: "packages/functions/api.handler",

url: {

router: {

instance: router,

path: "/api"

}

}

});

// Docs

const docs = newsst.aws.Astro("MyDocs", {

path: "packages/docs",

router: {

instance: router,

domain: subdomain("docs")

}

});

```

Our components are all sharing the same CloudFront distribution. We also have our PR stages sharing the same router as our dev stage.

[Skip to content](https://sst.dev/docs/component/aws/cron#_top)

# Cron

The `Cron` component lets you add cron jobs to your app using `Function` or a container `Task`.

#### [Cron job function](https://sst.dev/docs/component/aws/cron#cron-job-function)

Pass in a `schedule` and a `function` that’ll be executed.
sst.config.ts

```typescript


new sst.aws.Cron("MyCronJob", {




function: "src/cron.handler",




schedule: "rate(1 minute)"



});

```

#### [Cron job container task](https://sst.dev/docs/component/aws/cron#cron-job-container-task)

Create a container task and pass in a `schedule` and a `task` that’ll be executed.
sst.config.ts

```typescript

const myCluster = newsst.aws.Cluster("MyCluster");

const myTask = newsst.aws.Task("MyTask", { cluster: myCluster });

new sst.aws.Cron("MyCronJob", {

task: myTask,

schedule: "rate(1 day)"

});

```

#### [Customize the function](https://sst.dev/docs/component/aws/cron#customize-the-function)

sst.config.ts

```typescript


newsst.aws.Cron("MyCronJob", {




schedule: "rate(1 minute)",



function: {



handler: "src/cron.handler",




timeout: "60 seconds"



}


});

```

* * *

## [Constructor](https://sst.dev/docs/component/aws/cron#constructor)

```


newCron(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cron#parameters)

* `name` `string`
* `args` [`CronArgs`](https://sst.dev/docs/component/aws/cron#cronargs)
* `opts?`

## [CronArgs](https://sst.dev/docs/component/aws/cron#cronargs)

### [enabled?](https://sst.dev/docs/component/aws/cron#enabled)

**Type** `Input``<``boolean``>`
**Default** true
Configures whether the cron job is enabled. When disabled, the cron job won’t run.

```

{



enabled: false



}

```

### [event?](https://sst.dev/docs/component/aws/cron#event)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
The event that’ll be passed to the function or task.

```

{


event: {



foo: "bar",



}


}

```

For Lambda functions, the event will be passed to the function as an event.

```


functionhandler(event) {




console.log(event.foo);



}

```

For ECS Fargate tasks, the event will be passed to the task as the `SST_EVENT` environment variable.

```


const event = JSON.parse(process.env.SST_EVENT);




console.log(event.foo);


```

### [function?](https://sst.dev/docs/component/aws/cron#function)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`| ``“arn:aws:lambda:${string}”``>`
The function that’ll be executed when the cron job runs.

```

{



function: "src/cron.handler"



}

```

You can pass in the full function props.

```

{



function: {




handler: "src/cron.handler",




timeout: "60 seconds"



}


}

```

You can also pass in a function ARN.

```

{



function: "arn:aws:lambda:us-east-1:000000000000:function:my-sst-app-jayair-MyFunction",



}

```

### [schedule](https://sst.dev/docs/component/aws/cron#schedule)

**Type** `Input``<``“``rate(${string})``”`` | ``“``cron(${string})``”``>`
The schedule for the cron job.
The cron job continues to run even after you exit `sst dev`.
You can use a

```

{



schedule: "rate(5 minutes)"



// schedule: "rate(1 minute)"


// schedule: "rate(5 minutes)"


// schedule: "rate(1 hour)"


// schedule: "rate(5 hours)"


// schedule: "rate(1 day)"


// schedule: "rate(5 days)"


}

```

Or a

```

{



schedule: "cron(15 10 * * ? *)", // 10:15 AM (UTC) every day



}

```

### [task?](https://sst.dev/docs/component/aws/cron#task)

**Type** [`Task`](https://sst.dev/docs/component/aws/task)
The task that’ll be executed when the cron job runs.
For example, let’s say you have a task.
sst.config.ts

```typescript

const myCluster = newsst.aws.Cluster("MyCluster");

const myTask = newsst.aws.Task("MyTask", { cluster: myCluster });

```

You can then pass in the task to the cron job.
sst.config.ts

```typescript


newsst.aws.Cron("MyCronJob", {




task: myTask,




schedule: "rate(1 minute)"



});

```

### [transform?](https://sst.dev/docs/component/aws/cron#transform)

**Type** `Object`

* [`rule?`](https://sst.dev/docs/component/aws/cron#transform-rule)
* [`target?`](https://sst.dev/docs/component/aws/cron#transform-target)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.rule?](https://sst.dev/docs/component/aws/cron#transform-rule)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EventBridge Rule resource.

#### [transform.target?](https://sst.dev/docs/component/aws/cron#transform-target)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the EventBridge Target resource.

## [Properties](https://sst.dev/docs/component/aws/cron#properties)

### [nodes](https://sst.dev/docs/component/aws/cron#nodes)

**Type** `Object`

* [`rule`](https://sst.dev/docs/component/aws/cron#nodes-rule)
* [`target`](https://sst.dev/docs/component/aws/cron#nodes-target)
* [`function`](https://sst.dev/docs/component/aws/cron#nodes-function)
* [`job`](https://sst.dev/docs/component/aws/cron#nodes-job)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.rule](https://sst.dev/docs/component/aws/cron#nodes-rule)

**Type**
The EventBridge Rule resource.

#### [nodes.target](https://sst.dev/docs/component/aws/cron#nodes-target)

**Type**
The EventBridge Target resource.

#### [nodes.function](https://sst.dev/docs/component/aws/cron#nodes-function)

**Type** `Output``<`[`Function`](https://sst.dev/docs/component/aws/function)`>`
The AWS Lambda Function that’ll be invoked when the cron job runs.

#### [nodes.job](https://sst.dev/docs/component/aws/cron#nodes-job)

**Type** `Output``<`[`Function`](https://sst.dev/docs/component/aws/function)`>`
The AWS Lambda Function that’ll be invoked when the cron job runs.

[Skip to content](https://sst.dev/docs/component/aws/cognito-identity-provider#_top)

# CognitoIdentityProvider

The `CognitoIdentityProvider` component is internally used by the `CognitoUserPool` component to add identity providers to your
This component is not intended to be created directly.
You’ll find this component returned by the `addIdentityProvider` method of the `CognitoUserPool` component.
* * *

## [Constructor](https://sst.dev/docs/component/aws/cognito-identity-provider#constructor)

```


newCognitoIdentityProvider(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cognito-identity-provider#parameters)

* `name` `string`
* `args` [`Args`](https://sst.dev/docs/component/aws/cognito-identity-provider#args)
* `opts?`

## [Properties](https://sst.dev/docs/component/aws/cognito-identity-provider#properties)

### [nodes](https://sst.dev/docs/component/aws/cognito-identity-provider#nodes)

**Type** `Object`

* [`identityProvider`](https://sst.dev/docs/component/aws/cognito-identity-provider#nodes-identityprovider)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.identityProvider](https://sst.dev/docs/component/aws/cognito-identity-provider#nodes-identityprovider)

**Type**
The Cognito identity provider.

### [providerName](https://sst.dev/docs/component/aws/cognito-identity-provider#providername)

**Type** `Output``<``string``>`
The Cognito identity provider name.

## [Args](https://sst.dev/docs/component/aws/cognito-identity-provider#args)

### [attributes?](https://sst.dev/docs/component/aws/cognito-identity-provider#attributes)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Define a mapping between identity provider attributes and user pool attributes.

```

{



email: "email",




username: "sub"



}

```

### [details](https://sst.dev/docs/component/aws/cognito-identity-provider#details)

**Type** `Input``<``Record``<``string`, `Input``<``string``>``>``>`
Configure the identity provider details, including the scopes, URLs, and identifiers.

```

{



authorize_scopes: "email profile",




client_id: "your-client-id",




client_secret: "your-client-secret"



}

```

### [transform?](https://sst.dev/docs/component/aws/cognito-identity-provider#transform)

**Type** `Object`

* [`identityProvider?`](https://sst.dev/docs/component/aws/cognito-identity-provider#transform-identityprovider)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.identityProvider?](https://sst.dev/docs/component/aws/cognito-identity-provider#transform-identityprovider)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Cognito identity provider resource.

### [type](https://sst.dev/docs/component/aws/cognito-identity-provider#type)

**Type** `Input``<``“``oidc``”`` | ``“``saml``”`` | ``“``google``”`` | ``“``facebook``”`` | ``“``apple``”`` | ``“``amazon``”``>`
The type of identity provider.

### [userPool](https://sst.dev/docs/component/aws/cognito-identity-provider#userpool)

**Type** `Input``<``string``>`
The Cognito user pool ID.

[Skip to content](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#_top)

# SnsTopicQueueSubscriber

The `SnsTopicQueueSubscriber` component is internally used by the `SnsTopic` component to add subscriptions to your
This component is not intended to be created directly.
You’ll find this component returned by the `subscribeQueue` method of the `SnsTopic` component.
* * *

## [Constructor](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#constructor)

```


newSnsTopicQueueSubscriber(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#parameters)

* `name` `string`
* `args` [`Args`](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#args)
* `opts?`

## [Properties](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#properties)

### [nodes](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#nodes)

**Type** `Object`

* [`policy`](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#nodes-policy)
* [`subscription`](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#nodes-subscription)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.policy](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#nodes-policy)

**Type**
The SQS Queue policy.

#### [nodes.subscription](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#nodes-subscription)

**Type**
The SNS Topic subscription.

## [Args](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#args)

### [filter?](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#filter)

**Type** `Input``<``Record``<``string`, `any``>``>`
Filter the messages that’ll be processed by the subscriber.
If any single property in the filter doesn’t match an attribute assigned to the message, then the policy rejects the message.
Learn more about
For example, if your SNS Topic message contains this in a JSON format.

```

{



store: "example_corp",




event: "order-placed",



customer_interests: [



"soccer",




"rugby",




"hockey"



],



price_usd: 210.75



}

```

Then this filter policy accepts the message.

```

{


filter: {



store: ["example_corp"],




event: [{"anything-but": "order_cancelled"}],



customer_interests: [



"rugby",




"football",




"baseball"



],



price_usd: [{numeric: [">=", 100]}]



}


}

```

### [queue](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#queue)

**Type** `Input``<``string`` |`[`Queue`](https://sst.dev/docs/component/aws/queue)`>`
The ARN of the SQS Queue.

### [topic](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#topic)

**Type** `Input``<``Object``>`

* [`arn`](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#topic-arn)

The SNS Topic to use.

#### [topic.arn](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#topic-arn)

**Type** `Input``<``string``>`
The ARN of the SNS Topic.

### [transform?](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#transform)

**Type** `Object`

* [`subscription?`](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#transform-subscription)

[Transform](https://sst.dev/docs/components#transform) how this subscription creates its underlying resources.

#### [transform.subscription?](https://sst.dev/docs/component/aws/sns-topic-queue-subscriber#transform-subscription)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the SNS Topic Subscription resource.

[Skip to content](https://sst.dev/docs/component/aws/cognito-user-pool-client#_top)

# CognitoUserPoolClient

The `CognitoUserPoolClient` component is internally used by the `CognitoUserPool` component to add clients to your
This component is not intended to be created directly.
You’ll find this component returned by the `addClient` method of the `CognitoUserPool` component.
* * *

## [Constructor](https://sst.dev/docs/component/aws/cognito-user-pool-client#constructor)

```


newCognitoUserPoolClient(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/cognito-user-pool-client#parameters)

* `name` `string`
* `args` [`Args`](https://sst.dev/docs/component/aws/cognito-user-pool-client#args)
* `opts?`

## [Properties](https://sst.dev/docs/component/aws/cognito-user-pool-client#properties)

### [id](https://sst.dev/docs/component/aws/cognito-user-pool-client#id)

**Type** `Output``<``string``>`
The Cognito User Pool client ID.

### [nodes](https://sst.dev/docs/component/aws/cognito-user-pool-client#nodes)

**Type** `Object`

* [`client`](https://sst.dev/docs/component/aws/cognito-user-pool-client#nodes-client)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.client](https://sst.dev/docs/component/aws/cognito-user-pool-client#nodes-client)

**Type**
The Cognito User Pool client.

### [secret](https://sst.dev/docs/component/aws/cognito-user-pool-client#secret)

**Type** `Output``<``string``>`
The Cognito User Pool client secret.

## [SDK](https://sst.dev/docs/component/aws/cognito-user-pool-client#sdk)

Use the [SDK](https://sst.dev/docs/reference/sdk/) in your runtime to interact with your infrastructure.
* * *

### [Links](https://sst.dev/docs/component/aws/cognito-user-pool-client#links)

This is accessible through the `Resource` object in the [SDK](https://sst.dev/docs/reference/sdk/#links).

* `id` `string`
The Cognito User Pool client ID.
* `secret` `string`
The Cognito User Pool client secret.

## [Args](https://sst.dev/docs/component/aws/cognito-user-pool-client#args)

### [providers?](https://sst.dev/docs/component/aws/cognito-user-pool-client#providers)

**Type** `Input``<``Input``<``string``>``[]``>`
**Default** `[“COGNITO”]`
A list of identity providers that are supported for this client.
Reference federated identity providers using their `providerName` property.
If you are using a federated identity provider.
sst.config.ts

```typescript

const provider = userPool.addIdentityProvider("MyProvider", {

type: "oidc",

details: {

authorize_scopes: "email profile",

client_id: "your-client-id",

client_secret: "your-client-secret"

},

});

```

Make sure to pass in `provider.providerName` instead of hardcoding it to `"MyProvider"`.
sst.config.ts

```typescript


userPool.addClient("Web", {




providers: [provider.providerName]



});

```

This ensures the client is created after the provider.

### [transform?](https://sst.dev/docs/component/aws/cognito-user-pool-client#transform)

**Type** `Object`

* [`client?`](https://sst.dev/docs/component/aws/cognito-user-pool-client#transform-client)

[Transform](https://sst.dev/docs/components#transform) how this component creates its underlying resources.

#### [transform.client?](https://sst.dev/docs/component/aws/cognito-user-pool-client#transform-client)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the Cognito User Pool client resource.

### [userPool](https://sst.dev/docs/component/aws/cognito-user-pool-client#userpool)

**Type** `Input``<``string``>`
The Cognito user pool ID.

[Skip to content](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#_top)

# SnsTopicLambdaSubscriber

The `SnsTopicLambdaSubscriber` component is internally used by the `SnsTopic` component to add subscriptions to your
This component is not intended to be created directly.
You’ll find this component returned by the `subscribe` method of the `SnsTopic` component.
* * *

## [Constructor](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#constructor)

```


newSnsTopicLambdaSubscriber(name, args, opts?)


```

#### [Parameters](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#parameters)

* `name` `string`
* `args` [`Args`](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#args)
* `opts?`

## [Properties](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#properties)

### [nodes](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#nodes)

**Type** `Object`

* [`permission`](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#nodes-permission)
* [`subscription`](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#nodes-subscription)
* [`function`](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#nodes-function)

The underlying [resources](https://sst.dev/docs/components/#nodes) this component creates.

#### [nodes.permission](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#nodes-permission)

**Type**
The Lambda permission.

#### [nodes.subscription](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#nodes-subscription)

**Type**
The SNS Topic subscription.

#### [nodes.function](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#nodes-function)

**Type** `Output``<`[`Function`](https://sst.dev/docs/component/aws/function)`>`
The Lambda function that’ll be notified.

## [Args](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#args)

### [filter?](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#filter)

**Type** `Input``<``Record``<``string`, `any``>``>`
Filter the messages that’ll be processed by the subscriber.
If any single property in the filter doesn’t match an attribute assigned to the message, then the policy rejects the message.
Learn more about
For example, if your SNS Topic message contains this in a JSON format.

```

{



store: "example_corp",




event: "order-placed",



customer_interests: [



"soccer",




"rugby",




"hockey"



],



price_usd: 210.75



}

```

Then this filter policy accepts the message.

```

{


filter: {



store: ["example_corp"],




event: [{"anything-but": "order_cancelled"}],



customer_interests: [



"rugby",




"football",




"baseball"



],



price_usd: [{numeric: [">=", 100]}]



}


}

```

### [subscriber](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#subscriber)

**Type** `Input``<``string`` |`[`FunctionArgs`](https://sst.dev/docs/component/aws/function#functionargs)`>`
The subscriber function.

### [topic](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#topic)

**Type** `Input``<``Object``>`

* [`arn`](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#topic-arn)

The Topic to use.

#### [topic.arn](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#topic-arn)

**Type** `Input``<``string``>`
The ARN of the Topic.

### [transform?](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#transform)

**Type** `Object`

* [`subscription?`](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#transform-subscription)

[Transform](https://sst.dev/docs/components#transform) how this subscription creates its underlying resources.

#### [transform.subscription?](https://sst.dev/docs/component/aws/sns-topic-lambda-subscriber#transform-subscription)

**Type** `| ``(``args``: ``, ``opts``: ``, ``name``: ``string``)`` => ``void`
Transform the SNS Topic Subscription resource.

[Skip to content](https://sst.dev/docs/custom-domains#_top)

# Custom Domains

You can configure custom domains and subdomains for your frontends, APIs, services, or routers in SST.
SST currently supports configuring custom domains for AWS components.
By default, these components auto-generate a URL. You can pass in the `domain` to use your custom domain.

* [Frontend](https://sst.dev/docs/custom-domains#tab-panel-2)
* [API](https://sst.dev/docs/custom-domains#tab-panel-3)
* [Service](https://sst.dev/docs/custom-domains#tab-panel-4)
* [Router](https://sst.dev/docs/custom-domains#tab-panel-5)

sst.config.ts

```typescript

new sst.aws.Nextjs("MyWeb", {

domain: "example.com"

});

```

sst.config.ts

```typescript


new sst.aws.ApiGatewayV2("MyApi", {




domain: "api.example.com"



});

```

sst.config.ts

```typescript

const vpc = newsst.aws.Vpc("MyVpc");

new sst.aws.Cluster("MyCluster", {

vpc,

loadBalancer: {

domain: "example.com"

}

});

```

sst.config.ts

```typescript


new sst.aws.Router("MyRouter", {




domain: "example.com"



});

```

SST supports a couple of DNS providers automatically. These include AWS Route 53, Cloudflare, and Vercel. Other providers will need to be manually configured.
We’ll look at how it works below.
* * *

##### [Redirect www to apex domain](https://sst.dev/docs/custom-domains#redirect-www-to-apex-domain)

A common use case is to redirect `www.example.com` to `example.com`. You can do this by:
sst.config.ts

```typescript

new sst.aws.Router("MyRouter", {

domain: {

name: "example.com",

redirects: ["www.example.com"]

}

});

```

* * *

##### [Add subdomains](https://sst.dev/docs/custom-domains#add-subdomains)

You can add subdomains to your domain. This is useful if you want to use a `Router` to route a subdomain to a separate resource.
sst.config.ts

```typescript


const router = newsst.aws.Router("MyRouter", {



domain: {



"example.com",




 ["*.example.com"]



}



});




new sst.aws.Nextjs("MyWeb", {



router: {


instance: router,



domain: "docs.example.com"



}


});

```

Here if a user visits `docs.example.com`, they’ll kept on the alias domain and be served the docs site.
You can use the `Router` component to centrally manage domains and routing for your app. [Learn more](https://sst.dev/docs/configure-a-router).
However, this does not match `docs.dev.example.com`. For that, you’ll need to add `*.dev.example.com` as an alias.
* * *

## [How it works](https://sst.dev/docs/custom-domains#how-it-works)

Configuring a custom domain is a two step process.

  1. Validate that you own the domain. For AWS you do this by
     * Setting a DNS record with your domain provider.
     * Verifying through an email sent to the domain owner.
  2. Add the DNS records to route your domain to your component.

SST can perform these steps automatically for the supported providers through a concept of _adapters_. These create the above DNS records on a given provider.
* * *

## [Adapters](https://sst.dev/docs/custom-domains#adapters)

You can use a custom domain hosted on any provider. SST supports domains on AWS, Cloudflare, and Vercel automatically.
* * *

### [AWS](https://sst.dev/docs/custom-domains#aws)

By default, if you set a custom domain, SST assumes the domain is configured in AWS Route 53 in the same AWS account.

```

{


domain: {



name: "example.com"



}


}

```

This is the same as using the [`sst.aws.dns`](https://sst.dev/docs/component/aws/dns/) adapter.

```

{


domain: {



name: "example.com",




dns: sst.aws.dns()



}


}

```

If you have the same domain in multiple hosted zones in Route 53, you can specify the hosted zone.

```

{


domain: {



name: "example.com",




dns: sst.aws.dns({




zone: "Z2FDTNDATAQYW2"



})


}


}

```

If your domains are hosted on AWS but in a separate AWS account, you’ll need to follow the [manual setup](https://sst.dev/docs/custom-domains#manual-setup).
* * *

### [Vercel](https://sst.dev/docs/custom-domains#vercel)

If your domains are hosted on

  1. [Add the Vercel provider to your app](https://sst.dev/docs/component/vercel/dns/#configure-provider).
Terminal window```

sstadd@pulumiverse/vercel

```

  2. Set the **`VERCEL_API_TOKEN`**in your environment. You might also need to set the`VERCEL_TEAM_ID` if the domain belongs to a team.
Terminal window```


exportVERCEL_API_TOKEN=aaaaaaaa_aaaaaaaaaaaa_aaaaaaaa


```

  3. Use the [`sst.vercel.dns`](https://sst.dev/docs/component/vercel/dns/) adapter.

```

{


domain: {



name: "example.com",




dns: sst.vercel.dns()



}


}

```

* * *

### [Cloudflare](https://sst.dev/docs/custom-domains#cloudflare)

If your domains are hosted on

  1. Add the Cloudflare provider to your app.
Terminal window```

sstaddcloudflare

```

  2. Set the **`CLOUDFLARE_API_TOKEN`**in your environment.
Terminal window```


exportCLOUDFLARE_API_TOKEN=aaaaaaaa_aaaaaaaaaaaa_aaaaaaaa




exportCLOUDFLARE_DEFAULT_ACCOUNT_ID=aaaaaaaa_aaaaaaaaaaaa_aaaaaaaa


```

To get your API tokens, head to the **Edit zone DNS** policy.
The Cloudflare providers need these credentials to deploy your app in the first place, which means they can’t be set using the `sst secret` CLI.
If you are auto-deploying your app through the [SST Console](https://sst.dev/docs/console.mdx#autodeploy) or through your CI, you’ll need to set these as environment variables.
  3. Use the [`sst.cloudflare.dns`](https://sst.dev/docs/component/cloudflare/dns/) adapter.

```

{


domain: {



name: "example.com",




dns: sst.cloudflare.dns()



}


}

```

* * *

## [Manual setup](https://sst.dev/docs/custom-domains#manual-setup)

If your domain is on a provider that is not supported above, or is in a separate AWS account; you’ll need to verify that you own the domain and set up the DNS records on your own.
To manually set up a domain on an unsupported provider, you’ll need to:

  1. For CloudFront distributions, the certificate needs to be created in `us-east-1`.
If you are configuring a custom domain for a CloudFront distribution, the ACM certificate that’s used to prove that you own the domain needs be created in the `us-east-1` region.
For all the other components, like ApiGatewayV2 or Cluster, can be created in any region.
  2. Once validated, set the certificate ARN as the `cert` and set `dns` to `false`.

```

{


domain: {



name: "domain.com",




dns: false,




cert: "arn:aws:acm:us-east-1:112233445566:certificate/3a958790-8878-4cdc-a396-06d95064cf63"



}


}

```

  3. Add the DNS records in your provider to point to the CloudFront distribution, API Gateway, or load balancer URL.

`AccessDenied`Access Denied
This XML file does not appear to have any style information associated with it. The document tree is shown below.  

<Error>
<Code>AccessDenied</Code>
<Message>Access Denied</Message>
...
</Error>
