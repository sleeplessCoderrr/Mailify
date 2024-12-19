<script lang="ts">
    import './app.css';
    import Home from "./routes/Home.svelte";
    import { Router, Route } from "svelte-routing";
    import EmailGenerator from "./routes/EmailGenerator.svelte";
    import TransitionWrapper from "./components/ui/TransitionWrapper.svelte";
</script>

<Router>
    <Route path="/">
        <TransitionWrapper duration={300}>
            <Home/>
        </TransitionWrapper>
    </Route>
    <Route path="/mailing">
        <TransitionWrapper duration={300}>
            <EmailGenerator/>
        </TransitionWrapper>
    </Route>
</Router>

