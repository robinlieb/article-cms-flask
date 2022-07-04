# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

- Analyze costs, scalability, availability, and workflow
    * Costs: Azure VMs are more expensive compared with Azure App Service. With App Service you’re always paying for the service plan, even if your services or application isn’t running.
    * Scalability: Multiple VMs can be grouped to provide high availability, scalability, and redundancy. There are two options when it comes to scaling—Virtual Machine Scale Sets and Load Balancers. Azure App Services have high availability, auto-scaling, and support of both Linux and Windows environments. There are two options when in comes to scaling, vertical or horizontal scaling. Vertical scaling increases or decreases resources allocated to our App Service, such as the amount of vCPUs or RAM, by changing the App Service pricing tier. Horizontal scaling increases or decreases the number of Virtual Machine instances our App Service is running.
    * Availability: Azure App Services have high availability, auto-scaling, and support of both Linux and Windows environments. Multiple VMs can be grouped to provide high availability, scalability, and redundancy.
    * Workflow: Azure App Services provides continuous deployment model using GitHub, Azure DevOps, or any Git repo. More steps required to automate deployment to Azure VM.

I would use App Service as a solution for deploying the app because of following reasons:
- Cheaper compared to VMs.
- I currently have not the requirement to change something on the underlying operations system.
- Easier to automate and set up CI/CD.
- App Service does support Python as stack which the app is written in.
- Less concern about scaling up processing power.

### Assess app changes that would change your decision.

- The app will be migrated to another programming language which is not supported by App Service.
- The app would exceed the limit of 4 vCPU and 14GB of memory per instance. 
- The app would require access to the underlying operating system for example to install additional software.
