<script lang="ts">
    import './app.css';

    import { Router, Route } from "svelte-routing";
    import TransitionWrapper from "./components/ui/TransitionWrapper.svelte";

    import Home from "./routes/Home.svelte";
    import EmailResult from "./routes/EmailResult.svelte";
    import EmailGenerator from "./routes/EmailGenerator.svelte";
</script>

<Router>
    <Route path="/">
        <TransitionWrapper duration={300}>
            <Home/>
        </TransitionWrapper>
    </Route>
    <Route path="/page/mailing">
        <TransitionWrapper duration={300}>
            <EmailGenerator/>
        </TransitionWrapper>
    </Route>
    <Route path="/page/result">
        <TransitionWrapper duration={300}>
            <EmailResult/>
        </TransitionWrapper>
    </Route>
</Router>

